#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<algorithm>
#include<cmath>
#include<climits>
#include<queue>
#include<set>
#include<iomanip>

#define VI vector<int>
#define PII pair<int,int>
#define mp make_pair
#define rep(i,a,b) for(i=(a); i<(b); i++)
#define repI(i,a,b) for(i=(a); i<=(b); i++)

using namespace std;
typedef unsigned long long int ulli;
typedef long long int lli;

double c,f,x,val,duration;

double get_val(int farmCnt)
{
    int i;
    double tmp = 0;
    for (i=0; i<farmCnt; i++)
    {
        tmp += ( c/(2+(i*f)) );
    }
    tmp += ( x/(2+farmCnt*f) );
    return tmp;
}

main()
{
    int T;
    cin >> T;
    int tot = T;
    int farmCnt;
    std::cout << std::fixed;
    std::cout << setprecision(7);
    while(T--)
    {
        cin >> c >> f >> x;
        duration = x/2;
        val = (x/c) - (2/f);
        farmCnt = floor(val);
        if(farmCnt>0)
            cout << "Case #" << tot-T << ": " << get_val(farmCnt) << endl;
        else 
            cout << "Case #" << tot-T << ": " << duration << endl;
    }
}

