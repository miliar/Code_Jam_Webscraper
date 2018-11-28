#include<cstdio>
#include<iostream>
#include<cstring>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
using namespace std;
int N;
map<string,int>mp;
char ch[200010];
int o;
int X[1010],Y[1010];
int A[210][1010];
int SN[210];
int D[100010];
int main(){
    freopen("inc.in","r",stdin);
    freopen("outc.out","w",stdout);
    int T;scanf("%d",&T);int tt = 0;
    while(T--){tt++;
        o = 0;
        mp.clear();
        scanf("%d",&N);
        gets(ch);
        for(int i=0;i<N;i++){
            gets(ch);
            //printf("%s\n",ch);
            int k = strlen(ch);
            SN[i] = 0;
            string str;
            for(int j=0;j<k;j++){
                str.clear();
                while(j<k && ch[j] != ' '){
                    str += ch[j++];
                }//cout<<str<<endl;
                if(mp[str] == 0) mp[str] = ++o;
                A[i][SN[i]++] = mp[str];
            }
        }
        /*
        for(int i=0;i<N;i++){
            for(int j=0;j<SN[i];j++){
                printf("%d ",A[i][j]);
            }printf("\n");
        }
        */
        int ans = o;
        for(int n=0;n<(1<<(N-2));n++){
            for(int i=0;i<=o;i++) D[i] = 0;
            for(int i=0;i<SN[0];i++) D[A[0][i]] |= 1;
            for(int i=0;i<SN[1];i++) D[A[1][i]] |= 2;
            for(int i=0;i<N-2;i++){
                if(n&(1<<i)){
                    for(int j=0;j<SN[i+2];j++){
                        D[A[i+2][j]] |= 1;
                    }
                }else{
                    for(int j=0;j<SN[i+2];j++){
                        D[A[i+2][j]] |= 2;
                    }
                }
            }
            int s = 0;
            for(int i=1;i<=o;i++) if(D[i] == 3) s++;
            ans = min(ans,s);
        }
        printf("Case #%d: %d\n",tt,ans);
    }return 0;
}
