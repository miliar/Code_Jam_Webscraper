#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using std::cout;
using std::endl;
using std::string;


string Solve(const string& str)
{
    string result = str.substr(0, 1);

    for (size_t i = 1; i < str.length(); i++)
    {
        string newChar = str.substr(i, 1);

        if(str[i] >= result[0])
        {
            result = newChar.append(result);
        }
        else
        {
            result.append(newChar);
        }
    }

    return result;
}


int main()
{
    cout << "Working..." << endl;

    std::ifstream input("input.txt" );
    std::ofstream output("output.txt");
    string line;
    std::getline(input, line);
    std::istringstream ss(line);

    int caseCount = 0;
    ss >> caseCount;

    for (int i = 0; i < caseCount; i++)
    {
        std::getline(input, line);
        string result = Solve(line);

        output << "Case #" << (i + 1) << ": " << result << endl;
    }

    input.close();
    output.close();

    cout << "Done!" << endl;

    return 0;
}
