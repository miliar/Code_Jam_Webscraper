#include<bits/stdc++.h>
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORI(i,n) for(int i=0;i<=n;i++)
using namespace std;
main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
int TC;

cin>>TC;
int axu=1;
while(TC--)
{

    string d;
    int s;
    cin>>s;
    cin>>d;
    int inv=0;
    int a=0;
    FORI(i,s)
    {
        if(i>a)
        {
            inv+=i-a;
            a+=i-a;
        }
        a+=d[i]-'0';
    }


    cout<<"Case #"<<axu++<<": "<<inv<<endl;
}


}
