#include <iostream>
#include <vector>

std::vector<int> g_inputs;
std::vector<int> g_outputs;

void OvationLogic() {
    int minFriends = 0;
    int total = 0;

    for (size_t inputIdx = 0; inputIdx < g_inputs.size(); inputIdx++) {
        if (inputIdx == 0) {
            total += g_inputs[inputIdx];
            continue;
        }
        if ((g_inputs[inputIdx] > 0) && (inputIdx > total)) {
            minFriends += inputIdx - total;
            total += minFriends;
        }
        total += g_inputs[inputIdx];
        if (total >= g_inputs.size() - 1) break;
    }
    g_outputs.push_back (minFriends);
}

int main (int argc, char *argv[]) {
    int noOfCases;

    std::cin >> noOfCases;
    for (int caseIdx = 0; caseIdx < noOfCases; caseIdx++) {
        int shyLevel;
        char ignoreSpace;

        std::cin >> shyLevel;
        ignoreSpace = std::cin.get();
        for (int shyIdx = 0; shyIdx <= shyLevel; shyIdx++) {
            char inputCh = std::cin.get();
            int input = inputCh - 48;
            g_inputs.push_back (input);
        }
        OvationLogic();
        g_inputs.clear();
    }
    for (size_t caseIdx = 0; caseIdx < g_outputs.size(); caseIdx++) {
        std::cout << "Case #" << caseIdx + 1 << ": " << g_outputs[caseIdx] << std::endl;
    }
    return 0;
}
