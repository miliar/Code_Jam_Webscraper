#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;
#define pb push_back
#define MP make_pair
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define DWN(i,h,l) for(int i=(h);i>=(l);--i)
typedef long long LL;
typedef pair<int,int> PII;

int a[4][4],b[4][4];

int main()
{
    freopen("in","r",stdin);
    freopen("out","w",stdout);
    int casnum;
    int n,m;
    cin>>casnum;
    FOR(cas,1,casnum){
        cin>>n;
        REP(i,4)
            REP(j,4)
                scanf("%d",&a[i][j]);
        cin>>m;
        REP(i,4)
            REP(j,4)
                scanf("%d",&b[i][j]);

        int ans=0;
        int temp=0;
        REP(i,4)
            REP(j,4)
                if(a[n-1][i] == b[m-1][j]){
                    ans++;
                    temp=a[n-1][i];
                }


        printf("Case #%d: ",cas);
        if(ans==1)  cout<<temp<<endl;
        else if(ans>=1) cout<<"Bad magician!"<<endl;
        else if(ans==0) cout<<"Volunteer cheated!"<<endl;
    }


    return 0;
}
