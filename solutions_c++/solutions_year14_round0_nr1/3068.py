#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<iostream>
#include<map>
#define REP(i,n) for(int i=0;i<n;i++)
typedef long long ll;

using namespace std;
int ans1[5][5];
int ans2[5][5];
int main(){
#ifdef LOCALL
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
#endif
    int t,a,b;
    cin>>t;
    for(int kase = 1;kase <= t;kase ++){
        cin>>a;
        REP(i,4) REP(j,4) cin>>ans1[i][j];
        cin>>b;
        REP(i,4) REP(j,4) cin>>ans2[i][j];
//        cout<<a<<endl;
//        REP(i,4) {REP(j,4) cout<<ans1[i][j]<<"\t"; cout<<"\n";};
//        cout<<"\n"<<b<<"\n";
//        REP(i,4) {REP(j,4) cout<<ans2[i][j]<<"\t"; cout<<"\n";};


        int ret = -1;
        for(int i = 0;i<4;i++){
            for(int j = 0;j<4;j++){
                if(ans1[a-1][i] == ans2[b-1][j]){
                    //cout<<ans1[a-1][i]<<endl;
                    if(ret == -1)
                        ret = ans1[a-1][i];
                    else if(ret > 0) ret = -2;
                }
            }
        }

        cout<<"Case #"<<kase<<": ";
        if(ret > 0)cout<<ret<<endl;
        else if (ret == -1)cout<<"Volunteer cheated!"<<endl;
        else if(ret == -2)cout<<"Bad magician!\n";
    }
    return 0;
}

