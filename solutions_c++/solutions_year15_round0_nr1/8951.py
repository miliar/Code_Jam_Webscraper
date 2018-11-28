
/**
 * The standing ovation program (Google code jam 2015).
 * Author: Rubén Castrillón.
 * Using g++ (gcc) with std=c++11
 */

#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using std::cout;
using std::cin;
using std::string;
using std::vector;
using std::ifstream;
using std::ofstream;
using std::endl;

class Line {
public:
    Line(int, string);
    int solve(); // Solves this line and returns the amount of people needed.
private:
    int s_max;
    string s_values;
};

int main() {

    ifstream in {"Input.txt"};
    ofstream out {"Output.txt"};
    if (!in || !out) throw "IO error with the files.";

    int T {0};
    in >> T;
    if (T < 1 || T > 100) throw "T is not valid.";

    vector<Line> lines {}; // Used to store the lines that we will parse.
    for (int i = 1; i <= T; i++) {
        int currentInt {0};
        string currentString {NULL};
        in >> currentInt >> currentString;
        lines.push_back(Line(currentInt, currentString));
    }

    // Finally going line per line printing the result.
    for (int i = 0; i < T; i++) {
        int solution = lines[i].solve();
        out << "Case #" << i + 1 << ": " << solution << endl;
    }
	return 0;
}

Line::Line(int i, string s):
    s_max {i},
    s_values {s}
{
}

int Line::solve() {
    int solution {0};
    int people {0}; // Stores the amount of people standing.
    for (int i = 0; i <= s_max; i++) {
        while (i > people) {
            people++;
            solution++;
        }
        people += (s_values[i] - '0');
    }
    return solution;
}
