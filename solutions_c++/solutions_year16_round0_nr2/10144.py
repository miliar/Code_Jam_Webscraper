#include <iostream>
#include <fstream>

using namespace std;

__int128 convert(string strstack) {
    __int128 stk = 0;
    int size = strstack.length();
    for (int i = 0; i < size; i++) {
        stk = stk | ((strstack.at(i) == '+' ? 1 : 0) << (size - i - 1));
    }
    return stk;
}

int calculate(__int128 stk, int target, int bottom, int size) {
    if (bottom == size)
        return 0;
    int top = (stk >> (bottom)) & 1;
    if (size == 1) {
        return (top == target) ? 0 : 1;
    } else {
        if (top == target) {
            return calculate(stk, target, bottom + 1, size);
        } else
            return 1 + calculate(stk, !target, bottom + 1, size);
    }
}

int main(int argc, char **argv) {
    ifstream ifstreamIn;
    ofstream ofstreamOut;
    ofstreamOut.open("output.txt");
    ifstreamIn.open("input.txt");

    int t, s;
    string strstack;
    __int128 stack;
    ifstreamIn >> t;
    int size = t;
    while (t-- > 0) {
        stack = 0;
        ifstreamIn >> strstack;
        s = strstack.length();
        stack = convert(strstack);

        fout << "Case #" << size - t  << ": " << calculate(stack, 1, 0, s) << endl;
        cout << "Case #" << size - t  << ": " << calculate(stack, 1, 0, s) << endl;

    }
    ifstreamIn.close();
    ofstreamOut.close();
    return 0;
}
