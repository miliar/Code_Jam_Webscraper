/*input

*/
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
    ll t;
    cin>>t;
    int counter=1;
    while(t--)
    {
    	int n;
    	cin>>n;
    	int ar[2501];
    	for (int i = 0; i < 2501; ++i)
    	{
    			ar[i] = 0 ;
    		
    	}
    	for (int i = 0; i < (2*n-1)*n; ++i)
    	{
    	 	
    			int x;
    			cin>>x;
    			ar[x]++;
    		
    		
    	}
    	cout<<"Case #"<<counter<<": ";
    	for (int i = 0; i < 2501; ++i)
    	{
    		if(ar[i]%2!=0 && ar[i]!=0)
    			cout<<i<<" ";
    	}
    	cout<<endl;
    	counter++;

    }

    return 0;
}
