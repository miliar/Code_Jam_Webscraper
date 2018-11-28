#include <iostream>
#include <cassert>
#include <string>
#include <set>

std::string solve(const std::set<int>& first, const std::set<int>& second) {
    std::set<int> solution;
    for (const auto e : first) {
        if (second.find(e) != second.end())
            solution.insert(e);
    }
    if (solution.size() == 1) {
        int sol = *solution.begin();
        return std::to_string(sol);
    } else if (solution.empty()) {
        return "Volunteer cheated!";
    } else {
        return "Bad magician!";
    }
}

std::set<int> readRow() {
    std::set<int> row;
    for(int i = 1; i <= 4; ++i) {
        int card;
        std::cin >> card;
        row.insert(card);
    }
    return row;
}

std::set<int> readNthRowFromBoard(const int rowNum) {
    assert(rowNum > 0);
    assert(rowNum < 5);
    std::set<int> ret;
    for (int i = 1; i <= 4; ++i) {
        auto row = readRow();
        if (i == rowNum)
            ret = row;
    }
    return ret;
}

int main() {
    int T;
    std::cin >> T;
    for(int i = 1; i <= T; ++i) {
        int selection1;
        std::cin >> selection1;
        auto firstRow = readNthRowFromBoard(selection1);
        int selection2;
        std::cin >> selection2;
        auto secondRow = readNthRowFromBoard(selection2);
        std::cout << "Case #" << i << ": " <<
            solve(firstRow, secondRow) << std::endl;
    }
}
