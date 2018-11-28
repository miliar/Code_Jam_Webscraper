#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t,kase=1;
    cin>>t;
    while(t--){
        int n,ans=0,sum=0;
        cin>>n;
        string s;
        cin>>s;
        sum += (s[0]-'0');
        for (int i=1;i<=n;i++){
            if (s[i]!='0'&&sum<i){
                ans += (i-sum);
                sum += (i-sum);
            }
            sum += (s[i]-'0');
        }
        cout<<"Case #"<<kase++<<": "<<ans<<endl;
    }
    return 0;
}
