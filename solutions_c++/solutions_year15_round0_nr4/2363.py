#include <string>
#include <set>
#include <iostream>
#include <algorithm>

int DIR[][2] = { {-1,0}, {0,-1}, {1,0}, {0,1} };

void generate_all(int size, std::set<std::string> &output, int nx, int ny, std::string current, int limit) {
    current[nx+ny*size] = '#';
    if (limit == 0) {
        output.insert(current);
        return;
    }
    for (int i=0; i<size; ++i)
        for (int j=0; j<size; ++j)
            if (current[i+j*size] == '#') {
                for (auto d : DIR) {
                    int nnx = nx+d[0];
                    int nny = ny+d[1];
                    if (nnx >= 0 && nny >= 0 && nnx < size && nny < size && current[nnx+nny*size] == ' ')
                        generate_all(size, output, nnx, nny, current, limit-1);
                }
            }
}

void generate_all(int size, std::set<std::string> &output) {
    output.clear();
    std::string current;
    current.reserve(size*size);
    for (int i=0; i<size*size; ++i) current += ' ';
    for (int i=0; i<size; ++i)
        for (int j=0; j<size; ++j)
            generate_all(size, output, i, j, current, size-1);
}

bool canGabriel(int x, int width, int height) {
    if ((x>width && x> height) || width*height % x != 0) return false;
    return (x%2==0 ? x/2 : x/2+1) <= std::min(width, height);
}

bool canPlace(int width, int height, std::string const &table, int omiSize, std::string const &omi, int x, int y) {
    for (int i=0; i<omiSize; ++i)
        for (int j=0; j<omiSize; ++j)
        {
            int tx = i+x, ty = j+y;
            if (omi[i+j*omiSize] == '#') {
                if (tx >= width || ty >= height || tx<0 || ty<0) return false;
                if (table[tx+ty*width] == '#') return false;
            }
        }
    return true;
}

bool place(int width, int height, std::string &table, int omiSize, std::string const &omi, int x, int y) {
    if (!canPlace(width, height, table, omiSize, omi, x, y)) return false;
    for (int i=0; i<omiSize; ++i)
        for (int j=0; j<omiSize; ++j)
        {
            int tx = i+x, ty = j+y;
            if (omi[i+j*omiSize] != ' ') table[tx+ty*width] = '#';
        }
    return true;
}

bool isDone(std::string const &table) {
    return std::all_of(table.cbegin(), table.cend(), [] (char c) { return c == '#'; });
}

bool brute(int x, int width, int height, std::set<std::string> const &omi_list, std::string const &table) {
    std::string new_table = table;
    for (int i=0; i<width; ++i)
        for (int j=0; j<height; ++j)
            for (auto omi : omi_list)
            {
                if (place(width, height, new_table, x, omi, i, j)) {
                    if (isDone(new_table)) return true;
                    if (brute(x, width, height, omi_list, new_table)) return true;
                    new_table = table;
                }
            }
    return false;
}

bool canSolve(int x, int width, int height, std::set<std::string> &omi_list, std::string const &omi, std::string const &table) {
    std::string new_table = table;
    for (int i=1-x; i<width; ++i)
        for (int j=1-x; j<height; ++j)
            if (place(width, height, new_table, x, omi, i, j)) {
                //std::cout << "CAN_SOLVE\n";
                if (isDone(new_table)) return true;
                if (brute(x, width, height, omi_list, new_table)) return true;
                new_table = table;
            }
    return false;
}

std::string transpose(int width, std::string const &omi) {
    std::string output = omi;
    for (int i=0; i<width; ++i)
        for (int j=0; j<width; ++j)
            output[i+j*width] = omi[i*width+j];
    return output;
}

bool brute(int x, int width, int height, std::set<std::string> &omi_list) {
    std::string table;
    table.reserve(width*height);
    for (int i=0; i<width*height; ++i) table += ' ';
    //#pragma omp parallel
    for (auto omi : omi_list) {
        //std::cout << "try omi: '" << omi  << "'" << std::endl;
        if (!canSolve(x, width, height, omi_list, omi, table)) {
            std::string tomi = transpose(x, omi);
            //std::cout << "try transpose: '" << tomi << "'" << std::endl;
            if (omi == tomi || !canSolve(x, width, height, omi_list, tomi, table)) {
                //std::cout << "solve failed: '" << omi << "' '" << tomi << "'" << std::endl;
                return false;
            }
        }
    }
    return true;
}

bool solve(int x, int width, int height, std::set<std::string> &omi_list) {
    if (!canGabriel(x, width, height)) return false;
    if (x <= 3) return true;
    return brute(x, width, height, omi_list);
}

int main() {
    std::vector<std::set<std::string>> all_omi;
    all_omi.emplace({});
    for (int i=1; i<=4; ++i) {
        std::set<std::string> omi_list;
        generate_all(i, omi_list);
        all_omi.push_back(omi_list);
    }
    int k;
    std::cin >> k;
    for (int i=0; i<k; ++i) {
        int x, width, height;
        std::cin >> x >> width >> height;
        std::cout << "Case #" << i+1 << ": " << (solve(x, width, height, all_omi[x]) ? "GABRIEL" : "RICHARD") << std::endl;
    }
    //for (auto pos : all_possible) std::cout << pos << std::endl;
}
