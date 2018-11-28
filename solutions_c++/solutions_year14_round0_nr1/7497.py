#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
using namespace std;
typedef long long int ll;

ll t,a1,a2,a[5][5],arr[22],num,ans;

int main()
{
    cin>>t;
    int tt = 1;
    while(t--)
    {
    	cin>>a1;
    	int p = 1;
    	for(int i=0;i<4;i++)
    	{
    		for(int j=0;j<4;j++)
    		{
    			cin>>a[i][j];
    			arr[p++] = 0;
    		}
    	}
    	for(int i=0;i<4;i++)
    	{
    		arr[a[a1-1][i]] = 1;
    	}
    	cin>>a2;
    	for(int i=0;i<4;i++)
    	{
    		for(int j=0;j<4;j++)
    		{
    			cin>>a[i][j];
    		}
    	}
    	ans = 0;
    	for(int i=0;i<4;i++)
    	{
    		if(arr[a[a2-1][i]] == 1)
    		{
    			ans++;
    			num = a[a2-1][i];
    		}
    	}
    	if(ans == 1)
    	{
    		cout<<"Case #"<<tt++<<": "<<num<<"\n";
    	}
    	else if(ans == 0)
    	{
    		cout<<"Case #"<<tt++<<": Volunteer cheated!\n";
    	}
    	else
    	{
    		cout<<"Case #"<<tt++<<": Bad magician!\n";
    	}
    }	
}
    