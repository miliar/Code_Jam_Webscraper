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
int arr[10000],ans[10000];
int main(){
    ios::sync_with_stdio(false);
    int t;
    cin>>t;
    For(x,1,t+1){
        int n;
        cin>>n;
        For(i,0,n){
            cin>>arr[i];
        }
        int mn=10000000,rate,tot=0,tot1=0;
        For(i,0,n-1){
            ans[i]=arr[i+1]-arr[i];
            mn=min(ans[i],mn);
            if(ans[i]<0)
                tot+=(-ans[i]);
        }
        rate=-mn;
        For(i,0,n-1){
            if(arr[i]-rate<0){
                tot1+=arr[i];
            }
            else
                tot1+=rate;
        }
        cout<<"Case #"<<x<<": "<<tot<<" "<<tot1<<endl;
    }
}
