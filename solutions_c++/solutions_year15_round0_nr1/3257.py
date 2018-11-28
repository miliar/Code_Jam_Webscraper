#include<iostream>
#include<cstdio>
#include<vector>
#include<climits>
#include<cstring>
#include<algorithm>
#include<cmath>
#include<map>

using namespace std;
int main()
{
	long long int t,cost,ava,n,i; 
	char a[1009];
	
	
	
	cin>>t;
	int k=1;
    while(t--)
    {
    	cin>>n;
    	cost=0;
    	ava=0;
    	for(i=0;i<=n;i++)
    	{
    		cin>>a[i];
    		if(i<=ava)
    		{
    			ava+=(a[i]-'0');
    		}
    		else
    		{
    			cost+=(i-ava);
    			ava=ava+i-ava+(a[i]-'0');
    		}
    	}
    	cout<<"Case #"<<k<<": "<<cost<<endl;
		k++;
    }
    return 0;
}


