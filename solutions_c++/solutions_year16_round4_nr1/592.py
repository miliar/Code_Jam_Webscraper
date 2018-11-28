#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
using namespace std;

int T,N,P,R,S;

string ans[13][3];
int pnum[13][3],rnum[13][3],snum[13][3];

void st()
{
    ans[0][0] = 'P';
    ans[0][1] = 'R';
    ans[0][2] = 'S';
    for(int i=0;i<12;i++) {
        ans[i+1][0] = ans[i][0] + ans[i][1];
        ans[i+1][1] = ans[i][0] + ans[i][2];
        ans[i+1][2] = ans[i][1] + ans[i][2];
    }
    for(int i=0;i<=12;i++) {
        for(int j=0;j<3;j++) {
            for(int k=0;k<ans[i][j].length();k++) {
                if(ans[i][j][k] == 'P') pnum[i][j]++;
                if(ans[i][j][k] == 'R') rnum[i][j]++;
                if(ans[i][j][k] == 'S') snum[i][j]++;
            }
        }
    }

}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    st();
    cin>>T;
    for(int ca=1;ca<=T;ca++) {
        cin>>N>>R>>P>>S;
        cout<<"Case #"<<ca<<": ";
        bool flag = false;
        for(int i=0;i<3;i++) {
            if((R == rnum[N][i]) && (P == pnum[N][i]) && (S == snum[N][i])) {
                flag = true;
                cout<<ans[N][i]<<endl;
                break;
            }
        }
        if(!flag) cout<<"IMPOSSIBLE"<<endl;
    }
    return 0;
}
