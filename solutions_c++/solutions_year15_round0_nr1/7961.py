#include <iostream>
using namespace std;

int main()
{
    int t,n,i,invites,cnt,sum;
    string str;
    cin>>t;
    cnt=1;
    while(t--){
        cin>>n;
        int a[n+1];
        cin>>str;
        sum=0;
        invites = 0;
        a[0] = str[0] - '0';
        for(i=1;i<=n;++i){
            a[i] = str[i] - '0';
            sum = sum + a[i-1];
            if(sum < i){
                ++invites;
                sum = sum + 1;
            }
        }
        cout<<"Case #"<<cnt++<<": "<<invites<<endl;
    }
    return 0;
}
