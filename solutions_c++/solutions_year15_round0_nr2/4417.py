#include <iostream>
#include <vector>
#include <set>

int worst_case = 0;

int indentLevel = -1;
void indent() {
    auto x = indentLevel;
    while (x--) std::cout << "    ";
}

int calculate(std::multiset<int> plates, int toSplit, int split) {
    indentLevel++;
    if (indentLevel > worst_case + 2) {
        indentLevel--;
        return 100000000;
    }
//    indent();
//    std::cout << "calculate([";
//    bool isFirst = true;
//    for (auto element : plates) {
//        if (!isFirst) {
//            std::cout << ", ";
//        }
//        std::cout << element;
//        isFirst = false;
//    }
//    std::cout << "], " << toSplit << ", " << split << ")" << std::endl;
    /*
     * each case can be reduced to two kind of decision
     * split or not split
     * but you have two options to split
     * one, to continue the last split, for example, split 9 into 3 parts, instead of 2, or
     * two, make new split.
     */
    
    std::vector<int> possibleCases;
    
    // Case 1, Don't Split At All!
    // merge back
    
    auto mergedPlates = plates;
    
    for (int i = 0; i < split; ++i) {
        if (i < toSplit % split) {
            mergedPlates.insert(toSplit / split + 1);
        } else {
            mergedPlates.insert(toSplit / split);
        }
    }
    
    possibleCases.push_back(*(mergedPlates.rbegin()));
    
    // Case 2. Continue Current Split (if in split process of course)
    if (toSplit != 0) {
        // You should not split 10 pancakes into 11 plates, so stop at 10/10.
        if (toSplit != split) {
            possibleCases.push_back(1 + calculate(plates, toSplit, split + 1));
        }
    }
    
    // Case 3. Make New Split
    // Two case
    //   - currently in split, then we need to combine old splits.
    //   - split largest plate
    
    auto newPlates = plates;
    if (toSplit != 0) {
        // merge old split
        for (int i = 0; i < split; ++i) {
            if (i < toSplit % split) {
                newPlates.insert(toSplit / split + 1);
            } else {
                newPlates.insert(toSplit / split);
            }
        }
    }
    
    // create new split
    int largest = *(newPlates.rbegin());
    if (largest != 1) {
        auto it = newPlates.begin();
        for (int q = 0; q < newPlates.size() - 1; ++ q) {
            it++;
        }
        newPlates.erase(it);
        possibleCases.push_back(1 + calculate(newPlates, largest, 2));
    } else {
        possibleCases.push_back(1);
    }
    indentLevel--;
    return *(std::min_element(possibleCases.begin(), possibleCases.end()));
}

int main(int argc, char** argv) {
    std::ios_base::sync_with_stdio(false);
    int nCase = 0;
    
    std::cin >> nCase;
    for (int i = 1; i <= nCase; ++i) {
        int nPlate = 0;
        int thisPlate = 0;
        std::cin >> nPlate;
        std::multiset<int> plates;
        while (nPlate--) {
            std::cin >> thisPlate;
            plates.insert(thisPlate);
        }
        worst_case = *(plates.rbegin());
        int answer = calculate(plates, 0, 0);
        std::cout << "Case #" << i << ": " << answer << std::endl;
    }
}