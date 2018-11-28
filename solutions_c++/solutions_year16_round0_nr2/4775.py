#include <vector>
#include <iostream>
#include <string>

using namespace std;

int main(void)
{
    int t = 0;
    cin >> t;

    for (int i=0; i < t; i++)
    {
        string s;
        cin >> s;
        vector<int> pancakes;
        
        for (int j = 0; j < s.length(); j++)
        {
            s[j] == '+' ? pancakes.push_back(1) : pancakes.push_back(0);
        }
        int flips = 0;
        while (pancakes.size() > 0)
        {
            if (pancakes.back() == 0)
            {
                for (int j=0; j < pancakes.size(); j++)
                    pancakes[j] = pancakes[j] == 0 ? 1 : 0;
                flips += 1;
            }   
            pancakes.pop_back();
        }
        cout << "Case #" << i+1 <<": "<< flips << endl;
    }
}
