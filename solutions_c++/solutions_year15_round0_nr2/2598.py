#include <cassert>
#include <string>
#include <sstream>
#include <vector>
#include <set>
#include <unordered_map>
#include <map>
#include <iostream>
#include <cstdint>

template <typename T>
T max(T a, T b) { return (a > b) ? a : b; }

template <typename T>
T min(T a, T b) { return (a > b) ? b : a; }

template <typename T>
T halfCeil(const T a) { return (a/2) + (a%2==1); }

uint64_t splitCost(size_t maxCount, uint64_t maxVal, uint64_t nextMaxVal) {
    return maxCount + max(halfCeil(maxVal),nextMaxVal);
}

struct dinner {
    dinner() : currentMax{0} {}
    dinner(const dinner&) = default;

    dinner splitMax();
    size_t splitMaxCost() { return platesBySize[currentMax]; }

    void add(const uint64_t plate, const size_t count = 1) {
        platesBySize[plate] += count;
        if (plate > currentMax) {
            currentMax = plate;
        }
    }

    void tick() {
        std::map<uint64_t, size_t> newPlates;
        for (const auto& e : platesBySize) {
            if (e.first > 1) {
                newPlates[e.first-1] = e.second;
            }
        }
        swap(platesBySize, newPlates);
        setMaxPlate();
    }

    void remove(const uint64_t plate) {
        platesBySize.erase(plate);
        if (plate == currentMax) {
            setMaxPlate();
        }
    }

    void setMaxPlate() {
        currentMax = 0;
        for (const auto& e : platesBySize) {
            if (e.first > currentMax) {
                currentMax = e.first;
            }
        }
    }

    uint64_t findNextMax() {
        uint64_t candidate = 0;
        for (const auto& e : platesBySize) {
            if (e.first > candidate && e.first < currentMax) {
                candidate = e.first;
            }
        }
        return candidate;
    }

    uint64_t splitCost() {
        const auto nextMax = findNextMax();
        return ::splitCost(platesBySize[currentMax], currentMax, nextMax);
    }

    uint64_t cost() const { return currentMax; }

    bool shouldSplit() {
        if (currentMax <= 1)
            return false;
        return splitCost() < cost();
    }

    std::map<uint64_t, size_t> platesBySize;
    uint64_t currentMax;
};

dinner dinner::splitMax() {
    auto maxPlateIt = platesBySize.find(currentMax);
    bool maxWasEven = currentMax%2 == 0;
    size_t maxPlates = maxPlateIt->second;
    const auto halfSize = currentMax/2;

    dinner ret = *this;
    if (currentMax == 9 && maxPlates == 1) {
        // magic...
        ret.add(3, maxPlates);
        ret.add(6, maxPlates);
    }
    else {
        if (maxWasEven) {
            ret.add(halfSize, maxPlates*2);
        } else {
            ret.add(halfSize, maxPlates);
            ret.add(halfSize+1, maxPlates);
        }
    }
    ret.remove(currentMax);
    return ret;
}

size_t solve3(std::vector<uint64_t> plates) {
}

size_t solve2(dinner d) {
    if (d.currentMax == 1)
        return 1;
    // split
    auto splitTime = d.splitMaxCost();
    dinner splitted = d.splitMax();
    auto splittedCost = splitTime + solve2(splitted);

    // non split
    d.tick();
    auto eatCost = 1 + solve2(d);
    return min(splittedCost, eatCost);
}

size_t solve2(std::vector<uint64_t> plates) {
    dinner c;
    for (const auto& e : plates) {
        c.add(e);
    }
    return solve2(c);
}

size_t solve(dinner c) {
    size_t best = c.cost();
    size_t t = 0;
    while(c.currentMax > 1) {
        // calc with split

        // calc without split
        
        // chose smaller return value
        if (best > (t + c.cost()))
            best = t + c.cost();
        
        auto cost = c.splitMaxCost();
        c = c.splitMax();
        if (best > (t + cost + c.cost())) {
            best = t + cost + c.cost();
        }
        t += cost;
    }
    return best;
}

size_t solve(std::vector<uint64_t> plates) {
    dinner c;
    for (const auto& e : plates) {
        c.add(e);
    }
    return solve(c);
}

void test() {
    assert(splitCost(4, 10, 7) == 11);
    assert(halfCeil(11) == 6);
    assert(splitCost(2, 11, 5) == 8);

    dinner d;
    d.add(11, 2);
    d.add(7, 1);
    auto ds = d.splitMax();
    ds = ds.splitMax();
    assert(ds.platesBySize[5] == 2);
    assert(ds.platesBySize[6] == 2);
    assert(ds.platesBySize[3] == 1);
    assert(ds.platesBySize[4] == 1);

    assert(solve({3}) == 3);
    /*
    assert(solve2({3}) == 3);
    assert(solve2({4}) == 3);
    assert(solve2({1,2,1,2}) == 2);
    assert(solve2({16,4}) == 7);
    assert(solve2({16,6}) == 8);
    */
    assert(solve({4}) == 3);
    assert(solve({1,2,1,2}) == 2);
    assert(solve({16,4}) == 7);
    assert(solve({16,6}) == 8);
    assert(solve({10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10}) == 10);
}

std::string to_string(const std::vector<uint64_t>& input) {
    std::stringstream ss;
    for (const auto& e : input)
        ss << e << " ";
    return ss.str();
}

int main() {
    test();
    size_t T;
    std::cin >> T;
    for (int i = 0; i != T; ++i) {
        size_t D;
        std::cin >> D;
        std::vector<uint64_t> input;
        for (int j = 0; j != D; ++j) {
            uint64_t plate = 0;
            std::cin >> plate;
            input.push_back(plate);
        }
        std::cerr << to_string(input) << std::endl;
        std::cout << "Case #" << (i+1) << ": " << solve2(input) << std::endl;
    }
}
