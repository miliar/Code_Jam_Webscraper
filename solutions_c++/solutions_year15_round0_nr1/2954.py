#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<set>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<cstring>
#include<stack>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,id=1;;
	cin>>t;
	while(t--)
    {
    	int req=0,tot;
    	int n;
    	cin>>n;
    	string str;
    	cin>>str;
    	tot = str[0]-'0';
    	
    	for(int i=1;i<=n;i++)
    	{
    		if(tot>=i)
    		{
    			tot+=str[i]-'0';
			}
			else
			{
				req++;
				tot++;
				tot+=str[i]-'0';
			}
		}
    	cout<<"Case #"<<id<<": "<<req<<endl;
    	id++;
	}
}
