/*Ominous Omino*/
#include<iostream>
using namespace std;
int main()
{
    freopen("D-small-attempt3.in","r",stdin);
    freopen("4_small.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {   int x,r,c;
        cin>>x>>r>>c;
        int flag=1;
        if(x==2)
        {   if((r*c)%2)
                flag=0;
        }
        else if(x==3)
        {   if(r*c!=3&&(r*c)%3==0)
                ;
            else
                flag=0;
        }
        else if(x==4)
        {   if(r*c==12||r*c==16);
            else
                flag=0;
        }
        cout<<"Case #"<<cas<<": ";
        if(flag)
            cout<<"GABRIEL\n";
        else
            cout<<"RICHARD\n";
        cas++;
    }
    return 0;
}
