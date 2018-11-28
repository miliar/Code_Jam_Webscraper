#include <algorithm>
#include <iostream>
#include <vector>
#include <set>

#include <boost/function.hpp>

std::set<double> readBricks(const int amount) {
    std::set<double> bricks;
    for(int i = 0; i < amount; ++i) {
        double weight;
        std::cin >> weight;
        bricks.insert(weight);
    }
    return bricks;
}

double naomiWarMove(std::set<double>& bricks) {
    const double selection = *bricks.rbegin();
    bricks.erase(--bricks.rbegin().base());
    return selection;
}

double kenWarMove(const double naomiMove, std::set<double>& bricks) {
    auto bigger = std::upper_bound(bricks.begin(), bricks.end(), naomiMove);
    if (bigger != bricks.end()) {
        const double selection = *bigger;
        bricks.erase(bigger);
        return selection;
    }
    const double smallest = *bricks.begin();
    bricks.erase(bricks.begin());
    return smallest;
}

int war(const std::set<double>& naomi, const std::set<double>& ken) {
    std::set<double> naomiBricks{naomi};
    std::set<double> kenBricks{ken};
    const auto size = naomi.size();
    int naomiScore = 0;
    for(size_t i = 0; i < size; ++i) {
        double naomiMove = naomiWarMove(naomiBricks);
        double kenMove = kenWarMove(naomiMove, kenBricks);
        if (kenMove < naomiMove) {
            naomiScore++;
        }
    }
    return naomiScore;
}

double naomiWarDMove(std::set<double>& naomiBricks, const std::set<double>& kenBricks) {
    const double naomiSmallest = *naomiBricks.begin();
    naomiBricks.erase(naomiBricks.begin());
    if (naomiBricks.size() == 1) {
        return naomiSmallest;
    }
    const double kenBiggest = *kenBricks.rbegin();
    const double kenSecondBiggest = *(++kenBricks.rbegin());
    if (naomiSmallest > kenBiggest) {
        return naomiSmallest;
    }
    const double solution = kenSecondBiggest + ((kenBiggest - kenSecondBiggest)/2.0);
    std::cerr << kenBiggest << " " << kenSecondBiggest << " " << solution << " (" << naomiSmallest << ")\n";
    return solution;
}

const double epsilon = 0.0000001;

double naomiWarDMove2(std::set<double>& naomiBricks, const std::set<double>& kenBricks) {
    if (naomiBricks.size() == 1) {
        const double ret = *naomiBricks.begin();
        naomiBricks.erase(naomiBricks.begin());
        return ret;
    }
    const double smallestNaomi    = *naomiBricks.begin();
    const double smallestKen      = *kenBricks.begin();
    const double biggestKen       = *kenBricks.rbegin();
    const double secondBiggestKen = *(++kenBricks.rbegin());
    if (smallestNaomi < smallestKen) {
        const double dist = biggestKen - secondBiggestKen;
        const double ret = secondBiggestKen + dist/2.0;
        naomiBricks.erase(naomiBricks.begin());
        return ret;
    } else {
        naomiBricks.erase(naomiBricks.begin());
        return biggestKen + epsilon;
    }
    return 0;
}

int warD(const std::set<double>& naomi, const std::set<double>& ken) {
    std::set<double> naomiBricks{naomi};
    std::set<double> kenBricks{ken};
    const auto size = naomi.size();
    int naomiScore = 0;
    for(size_t i = 0; i < size; ++i) {
        double naomiMove = naomiWarDMove2(naomiBricks, kenBricks);
        double kenMove = kenWarMove(naomiMove, kenBricks);
        if (kenMove < naomiMove) {
            naomiScore++;
        }
    }
    return naomiScore;
}

std::pair<int, int> solve(const std::set<double>& naomi, const std::set<double>& ken) {
    return std::make_pair(
        warD(naomi, ken),
        war(naomi, ken)
    );
}

void readAndSolve(const int caseNumber) {
    int N;
    std::cin >> N;
    auto naomi = readBricks(N);
    auto ken   = readBricks(N);
    auto solution = solve(naomi, ken);
    std::cout << "Case #" << caseNumber << ": " << solution.first << " " <<
        solution.second << std::endl;
}

int main() {
    int T;
    std::cin >> T;
    for(int i = 1; i <= T; ++i) {
        readAndSolve(i);
    }
}
