#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    freopen("D:\\GoogleCodeJam\\in.txt","r",stdin);
    freopen("D:\\GoogleCodeJam\\out.txt","w",stdout);

    int TestNum = 0;
    cin >> TestNum;
    for (int testCase = 0;testCase < TestNum;testCase++)
	{
	    int maxLevel = 0;
	    cin >> maxLevel;
	    string s = "";
	    cin >> s;
	    int prevSum = s[0] - '0';
	    int fdNum = 0;
	    for (int i = 1; i <= maxLevel; i++)
        {
            if (s[i] != '0')
            {
                if (prevSum < i)
                {
                    fdNum += i - prevSum;
                    prevSum = i;
                }
                prevSum += s[i] - '0';
            }
        }
        if (testCase != 0) cout << endl;
        cout << "Case #" << (testCase + 1) << ": " << fdNum;
	}
    return 0;
}
