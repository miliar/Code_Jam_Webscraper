#include <iostream>
#include <c++/fstream>
#include <c++/sstream>
#include <deque>

using namespace std;


int main() {
    ofstream ofs("output.txt");
    ifstream fs("input.txt");
    cout << "Hello, World!" << endl;

    string line;
    ostringstream outline;

    std::getline(fs, line); // consumes number.

    string emptyStr = "";
    char left;
    deque<char> lineResult;
    for (unsigned int i = 1, line_index = 0; std::getline(fs, line);
         ++i, lineResult.clear(),
         outline.str(emptyStr))
    {
        cout << line << endl;

        if(line.size() == 0) {
            cout << "WTF no cookies !";
            return -1;
        }

        left = line[0];
        lineResult.push_back(left);
        for(line_index = 1; line_index < line.size(); ++line_index) {
            if(line[line_index] >= left) {
                lineResult.push_front(line[line_index]);
                left = line[line_index];
            }
            else {
                lineResult.push_back(line[line_index]);
            }
        }

        //lineResult.push_back('\0');
        string res(lineResult.begin(), lineResult.end());

        outline << "Case #" << i << ": "
                << res
                << endl;
        outline.flush();

        cout << outline.str();
        ofs << outline.str();
    }

    fs.close();
    ofs.close();

    return 0;
}