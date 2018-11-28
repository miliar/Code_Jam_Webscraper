#include <iostream>
#include <fstream>
#include <algorithm>
#include <deque>
#include <sstream>
using namespace std;

const string INPUT_FILE = "in.txt";
const string OUTPUT_FILE = "out.txt";

int solveCase(ifstream & input) {
    int n, capacity;
    input >> n >> capacity;
    deque<int> sizes;
    for (int i = 0; i < n; i++) {
        int s;
        input >> s;
        sizes.push_back(s);
    }
    sort(sizes.begin(), sizes.end());

    int answer = 0;
    int a = 0;
    int b = n - 1;
    while (b > a) {
        answer++;
        if (sizes[a] + sizes[b] <= capacity) {
            a++;
        }
        b--;
    }
    if (a == b)
        answer++;
    return answer;
}

void solveAllCases(ifstream & input, ofstream & output) {
    int cases;
    stringstream("2") >> cases;
    input >> cases;
    cout << "Testcases to run: " << cases << endl;
    for (int i = 1; i <= cases; i++) {
        output << "Case #" << i << ": ";
        output << solveCase(input);
        output << endl;
    }
}

int main()
{
    ifstream input(INPUT_FILE.c_str(), ios::in);
    ofstream output(OUTPUT_FILE.c_str(), ios::out);
    solveAllCases(input, output);
    input.close();
    output.close();
    return 0;
}
