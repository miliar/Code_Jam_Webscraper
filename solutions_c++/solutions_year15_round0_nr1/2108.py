#include<bits/stdc++.h>
#define For(i,i1,i2) for(int i=i1;i<i2;i++)
#define ll long long
#define pii pair<int,int>
#define F first
#define S second
#define V vector<int>
#define MP make_pair
#define PB push_back
#define MAX 1000000000000
#define CLR(x) memset(x,0,sizeof(x));
using namespace std;
int main(){
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    For(x,1,t+1){
        int s,ans=0,prev=0;
        string a;
        cin>>s>>a;
        For(i,0,s+1){
            if(prev<i&&a[i]!='0'){
                ans+=i-prev;
                prev=i;
            }
                prev+=a[i]-'0';
        }
        cout<<"Case #"<<x<<": "<<ans<<endl;
    }
}

