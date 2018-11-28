#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    cin>>t;
    for(int f=1;f<=t;f++){
        int mx;
        string s;
        cin>>mx>>s;
        int arr[mx+1];
        for(int i=0;i<=mx;i++)
            arr[i] = s[i]-'0';
        int prev=arr[0];
        int res =0;

        for(int i=1;i<=mx;i++){
            if(i>prev){
                res+=i-prev;
                prev+=i-prev;
            }
            prev+=arr[i];
        }
        cout<<"Case #"<<f<<": "<<res<<endl;
    }
    return 0;
}
