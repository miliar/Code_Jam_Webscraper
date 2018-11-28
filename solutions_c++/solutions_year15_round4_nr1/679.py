#include <bits/stdc++.h> //includes everything.
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
using namespace std;

map<int,int> h;
vector<int> v;
int N,x;
int ind = 0;
int T = 0;
string s[1010];
int nrc[1010];
int nrl[1010],M;
int main(){
    freopen("cj.in","r",stdin);
    freopen("cj2.out","w",stdout);
    scanf("%d\n",&T);
    while(T--){
        ++ind;
        scanf("%d%d\n",&N,&M);
        for(int i=0;i<N;++i){
            cin>>s[i];
        }

        for(int i=0;i<=1000;++i){
            nrl[i]=nrc[i]=0;
        }
        for(int i=0;i<N;++i){
            for(int j=0;j<M;++j){
                if(s[i][j]!='.'){
                    ++nrc[i];
                    ++nrl[j];
                }
            }
        }
        int ok = 0;
        for(int i=0;i<N;++i){
            for(int j=0;j<M;++j){
                if(s[i][j]!='.')
                if(nrc[i] == 1 && nrl[j] == 1){
                    ok=1;
                }
            }
        }
        //printf("%d",ok);
        if(ok){
            printf("Case #%d: IMPOSSIBLE\n",ind);
            continue;
        }
        ok=0;
        for(int i=0;i<N;++i){
            for(int j=0;j<M;++j){
                if(s[i][j]=='<'){
                    ++ok;break;
                }
                if(s[i][j]!='.')
                    break;
            }
        }
        for(int i=0;i<N;++i){
            for(int j=M-1;j>=0;--j){
                if(s[i][j]=='>'){
                    ++ok;break;
                }
                if(s[i][j]!='.')
                    break;
            }
        }
        for(int i=0;i<M;++i){
            for(int j=0;j<N;++j){
                if(s[j][i]=='^'){
                    ++ok;break;
                }
                if(s[j][i]!='.')
                    break;
            }
        }
        for(int i=0;i<M;++i){
            for(int j=N-1;j>=0;--j){
                if(s[j][i]=='v'){
                    ++ok;break;
                }
                if(s[j][i]!='.')
                    break;
            }
        }
        printf("Case #%d: %d\n",ind,ok);

    }
    cout<<endl;


}
