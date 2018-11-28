#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r+",stdin);
    freopen("A-large.out","w+",stdout);
    set<int>cc;
    int c,t,save,i,n;
    cin>>t;
    for(c=1;c<=t;c++)
    {
        cin>>n;
        if(n==0)
        {
            cout<<"Case #"<<c<<": INSOMNIA\n";
            continue;
        }
        save=n;
        i=2;
        int prvn;
        while(cc.size()!=10)
        {
            prvn=n;
            while(n)
            {
                int y=n%10;
                cc.insert(y);
                n=n/10;
            }
            n=save*i;
            i++;
        }
        cout<<"Case #"<<c<<": "<<prvn<<"\n";
        cc.clear();
    }
    return 0;
}
