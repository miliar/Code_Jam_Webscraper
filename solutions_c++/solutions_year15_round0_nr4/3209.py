#include<iostream>
#include<fstream>
using namespace std;

int game(int x,int m,int n)
{
    if(x==1)
        return 1;
    else if(x==2)
    {
        if((m*n)%x==0)
            return 1;
        else
            return 0;
    }
    else if(x==4)
    {
        if((m==4 && n==4) || (m==3 && n==4) || (m==4 && n==3))
        return 1;
        else return 0;
    }
    else if(x==3)
    {
        if((m!=1)&&(n%x==0))
            return 1;
        if(m%x==0 && n!=1)
            return 1;
        return 0;
    }
}

int main()
{
   freopen("ominous_omino_small.txt", "r", stdin);
   freopen("ans4_small.txt", "w", stdout);
    int i,t,x,r,c;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>x>>r>>c;
        if(game(x,r,c))
            cout<<"Case #"<<i<<": GABRIEL"<<endl;
        else
            cout<<"Case #"<<i<<": RICHARD"<<endl;
    }
    return 0;
}
