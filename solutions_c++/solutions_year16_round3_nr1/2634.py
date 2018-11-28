#include<bits/stdc++.h>
using namespace std;

int main()
{
   // freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int t;
    cin>>t;
    int n,c,x,mx; char ch;
    int arr[29];
    long long s;
    for(int k=1;k<=t;k++)
    {
    mx=-1;
        cin>>n;
        c=0; s=0;
        for(int i=0;i<n;i++) {cin>>arr[i]; if(arr[i]>mx) mx=arr[i]; s+=arr[i];}
        cout<<"Case #"<<k<<": ";
        bool f=0;
        if(s%2==1) f=1;
        for(int j=mx;j>=1;j--){
        for(int i=0;i<n;i++)
        {
        if(arr[i]==j) {ch='A'+i; cout<<ch; c++;arr[i]--;}
        if(c==1&&f) {f=0,c=0;cout<<" "; }
        if(c==2){cout<<" "; c=0;}
        }
        }
        cout<<endl;
  }
    return 0;
}
