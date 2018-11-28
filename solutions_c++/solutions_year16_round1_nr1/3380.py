#include <iostream>
#include <fstream>
#include <cstring>
#include <queue>
#include <list>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream cout("output.txt");

    int T;
    fin >> T;

    char str[1005];
    fin.getline(str, 500);

    for (int t = 0; t < T; t++)
    {
        fin.getline(str, 1005);

        //char result[1000];
        list<char> result;

        for (auto i = 0; i < strlen(str); i++)
        {
            if (result.size() == 0 || result.back() <= str[i])
                result.push_back(str[i]);
            else
                result.push_front(str[i]);
        }

        cout << "Case #" << (t+1) <<": ";
        int size = result.size();
        for (auto i = 0; i < size; i++)
        {
            cout << result.back();
            result.pop_back();
        }
        //cout << result.back();

        cout << endl;
    }

    return 0;
}