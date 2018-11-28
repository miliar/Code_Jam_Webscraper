#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,n,i,z;
    string a,b;
    freopen("A1.in","r",stdin);
    freopen("ank1.txt","w",stdout);

    scanf("%d",&t);
    z=1;
    while(t--)
    {
        cin>>a;
        b+=a[0];
        for(i=1;i<a.size();i++)
        {
            if(a[i]>=b[0])
                b.insert(b.begin(),a[i]);
            else
                b+=a[i];
        }
        cout<<"Case #"<<z<<": "<<b<<endl;
        z++;
        a.clear();b.clear();
    }
    return 0;
}
