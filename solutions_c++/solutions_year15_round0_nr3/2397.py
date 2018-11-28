#include <iostream>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

char multiple(char a, char b, bool& positive)
{
    if (a == '1') return b;
    if (b == '1') return a;
    if (a == b)
    {
        positive = !positive;
        return '1';
    }

    if (a == 'i' && b == 'j') return 'k';
    if (a == 'j' && b == 'i'){positive = !positive; return 'k';}

    if (a == 'j' && b == 'k') return 'i';
    if (a == 'k' && b == 'j'){positive = !positive; return 'i';}

    if (a == 'k' && b == 'i') return 'j';
    if (a == 'i' && b == 'k'){positive = !positive; return 'j';}
}

int main()
{
    freopen("D:\\GoogleCodeJam\\in.txt","r",stdin);
    freopen("D:\\GoogleCodeJam\\out.txt","w",stdout);

    int TestNum = 0;
    cin >> TestNum;
    for (int testCase = 0;testCase < TestNum;testCase++)
	{
	    bool positive = true;
	    char temp = '1';
        int len,rpt;
        cin >> len >> rpt;
        string s;
        cin >> s;
        bool findi = false, findj = false, findk = false;

        for (int r = 0; r < rpt; r++)
        for (int i = 0;i < len; i++)
        {
            temp = multiple(temp, s[i], positive);
            if (temp == 'i' && !findi && positive)
            {
                findi = true;
                temp = '1';
            }
            if (temp == 'j' && findi && !findj && positive)
            {
                findj = true;
                temp = '1';
            }

        }

        if (temp == 'k' && findi && findj && !findk && positive)
        {
            findk = true;
        }

        if (testCase != 0) cout << endl;
        cout << "Case #" << (testCase + 1) << ": " ;
        cout << (findi && findj && findk ? "YES" : "NO");
	}
    return 0;
}
