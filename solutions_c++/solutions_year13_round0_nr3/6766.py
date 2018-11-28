#include<iostream>
using namespace std;
int x,y,ans[100],p=0,count=0;
void getval()
{
    cin>>x>>y;
}
void check()
{
    for(int i=x;i<=y;i++)
    {
        if(i==1)
        {
            ++count;
        }
        else if(i==4)
        {
            ++count;
        }
        else if(i==9)
        {
            ++count;
        }
        else if(i==121)
        {
            ++count;
        }
        else if(i==484)
        {
            ++count;
        }
    }
    ans[p]=count;
    count=0;
    p++;
}
int main()
{
    int cas;
    cin>>cas;
    for(int k=0;k<cas;k++)
    {
        getval();
        check();
    }
    for(int j=0;j<cas;j++)
    {
        cout<<"Case #"<<j+1<<": "<<ans[j]<<endl;
    }
    return 0;
}