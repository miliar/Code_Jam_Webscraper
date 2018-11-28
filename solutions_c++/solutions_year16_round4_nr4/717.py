#include<bits/stdc++.h>
using namespace std;
string a[5],b[5];
int ans,n;
void dfs(int ii,int mask){
    if(ii==n){
        ans=max(ans,n-__builtin_popcount(mask));
        return;
    }
    bool f=1;
    for(int i=0;i<n;i++){
        if(!(mask&(1<<i))){
            if(b[ii][i]=='1'){
                dfs(ii+1,mask|(1<<i));
                f=0;
            }
        }
    }
    if(f)dfs(ii+1,mask);
    return;
}
int main()
{
//    ios_base::sync_with_stdio(0);
//    cin.tie(nullptr);
    freopen("in4","r",stdin);
    freopen("out4","w",stdout);
    int t;
    cin>>t;
    for(int z=1; z<=t; z++)
    {
        cin>>n;
        for(int i=0; i<n; i++)
        {
            cin>>a[i];
            b[i]=a[i];
        }
        int mn=12345678;
        for(int i=0;i<(1<<(n*n));i++){
            for(int j=0;j<n;j++)b[j]=a[j];
            int cnt=0;
            for(int j=0;j<n*n;j++){
                if(i&(1<<j)){
                    if(b[j/n][j%n]!='1')cnt++;
                    b[j/n][j%n]='1';
                }
            }
            ans=0;
            sort(b,b+n);
            do{
                dfs(0,0);
            }while(next_permutation(b,b+n));
            if(ans==0)mn=min(mn,cnt);
        }
        cout<<"Case #"<<z<<": "<<mn<<"\n";
    }
    return 0;
}
