#include <cstdio>
#include <cstdlib>
#include<climits>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
#define F(i,a,n) for(int i=a;i<n;i++)
const int MOD = 1000002013;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

bool myfunction (pair<int,int> i,pair<int,int> j) 
{
 	return (i.second<j.second); 
}

int main() {
    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
 	int t;
 	cin>>t;
 	F1(i,t)
 	{
 		int n;
 		cin>>n;
 		int sum=0;
 		vector<pair<int,int>> v;
 		vector<string> ans;
		F0(j,n)
		{
			int a;
			cin>>a;
			sum+=a;
			pair<int,int> p;
			p=make_pair(j,a);
			v.push_back(p);	
		}
		sort(v.begin(),v.end(),myfunction);
		//F0(k,n)
		//	{
		//	cout<<v[k].first<<" "<<v[k].second<<endl;
		//}
		ans.clear();
		for(int j=v.size()-1;j>=0;j--)
		{	
			string s;
			//cout<<sum<<endl;
			//F0(k,n)
			//{
			//	cout<<v[k].first<<" "<<v[k].second<<endl;
			//}
			//cout<<endl;
			//s.clear();
			if(v[j].second==0)
			{
				continue;
			}
			if(v[j].second>=2)
			{
				v[j].second-=2;
				if(j==0)
				{
					continue;
				}
				if(sum/2>v[j-1].second)
				{
					char ch=v[j].first+65;
					s.push_back(ch);
					s.push_back(ch);
					ans.push_back(s);
					sum-=2;
					j++;
					sort(v.begin(),v.end(),myfunction);
					continue;
				}	
				else
				{
					v[j].second+=2;
				}
			}
			v[j].second--;
			if((sum+1)/2>v[j-1].second)
			{
				char ch=v[j].first+65;
				s.push_back(ch);
				ans.push_back(s);
				sum-=1;
				j++;
				sort(v.begin(),v.end(),myfunction);
				continue;
			}
			else
				v[j].second++;
			
			v[j].second--;
			v[j-1].second--;
			char ch=v[j].first+65,ch1=v[j-1].first+65;
			s.push_back(ch);
			s.push_back(ch1);
			ans.push_back(s);
			sum-=2;
			j++;
			sort(v.begin(),v.end(),myfunction);	
		}
		cout<<"Case #"<<i<<": ";
		F0(j,ans.size())
		{
			cout<<ans[j]<<" ";
		}
		cout<<endl;
	}
	
	return 0;
}
