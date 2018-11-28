#include<iostream>
#include<cstdio>
#include<string>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,k;
    string str;
    cin>>t;
    for(int cas=1;cas<=t;cas++) {
        cin>>k>>str;
        int total=0;
        int ans=0;
        for(int i=0;i<=k;i++) {
            int x=str[i]-'0';
            //cout<<"x:"<<x<<"i:"<<i<<"total:"<<total<<endl;
            if(total<=i) {
                ans+=i-total;
                total=i;
            }
            total+=x;
        }
        cout<<"Case #"<<cas<<": "<<ans<<endl;
    }
    return 0;
}
