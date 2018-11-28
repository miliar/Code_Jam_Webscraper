#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;
int N,R,P,S;
int A[3],B[3];
char ch[3] = {'R','S','P'};
string STR[3] = {"RS","PS","PR"};
void pdfs(int n,int k) {
    if(n == 0) {
        A[k]++;
        A[(k+1)%3]++;
        return ;
    }
    pdfs(n-1,k);
    pdfs(n-1,(k+1)%3);
}
string dfs(int n,int k) {
    if(n == 0) {
        string str = STR[k];
        return str;
    }
    string str1 = dfs(n-1,k);
    string str2 = dfs(n-1,(k+1)%3);
    string str;
    if(str1 < str2) str = str1 + str2;
    else str = str2 + str1;
    return str;
}
int main(){
    freopen("ail.in","r",stdin);
    freopen("ao.out","w",stdout);
    int T;scanf("%d",&T);
    for(int tt=1;tt<=T;tt++){
        scanf("%d%d%d%d",&N,&B[0],&B[2],&B[1]);
        string ans = "";
        //cout<<ans.size()<<endl;
        for(int i=0;i<3;i++) {
            memset(A,0,sizeof(A));
            pdfs(N-1,i);
            bool jud = true;
            for(int j=0;j<3;j++) {
                    //cout<<A[j];
                if(A[j] != B[j]) jud = false;
            }//cout<<endl;
            if(jud) {
                //cout<<"AA"<<endl;
                string str = dfs(N-1,i);
                if(ans.size() == 0 || ans > str) ans = str;
            }
        }
        cout<<"Case #"<<tt<<": ";
        if(ans.size() > 0) {
            cout<<ans<<endl;
        }
        else cout<<"IMPOSSIBLE" << endl;
    }
    return 0;
}
