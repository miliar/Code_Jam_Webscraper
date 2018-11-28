#include<iostream>
using namespace std;
int x,y,ans[100],p=0,count=0;
int main()
{
    int t;
    cin>>t;
    int g=t;
    while(t--)
    {
        cin>>x>>y;
        count=0;
        for(int i=x;i<=y;i++)
    	{
        if(i==1)
        	++count;
        else if(i==4)
        	++count;
        else if(i==9)
        	++count;
        else if(i==121)
        	++count;
        else if(i==484)
        	++count;
    	}
    	ans[p]=count;
    	p++;
    }
    for(int j=0;j<g;j++)
    {
        cout<<"Case #"<<j+1<<": "<<ans[j]<<endl;
    }
    return 0;
}
