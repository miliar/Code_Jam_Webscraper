// c++ 11

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int ispresent(string s, char a)
{
    for (unsigned int i = 0; i < s.length(); i += 1)
    {
        if(s[i] == a) return i;
    }
    return -1;
}


int main (int argc, char const* argv[])
{
    int test;
    cin >> test;
    for (int t = 0; t < test; t += 1)
    {
        string s;
        cin >> s;
        cout << "Case #" << t+1 << ": ";
        string nos[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
        int on[10] = {0, 6, 7, 8, 2, 3, 4, 5, 1, 9};
	    int o = 0;
	    string ans = "";
	    while(o < 10)
        {
            int i = on[o];
            string d = "";
            int j = 0;
	    	for (j = 0; j < nos[i].length(); j += 1)
	    	{
                int p = ispresent(s, nos[i][j]);
	    	    if(p != -1)
                {
                    d += nos[i][j];
                    s = s.substr(0, p) + s.substr(p+1);
                }
                else break;
	    	}
            if(j == nos[i].length())
            {
                ans += std::to_string(i);
            }
            else
            {
                o++;
                s+=d;
            }
	    }
	    sort(ans.begin(), ans.end());
        cout << ans << endl;
    }
    return 0;
}
