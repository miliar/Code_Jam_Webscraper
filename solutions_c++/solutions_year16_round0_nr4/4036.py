#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
    int test;
    cin>>test;
    for(int i=1;i<=test;i++){
       int k,c,s;
       cin>>k>>c>>s;

        cout<<"Case #"<<i<<": ";
        long long int j=1;
        long long int add=pow(k,c-1);
        while(s--){
            cout<<j<<" ";
            j+=add;
        }cout<<endl;

    }
    return 0;
}
