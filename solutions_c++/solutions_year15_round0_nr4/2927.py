#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <vector>

#include <cmath>

#define DEBUG(x) x

using Pos = std::pair<int, int>;
using Omino = std::set<Pos>;

Omino rebase(const Omino& o) {
    Pos origin = { 0, 0 };
    for (const auto& pos: o) {
        origin.first = std::min(pos.first, origin.first);
        origin.second = std::min(pos.second, origin.second);
    }
    Omino o2;
    for (const auto& pos: o)
        o2.insert({ pos.first - origin.first, pos.second - origin.second });
    return o2;
}

Pos size(const Omino& o) {
    Pos size = { 0, 0 };
    for (const auto& pos: o) {
        size.first = std::max(pos.first + 1, size.first);
        size.second = std::max(pos.second + 1, size.second);
    }
    return size;
}

Omino rotate(const Omino& o) {
    Omino o2;
    for (const auto& pos: o)
        o2.insert({ -pos.second, pos.first });
    return rebase(o2);
}

Omino flip(const Omino& o) {
    Pos size(::size(o));
    Omino o2;
    for (const auto& pos: o)
        o2.insert({ -pos.first, pos.second });
    return rebase(o2);
}

std::ostream& operator<<(std::ostream& s, const Omino& o) {
    Pos size(::size(o));
    std::string display;
    for (int y = -1; y < size.second + 1; ++y) {
        for (int x = -1; x < size.first + 1; ++x)
            display += o.find({ x, y }) != o.end() ? 'X' : ' ';
        display += '\n';
    }
    return s << display;
}

bool canAlwaysFit(const std::set<Omino>& ominoes, const int count, const int width, const int height) {
    //DEBUG(std::cerr << "Fitting " << count << " ominoes in a " << width << 'x' << height << " grid\n");
    std::vector<const Omino*> stateV(count);
    std::multiset<const Omino*> stateS;
    std::map<std::multiset<const Omino*>, bool> alreadyTried;
    std::set<Pos> grid;
    std::function<bool(int)> choosePositions = [&](int i) {
        if (i == count) {
            if (grid.size() != width * height)
                abort();
            for (const auto& pos: grid) {
                if (pos.first < 0 or pos.second < 0)
                    abort();
                if (pos.first >= width or pos.second >= height)
                    abort();
            }
            int sum = 0;
            for (const Omino* o: stateV)
                sum += o->size();
            if (sum != width * height)
                abort();
            return true;
        }
        Omino o(*stateV[i]);
        for (int side = 0; side < 2; ++side, o = flip(o)) {
            for (int angle = 0; angle < 4; ++angle, o = rotate(o)) {
                Pos translation;
                Pos size(::size(o));
                for (translation.second = 0; translation.second < height - size.second + 1; ++translation.second) {
                    for (translation.first = 0; translation.first < width - size.first + 1; ++translation.first) {
                        bool overlap = false;
                        for (const auto& pos: o) {
                            //DEBUG(std::cerr << grid.size());
                            if (not grid.insert({ pos.first + translation.first, pos.second + translation.second }).second) {
                                overlap = true;
                                //DEBUG(std::cerr << "woops " << i << " for " << size.first << 'x' << size.second << '\n');
                                for (const auto& pos2: o) {
                                    if (pos2 == pos)
                                        break;
                                    grid.erase({ pos2.first + translation.first, pos2.second + translation.second });
                                }
                                break;
                            }
                        }
                        if (overlap)
                            continue;
                        bool fitting = choosePositions(i + 1);
                        for (const auto& pos: o)
                            grid.erase({ pos.first + translation.first, pos.second + translation.second });
                        if (fitting) {
                            //DEBUG(std::cout << o);
                            return true;
                        }
                    }
                }
            }
        }
        return false;
    };
    std::function<bool(int)> chooseOminos = [&](int i) {
        if (i < count) {
            for (const auto& o: ominoes) {
                stateV[i] = &o;
                stateS.insert(&o);
                bool fitting = chooseOminos(i + 1);
                stateS.erase(stateS.find(&o));
                //DEBUG(if (i == 0) std::cerr << (fitting ? "fitting:" : "not fitting:") << *stateV[0]);
                if (i == 0 and not fitting)
                    return false;
                if (i != 0 and fitting)
                    return true;
            }
            return i == 0;
        } else {
            auto previous = alreadyTried.find(stateS);
            bool fitting;
            if (previous != alreadyTried.end()) {
                fitting = previous->second;
            } else {
                fitting = choosePositions(0);
                if (not alreadyTried.insert(std::make_pair(stateS, fitting)).second)
                    abort();
            }
            return fitting;
        }
    };
    return chooseOminos(0); // XXX
}

#pragma omp critical
const std::set<Omino>& generateOminoes(int X) {
    // ★★★ BUILD _ALL_ THE THINGS!! ★★★
    static std::map<int, std::set<Omino>> ominoCache;
    if (ominoCache.find(X) != ominoCache.end())
        return ominoCache[X];
    std::set<Omino> ominoes = { { { 0, 0 } } };
    for (int i = 1; i < X; ++i) {
        decltype(ominoes) newOminoes;
        for (const auto& omino: ominoes) {
            for (const auto& pos: omino) {
                for (const auto& change: std::set<Pos>{ { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 } }) {
                    Omino newOmino(omino);
                    Pos newPos = { pos.first + change.first, pos.second + change.second };
                    if (not newOmino.insert(newPos).second)
                        continue;
                    newOminoes.insert(newOmino);
                }
            }
        }
        ominoes.swap(newOminoes);
    }
    {
        decltype(ominoes) newOminoes;
        for (const auto& omino: ominoes) {
            if (omino.size() != X)
                abort();
            Omino trans(rebase(omino));
            bool insert = true;
            for (int i = 0; i < 4 and insert; ++i) {
                if (newOminoes.find(trans) != newOminoes.end()
                    or newOminoes.find(flip(trans)) != newOminoes.end())
                    insert = false;
                trans = rotate(trans);
            }
            //DEBUG(std::cerr << (insert ? "keeping" : "removing") << trans);
            if (insert)
                newOminoes.insert(trans);
        }
        ominoes.swap(newOminoes);
    }
    DEBUG(std::cerr << X << "-ominoes: " << ominoes.size() << '\n');
    //DEBUG(for (auto omino: ominoes) std::cerr << omino);
    return ominoCache[X] = ominoes;
}

bool canAlwaysBeFilled(const int X, const int R, const int C) {
    // the cell count must be a multiple of the omino size
    // but with 7 cells or more, you can frame an empty one anyway
    // 
    //  XXX
    //  X X
    //  XX
    // 
    if (R * C % X != 0 or X >= 7)
        return false;
    
    return canAlwaysFit(generateOminoes(X), R * C / X, R, C);
}

int main() {
    std::istream& in(std::cin);
    std::ostream& out(std::cout);
    int tests;
    in >> tests;
    
    for (int i = 1; i < 7; ++i)
        generateOminoes(i);
    
    #pragma omp parallel for ordered schedule(dynamic)
    for (int test = 1; test <= tests; ++test) {
        int X, R, C;
        #pragma omp ordered
        in >> X >> R >> C;
        if (not in)
            abort();
        
        std::string winner = canAlwaysBeFilled(X, R, C) ? "GABRIEL" : "RICHARD";
        
        #pragma omp ordered
        out << "Case #" << test << ": " << winner << std::endl;
    }
}
