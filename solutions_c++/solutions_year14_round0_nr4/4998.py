#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
#include <string.h>
#include <limits>

#define SZ(c) c.size()
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define SORT(a) sort(a.begin(),a.end())
#define tests int test; scanf("%d",&test); while(test--)
#define dbg(n) cout<<#n<<" = "<<n<<endl;

using namespace std;

int strToInt(string str) {
    int ans;
    stringstream s;
    s<<str;
    s>>ans;
    return ans;
}
string intToStr(int n) {
    string str;
    stringstream s;
    s<<n;
    s>>str;
    return str;
}
int MAX(int a,int b) {
    if(a >b) return a;
    return b;
}
int MIN(int a,int b) {
    if(a <b) return a;
    return b;
}
int ABS(int a) {
    if(a >0) return a;
    return -a;
}

int point(double here, double there) {
    if( (here - there) > std::numeric_limits<double>::epsilon())
        return 1;
    return 0;
}

int main() {
    freopen("D-small-attempt1.txt", "r", stdin);
    freopen("writeDDD.txt", "w", stdout);
    int test;
    scanf("%d\n",&test);
    int number;
    double first[14], second[14];
    for(int current=1; current <= test; current++) {
        scanf("%d", &number);
        for(int i=0; i<number; i++) {
            cin>> first[i];
        }
        for(int i=0; i<number; i++) {
            cin>> second[i];
        }

        sort(first, first+number);
        sort(second, second+number);

//        for(int i=0; i<number; i++)
//            cout<<first[i] <<" ";
//        cout<<endl;
//
//        for(int i=0; i<number; i++)
//            cout<<second[i] <<" ";
//        cout<<endl;

        int war=0, deciet =0;
        int one=0, two=0, countWar=0; //index
        int visitOne[14], visitTwo[14];

        {
            for(int i=0; i<number; i++)
                visitOne[i] = visitTwo[i] =0;

            double here, there;
            countWar =0;
            for(int i=0; i<number; i++) {
                here = first[i];
                int flag =0;
                for(int j=0; j<number; j++) {
                    if(!visitTwo[j] && ((second[j] - here) > (std::numeric_limits<double>::epsilon())) ) {
                        visitTwo[j] =1;
                        there = second[j];
                        flag =1;
                        break;
                    }
                }
                if(flag)
                    countWar += point(here, there);
                else
                    countWar++;
            }

        }

        {
            for(int i=0; i< number; i++)
                visitOne[i] = visitTwo[i] =0;

            double here, there;

            for(int i=0 ; i<number; i++)
            {
                here = first[i];
                int flag =0;
                for(int j=0; j<number; j++)
                {
                    if(!visitTwo[j] && ((here - second[j]) > (std::numeric_limits<double>::epsilon()) )  )
                    {
                        visitTwo[j]=1;
                        deciet++;
                        flag =1;
                        break;
                    }

                }

                if(!flag)
                {
                    for(int j = (number-1); j>=0; j--)
                    {
                        if( !visitTwo[j])
                        {
                            visitTwo[j] =1;
                            break;
                        }
                    }
                }
            }

        }

        printf("Case #%d: %d %d\n",current, deciet, countWar);

    }
    return 0;
}

