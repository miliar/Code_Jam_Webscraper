#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using std::cout;
using std::endl;
using std::string;

long Calculate(long N)
{
    if (N == 0)
        return 0;

    long result = 0;
    std::vector<char> digits;
    long i = 1;

    while(true)
    {
        result = N * i;
        i++;
        string str = std::to_string(result);

        for (size_t i = 0; i < str.length(); i++)
        {
            char tc = str[i];
            if (std::find(digits.begin(), digits.end(), tc) == digits.end())
            {
                digits.push_back(tc);
                cout << tc << endl;
            }
        }
        
        if(digits.size() > 9)
        {
            break;
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
        int N = 0;
        string result = "INSOMNIA";
        
        std::getline(input, line);
        ss.clear();
        ss.str(line);
        ss >> N;

        long lastNum = Calculate(N);

        if(lastNum > 0)
        {
            result = std::to_string(lastNum);
        }

        output << "Case #" << (i + 1) << ": " << result << endl;
    }

    input.close();
    output.close();

    cout << "Done!" << endl;

    return 0;
}
