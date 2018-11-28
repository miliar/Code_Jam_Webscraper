#include <bits/stdc++.h>
#include<stdio.h>
#include<math.h>
using namespace std;
#define pii pair<long long,long long>
#define PI 3.14159265
#define ll long long
#define ff first
#define ss second
#define pb push_back
#define INF 1000000009
#define mod 1000000007
 
int main() 
{
    std::ios::sync_with_stdio(false);
    ll t ;
    int counter = 1;
    cin>>t;
    while(t--)
    {
 
    	string s;
    	cin>>s;
    	char max;
    	std::vector<char> v;
 
    	for (int i = 0; i < s.length(); ++i)
    	{
    		if(i==0)
    			{
    				v.push_back(s[i]);
    				max = s[i];
    			}
    		else if(s[i]>=max)
    		{
    			v.insert(v.begin(),s[i]);
    			max = s[i];
    		}
    		else if(s[i]<max)
    		{
    			v.push_back(s[i]);
    		}
 
    	}
    	cout<<"Case #"<<counter<<": ";
    	for (vector<char>::iterator it=v.begin(); it<v.end(); it++)
    		cout << *it;
		cout<<endl;
		counter++;
 
    }
 
    return 0;
}
