/*input
1
+-+-
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
 ll count = 1;
 ll t;
 cin>>t;
 while(t--)
 {
 	ll total = 0;
 	char b;
 	string s;
 	cin>>s;
 	ll counter = 1;
 	char a = s[0];
 	ll n = s.length();
 	while(counter<n)
 	{
 		b=s[counter];
 		if(a!=b)
 			{total++;
 				a = b;
 			}
 			counter++;
 	}

 	if(a=='+')
 		cout<<"Case #"<<count<<": "<<total<<endl;
 	else
 		cout<<"Case #"<<count<<": "<<total+1<<endl;
 	count++;
 }   
    return 0;
}

