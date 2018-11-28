//                                                  به نام خداوند بخشنده ی مهربان
#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <iomanip>
#include <fstream>
#include <complex>
#include <vector>
#include <string>
#include <cstdio>
#include <queue>
#include <deque>
#include <cmath>
#include <map>
#include <set>

# define xx first
# define yy second
# define pb push_back
# define pp pop_back
# define eps 1e-9
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef vector<int> vint;
int a[3][5][5];
int w[2][20],ans1,ans2;
vint v;

bool check_cheat(){
    bool mark=true;
    for(int i=1 ; i<=4 ; i++){
        int temp=a[0][ans1][i];
        for(int j=1 ; j<=4 ; j++){
            if(a[1][ans2][j]==temp)
                mark=false;
        }
    }
    return mark;
}
bool several_soulution(){
    for(int i=1 ; i<=4 ; i++){
        int temp=a[0][ans1][i];
        for(int j=1 ; j<=4 ; j++){
            if(a[1][ans2][j]==temp)
                v.pb(temp);
        }
    }
    if((int)v.size()!=1)
        return true;
    return false;
}
int main(){
    ios_base::sync_with_stdio(false);
    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("ans.out","w",stdout);
    int t;cin>>t;
    for(int T=1 ; T<=t ; T++){
        v.clear();
        cin>>ans1;
        for(int i=1 ; i<=4 ; i++)
            for(int j=1 ; j<=4 ; j++){
                cin>>a[0][i][j];
                w[0][a[0][i][j]]=j;
            }
        cin>>ans2;
        for(int i=1 ; i<=4 ; i++)
            for(int j=1 ; j<=4 ; j++){
                cin>>a[1][i][j];
                w[1][a[1][i][j]]=j;
            }
         cout<<"Case #"<<T<<": ";
        if(check_cheat())
            cout<<"Volunteer cheated!\n";
        else if(several_soulution())
            cout<<"Bad magician!\n";
        else
            cout<<v.back()<<'\n';
    }
    return 0;
}
