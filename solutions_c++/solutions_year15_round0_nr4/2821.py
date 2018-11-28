#include<iostream>
#include<cstdio>

using namespace std;
int main()
{
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    cin>>T;
    int x,r,c;
    int flag;
    for(int t=0;t<T;t++)
    {
        cin>>x>>r>>c;
        int temp=max(r,c);
        c=min(r,c);
        r=temp;
        cout<<"Case #"<<t+1<<": ";
        if((r*c)%x!=0)
        {
            cout<<"RICHARD\n";
            continue;
        }
        if(x>max(r,c))
        {
            cout<<"RICHARD\n";
            continue;
        }
        if((x/2)>min(r,c))
        {
            cout<<"RICHARD\n";
            continue;
        }
        if(x==1)
            flag=0;
        if(x==3)
        {
            if(r==1 || c==1)
                flag=1;
            else if(r%3==0 || c%3==0)
                flag=0;
            else
                flag=1;
        }
        if(x==2)
        {
            if(r%2==1 && c%2==1)
                flag=1;
            else
                flag=0;
        }
        if(x==4)
        {
            if(c==2)
                flag=1;
            else if(r%4==0 ||c%4==0)
                flag=0;
            else
                flag=1;
        }
        if(flag==0)
            cout<<"GABRIEL\n";
        if(flag==1)
            cout<<"RICHARD\n";
    }
    return 0;
}
