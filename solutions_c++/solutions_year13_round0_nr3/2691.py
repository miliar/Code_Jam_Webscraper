#include <iostream>
#include <cstdio>
#include <cstring>
#include <stdlib.h>
#include <set>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;

int T;
int A, B;

set<int> dict;
set<int> pali;

bool isPalindrome(int i)
{
    stringstream sstream;
    sstream << i;
    string s = sstream.str();
    string t = s;
    reverse(t.begin(), t.end());

    return s == t;
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);

    cin >> T;

    for (int cas = 1; cas <= T; cas++)
    {
        dict.erase(dict.begin(), dict.end());
        pali.erase(pali.begin(), pali.end());

        cin >> A >> B;

        int maxxy = sqrt((double)B);

        int ctr = 0;

        if (A == 1)
        {
            ctr = 1;
            A++;
        }

        for (int i = A; i <= B; i++)
        {
            if (dict.find(i) != dict.end() || pali.find(i) != pali.end())
            {
                continue;
            }
            dict.insert(i);
            if (isPalindrome(i))
            {
                //cout << i << endl;
                pali.insert(i);
                int root = sqrt((double)i);
                if (root * root == i && isPalindrome(root))
                {
                    ctr++;
                    //cout << "HINOW" << i << endl;
                }
            }else
            {
                continue;
            }
            int cur = i;
            bool good = true;
            while (good && cur <= maxxy)
            {
                cur *= cur;
                dict.insert(cur);
                if (pali.find(cur) != pali.end() || isPalindrome(cur))
                {
                    pali.insert(cur);
                    //cout << "HI" << cur << endl;
                    //cout << cur << endl;
                    ctr++;
                }else
                {
                    good = false;
                }
            }
        }
        printf("Case #%d: %d\n", cas, ctr);
        //cout << ctr << endl;
    }


    return 0;
}
