#include<iostream>
#include<fstream>
using namespace std;

int s,es,f[1010],a[1010];

bool special(int k,int mid)
{
    while(s<1010)
    {
        s++;
        a[s]=0;
    }
    es=0;
    for(int i=1; i<=s; i++)
    {
        if(a[i]<=mid)
        {}
        else if(a[i]>mid)
        {
            int diff=a[i]-mid;
            es++;
            f[es]=diff;
        }
    }
    int index=1;
    while( index<=es )
    {
        if(f[index]>0 && k==0)
        {
            return false;
        }
        if(mid>=f[index])
        {
            index++;
            k--;
        }
        else
        {
            f[index]-=mid;
            k--;
        }
    }
    return true;
}
int main()
{
    ifstream cin;
    ofstream cout;
    cin.open("B-large.in");
    cout.open("B-large-output.txt");
	int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
    	int ans=0,d,j,k,p;
    	cin>>d;
    	s=0;
    	for(j=1;j<=d;j++)
    	{
    		cin>>p;
    		s++;
    		a[s]=p;
    	}
    	int result=1000006;
    	for(k=0;k<=1000;k++)
    	{
    		int low,mid,high;
    		low=1;
    		high=1000;
    		while(low<high)
    		{
    			mid=low+(high-low)/2;
                bool temp=special(k,mid);
                if(temp==false)
                {
                	low=mid+1;
                }
                else
                {
                	high=mid;
                }
    		}
    		if(k+low<result)
            {
                result=k+low;
            }
    	}
    	cout<<"Case #"<<i<<": "<<result<<endl;
    }
    return 0;
}

