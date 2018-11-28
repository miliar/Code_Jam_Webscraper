#include <iostream>
#include <algorithm>
#include <cstdio>
#include <fstream>
#include <queue>
#include <math.h>
#include <limits.h>
#include <cstdlib>
#include <string.h>
#include <vector>
#include <iomanip>
#include <map>
#include <stack>
using namespace std;
//mehulagarwal
#define ll         long long
#define S(x)       scanf("%d", &x)
#define Sl(x)      scanf("%lld", &x)
#define Sd(x)      scanf("%lf", &x)
#define P(x)       printf("%d\n", x)
#define Pl(x)      printf("%lld\n", x)
#define Pd(x)      printf("%lf\n", x)
#define Pblank()   printf(" ")
#define mem(x,y)   memset(x,y,sizeof(x))
#define F(x,y,z,i) for (x = y; x < z; x = x + i)
#define mod 1000000007
using namespace std;

int main()
{
    int i,y,t;
    vector<int>vec;
    map<char,int>m;
    string str;

    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin >> t;
    for (int cid = 1; cid <= t; cid++) {
        cin >> str;
        for (i = 0; i < str.length(); i++) {
            m[str[i]]++;
        }

        if (m['Z'] != 0) { ///ZERO
            y = m['Z'];
            for (i = 0; i < y; i++) {
                vec.push_back(0);
                m['E']--;
                m['R']--;
                m['Z']--;
                m['O']--;
            }
        }
        if (m['W'] != 0) { ///TWO
            y = m['W'];
            for (i = 0; i < y ;i++) {
                vec.push_back(2);
                m['T']--;
                m['W']--;
                m['O']--;
            }
        }
        if (m['U'] != 0) { ///FOUR
            y = m['U'];
            for (i = 0; i < y ;i++) {
                vec.push_back(4);
                m['F']--;
                m['O']--;
                m['U']--;
                m['R']--;
            }
        }
        if (m['X'] != 0) { ///SIX
            y = m['X'];
            for (i = 0; i < y ;i++) {
                vec.push_back(6);
                m['S']--;
                m['I']--;
                m['X']--;
            }
        }
        if (m['U'] != 0) { ///FOUR
            y = m['U'];
            for (i = 0; i < y ;i++) {
                vec.push_back(4);
                m['F']--;
                m['O']--;
                m['U']--;
                m['R']--;
            }
        }
        if (m['S'] != 0) { ///SEVEN
            y = m['S'];
            for (i = 0; i < y ;i++) {
                vec.push_back(7);
                m['S']--;
                m['E']--;
                m['V']--;
                m['E']--;
                m['N']--;
            }
        }
        if (m['V'] != 0) { ///FIVE
            y = m['V'];
            for (i = 0; i < y ;i++) {
                vec.push_back(5);
                m['F']--;
                m['I']--;
                m['V']--;
                m['E']--;
            }
        }
        if (m['G'] != 0) { ///EIGHT
            y = m['G'];
            for (i = 0; i < y ;i++) {
                vec.push_back(8);
                m['E']--;
                m['I']--;
                m['G']--;
                m['H']--;
                m['T']--;
            }
        }
        if (m['O'] != 0) { ///ONE
            y = m['O'];
            for (i = 0; i < y ;i++) {
                vec.push_back(1);
                m['O']--;
                m['N']--;
                m['E']--;
            }
        }
        if (m['H'] != 0) { ///THREE
            y = m['H'];
            for (i = 0; i < y ;i++) {
                vec.push_back(3);
                m['T']--;
                m['H']--;
                m['R']--;
                m['E']--;
                m['E']--;
            }
        }
        if (m['I'] != 0) { ///NINE
            y = m['I'];
            for (i = 0; i < y ;i++) {
                vec.push_back(9);
                m['N']--;
                m['I']--;
                m['N']--;
                m['E']--;
            }
        }
        sort(vec.begin(),vec.end());

        cout << "Case #" << cid << ": ";
        for (i = 0; i < vec.size(); i++) {
            cout << vec[i];
        } cout << endl;
        vec.clear();
        m.clear();
    }

    return 0;
}
