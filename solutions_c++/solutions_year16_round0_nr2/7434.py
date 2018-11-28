#include <cassert>
#include <iostream>
#include <fstream>

int negativePancakeIndex(const std::string &stack)
{
    int n = -1;
    for (int i = 0; i < stack.length(); ++i) {
        if (stack[i] == '-') {
            n = i;
        }
    }
    
    return n;
}

int leastPositivePancakeIndex(const std::string &stack, const int index)
{
    for (int i = index; i > 0; --i) {
        if (stack[i] == '+') {
            return i;
        }
    }
    return 0;
}

int flipIndex(const std::string &stack)
{
    int n = negativePancakeIndex(stack);
    if (n < 0) {
        return n;
    }
    
    return stack[0] == '+' ? leastPositivePancakeIndex(stack, n) : n;
}

void flipPancake(std::string &stack, const int index)
{
    stack[index] = (stack[index] == '-') ? '+' : '-';
}

void flipStack(std::string &stack, const int index)
{
    if (index < 0 || index >= stack.length()) {
        return;
    }
    
    for (int low = 0, high = index; low <= high; low++, high--) {
        //swap
        char tmp = stack[low];
        stack[low] = stack[high];
        stack[high] = tmp;

        // flip
        flipPancake(stack, low);
        if (low != high) {
            // if both index are same don't flip twice
            flipPancake(stack, high);
        }
    }
}

void solve(const int c, std::string &stack)
{
    int steps = 0;
    for (int index = flipIndex(stack); index != -1; index = flipIndex(stack)) {
        steps += 1;
        flipStack(stack, index);
    }
    std::cout << "Case #" << c << ": " << steps << std::endl;
}

void unitTests()
{
    assert(negativePancakeIndex("-") == 0);
    assert(negativePancakeIndex("+") == -1);
    assert(negativePancakeIndex("-+-") == 2);
    assert(negativePancakeIndex("+-+") == 1);
    assert(negativePancakeIndex("+-") == 1);

    assert(flipIndex("-") == 0);
    assert(flipIndex("+") == -1);
    assert(flipIndex("-+-") == 2);
    assert(flipIndex("+-+") == 0);
    assert(flipIndex("+-") == 0);
    
    assert(leastPositivePancakeIndex("+--+---+++", 6) == 3);

    {
        std::string s("-");
        int i = flipIndex(s);
        flipStack(s, i);
        assert(s == "+");
    }
    
    {
        std::string s("--+-");
        int i = flipIndex(s);
        flipStack(s, i);
        assert(s == "+-++");
    }
    
    {
        std::string s("+-");
        int i = flipIndex(s);
        flipStack(s, i);
        assert(s == "--");
    }
    
    {
        std::string s("-+++-++-++");
        int i = flipIndex(s);
        flipStack(s, i);
        assert(s == "+--+---+++");
    }
    {
        std::string s("+--+---+++");
        int i = flipIndex(s);
        flipStack(s, i);
        assert(s == "-++----+++");
    }

}

int main(const int argc, const char *argv[])
{
    unitTests();
    
    if (argc < 2) {
        std::cout << "Missing filename" << std::endl;
        return 0;
    }
    
    std::ifstream fin(argv[1]);
    std::string line;
    for (int c = 0; std::getline(fin, line); ++c) {
        if (c > 0) {
            solve(c, line);
        }
    }
}

