/* 
 * Author: Mohamad Shawkey
 * Created on April 12, 2014, 2:59 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

int solve(vector<double> &,vector<double> &);

int main()
{
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int t;
	cin>>t;
	int n;
	
	for(int z=1;z<=t;z++)
	{
		cin>>n;
		vector <double> naom,ken;
		naom.resize(n);
		ken.resize(n);
		for(int i=0;i<n;i++) cin>>naom[i];
		for(int i=0;i<n;i++) cin>>ken[i];
		sort(naom.begin(),naom.end());
		sort(ken.begin(),ken.end());
		cout<<"Case #"<<z<<": "<<solve(naom,ken)<< " "<<n-solve(ken,naom)<<endl;
	}
	return 0;
}

int solve(vector<double> & v1,vector<double> & v2)
{
	int n=v1.size();
	int res=0;
	vector <bool> tak(n);
	for(int i=0;i<n;i++) tak[i]=false;
	for(int i=n-1;i>=0;i--)
	{
		for(int j=n-1;j>=0;j--)
		{
			if(v1[i]>v2[j] && !tak[j])
			{
				res++;
				tak[j]=true;
				break;
			}
		}
	}
	return res;
}