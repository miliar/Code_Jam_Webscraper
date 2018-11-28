#include <iostream>
#include <vector>

void printStack(std::vector<bool> &stack) {
    for (bool x : stack) {
        std::cout << x;
    }
    std::cout << std::endl;
}

void removeLowPositives(std::vector<bool> &stack) {
    for (int i = stack.size() - 1; i >= 0; --i) {
        if (stack[i]) {
            stack.erase(stack.begin() + i);
        } else {
            return;
        }
    }
}

std::vector<bool> invertStack(std::vector<bool> &stack, int h) {
    std::vector<bool> newStack;
    for (int i = h; i >= 0; --i) {
        newStack.push_back(!stack[i]);
    }
    for (int i = h + 1; i < stack.size(); ++i) {
        newStack.push_back(stack[i]);
    }
    return newStack;
}

std::vector<bool> invertStack(std::vector<bool> &stack) {
    return invertStack(stack, stack.size() - 1);
}

int main() {
    int T;
    std::cin >> T;
    int C = 1;
    while (C <= T) {
        std::string S;
        std::cin >> S;
        std::vector<bool> stack;
        for (char& c : S) {
            stack.push_back(c == '+');
        }
        int operations = 0;
        while (!stack.empty()) {
//            printStack(stack);
            removeLowPositives(stack);
            if (stack.empty()) {
                break;
            }
            // Lowest pancake on stack is negative

            // Invert stack if highst pancake on stack is negative
            if (!stack[0]) {
                stack = invertStack(stack);
                operations++;
                continue;
            }
            // Highest pancake on stack is positive

            for (int i = 0; i < stack.size(); ++i) {
                if (!stack[i]) {
                    // Invert all positive pancakes on top of this one
                    stack = invertStack(stack, i - 1);
                    operations++;
                    break;
                }
            }
        }
        std::cout << "Case #" << C++ << ": " << operations << std::endl;
    }
    return 0;
}
