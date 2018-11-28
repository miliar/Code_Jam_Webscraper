#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <limits.h>
#define fir(i,n,m) for(int i=n;i<m;i++)
#define fdr(i,n,m) for(int i=n;i>=m;i--)
#define pb push_back
#define vi vector<int>
#define vs vector<string>
#define sz(v) (int)v.size()
#define all(v) v.begin(),v.end()
using namespace std;

int main(){
    int t, smax;
    string run;
    scanf("%d", &t);
    int nCases=1;
    while(t--){
        cin>>smax>>run;
        int total=run[0]-'0', diff=0;
        for(int i=1;i<=smax;i++){
            int num = run[i]-'0';
            if(num==0){
                continue;
            }
            if(total<i){
                diff+=i-total;
                total+=diff;
            }
            total += num;
        }
        printf("Case #%d: %d\n",nCases, diff);
        nCases++;
    }
    return 0;
}
