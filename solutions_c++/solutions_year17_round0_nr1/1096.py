#include <bits/stdc++.h>
using namespace std;
const int maxn = 23333;
char t[maxn];
int st[maxn],sum[maxn];
int n;
int T;
int main(){
    cin>>T;
    freopen("out.txt","w",stdout);
    int _case = 0;
    while(T--){
        cin>>t;
        cin>>n;
        int len = strlen(t);
        for(int i=0;i<len;i++){
            if(t[i]=='+') st[i]=1;
            else st[i]=0;
        }
        int ans = 0;
        memset(sum,0,sizeof(sum));
        for(int i=0;i+n<=len;i++){
            if(st[i]==0){
                ans++;
                for(int j=i;j<i+n;j++){
                    st[j]^=1;
                }
            }
            //for(int j=0;j<len;j++) cout<<st[j];cout<<endl;
        }
        int flag = 0;
        for(int i=0;i<len;i++){
            if(!st[i]){
                cout<<"Case #"<<++_case<<": "<<"IMPOSSIBLE"<<endl;
                flag = 1;
                break;
            }
        }
        if(!flag)
        cout<<"Case #"<<++_case<<": "<<ans<<endl;
    }
    return 0;
}
