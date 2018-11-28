#include <iostream>
#include <vector>
#include <list>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <fstream>
#include <sstream>

using namespace std;

int main()
{
    int N;
    cin >> N;
    char data[100];
    int caseNumber = 0;
    while (N--)
    {
        cin >> data;
        string str(data);

        int count = 0;
        while (true)
        {
            char check = str[0];
            int i = 1;
            for (; i < str.size(); ++i) {
                if (check != str[i]) {
                    reverse(str.begin(), str.begin() + i - 1);
                    for (int j = 0; j < i; ++j) {
                        if (str[j] == '+')
                            str[j] = '-';
                        else
                            str[j] = '+';
                    }
                    ++count;
                    i = 0;
                    check = str[0];
                    continue;
                }
            }

            if (check == '-') {
                ++count;
            }
            break;
        }


        cout << "Case #" << ++caseNumber << ": " << count << endl;
    }

    return 0;
}