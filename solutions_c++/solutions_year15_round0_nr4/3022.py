#include<bits/stdc++.h>
using namespace std;
//#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
//#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);

int main()
{   freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);

    int test,i,p,r,c,x;
     cin>>test;
     for(i=1;i<=test;i++)
     {
         cin>>x>>r>>c;
         p=r*c;
         if(x==1)
         cout<<"Case #"<<i<<": GABRIEL"<<endl;


        else if(x==2)
        {
            if(p%2==0) cout<<"Case #"<<i<<": GABRIEL"<<endl;
            else cout<<"Case #"<<i<<": RICHARD"<<endl;
        }
        else if(x==3)
        {
            if(p>3&&p%3==0) cout<<"Case #"<<i<<": GABRIEL"<<endl;
            else cout<<"Case #"<<i<<": RICHARD"<<endl;
        }
        else

        {
            if(p==12||p==16) cout<<"Case #"<<i<<": GABRIEL"<<endl;
            else cout<<"Case #"<<i<<": RICHARD"<<endl;

        }
     }

    return 0;
}
