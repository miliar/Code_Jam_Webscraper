#include <algorithm>
#include <bitset>
#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
using namespace std;

int main()
{
	freopen("in.txt", "r",stdin);
    freopen("out.txt", "w",stdout);
    int n;
    cin>>n;
    for (int i = 0; i < n; ++i)
    {
    	vector<int> uan;
		vector<int> tu;
    	int a;
    	cin>>a;
    	for(int j=0;j<16;j++)
    	{
    		int c;
    		cin>>c;
    		if(j>=4*(a-1) && j<=(4*a)-1)
    		{
    			//cout<<"ce de uno : "<<c<<endl;
    			uan.push_back(c);
    		}
    	}
    	cin>>a;
    	for(int j=0;j<16;j++)
    	{
    		int c;
    		cin>>c;
    		if(j>=4*(a-1) && j<=(4*a)-1)
    		{
    			//cout<<"ce de dos : "<<c<<endl;
    			tu.push_back(c);
    		}
    	}
    	int ans=0;
    	int res=0;
    	for(int j=0;j<4;j++)
    	{
    		
    		for(int k=0;k<4;k++)
    		{
    			//cout<<"uan j : "<<uan[j]<<endl;
    			//cout<<"tu k : "<<tu[k]<<endl;
    			if(uan[j]==tu[k])
    			{
    				//cout<<"IS HERE ...! "<<endl;
    				res=uan[j];
    				ans++;
    			}
    		}
    	}
    	if(ans==1)
    	{
    		cout<<"Case #"<<i+1<<": "<<res<<endl;
    	}else if(ans==0)
    	{
    		cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
    	}else
    	{
    		cout<<"Case #"<<i+1<<": Bad magician!"<<endl;	
    	}
    }
}