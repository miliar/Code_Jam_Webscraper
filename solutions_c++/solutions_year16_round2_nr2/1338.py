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

int main()
{
    int t;
    int i,j;
    string str1,str2,fstr1,fstr2;
    string tstr,tstr1;
    int r,temp;
    int minn,mini,minj;

    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);

    cin >> t;
    for (int cid = 1; cid <= t; cid++) {
        cin >> str1 >> str2;

        minn = INT_MAX;
        mini = 1000;
        minj = 1000;
        int ml;

        if (str1.length() == 1) {
            ml = 10;
        } else if (str1.length() == 2) {
            ml = 100;
        } else {
            ml = 1000;
        }

        for (i = 0; i < ml; i++) {
            tstr = "";
            int flag = 0;
            temp = i;
            while (temp > 0) {
                r = temp % 10;
                temp = temp / 10;
                tstr.push_back(r+'0');
            }
            if (i == 0)
                tstr.push_back('0');
            if (i < 100 && ml == 1000) {
                tstr = tstr + '0';
            }
            if (i < 10 && ml > 10) {
                tstr = tstr + '0';
            }
            reverse(tstr.begin(),tstr.end());

            for (int i1 = 0; i1 < tstr.length(); i1++) {
                if (str1[i1] != '?' && str1[i1] != tstr[i1]) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 1) {
                continue;
            }
            for (j = 0; j < ml; j++) {
                ///maintain min diff and the numbers
                tstr1 = "";
                temp = j;
                flag = 0;
                while (temp > 0) {
                    r = temp % 10;
                    temp = temp / 10;
                    tstr1.push_back(r+'0');
                }
                if (j == 0)
                    tstr1.push_back('0');
                if (j < 100 && ml == 1000) {
                    tstr1 = tstr1 + '0';
                }
                if (j < 10 && ml > 10) {
                    tstr1 = tstr1 + '0';
                }
                reverse(tstr1.begin(),tstr1.end());
                for (int i1 = 0; i1 < tstr1.length(); i1++) {
                    if (str2[i1] != '?' && str2[i1] != tstr1[i1]) {
                        flag = 1;
                        break;
                    }
                }
                if (flag == 0) {
                    if (abs(i-j) < minn) {
                        minn = abs(i-j);
                        mini = i;
                        minj = j;
                    } else if (abs(i-j) == minn) {
                        if (i < mini) {
                            mini = i;
                            minj = j;
                        } else if (i == mini) {
                            if (j < minj) {
                                minj = j;
                            }
                        }
                    }
                }
            }
        }

        cout << "Case #" << cid << ": ";
        if (str1.length() == 3 && mini < 100) {
            if (mini < 10) {
                cout << "0";
            }
            cout << "0";
        }
        if (str1.length() == 2 && mini < 10) {
            cout << "0";
        }
        cout << mini << " ";
        if (str1.length() == 3 && minj < 100) {
            if (minj < 10) {
                cout << "0";
            }
            cout << "0";
        }
        if (str1.length() == 2 && minj < 10) {
            cout << "0";
        }
        cout << minj << endl;
    }

    return 0;
}
