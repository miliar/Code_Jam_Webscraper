#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
#include<fstream>
#include<cstring>
#include<stack>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<queue>
#define ll long long int
using namespace std;
int main()
{
	ifstream cin;
	ofstream cout;
	cin.open("C:\\Users\\Admin\\Downloads\\1.in");
	cout.open("C:\\Users\\Admin\\Downloads\\out.txt");
	ll t,x=1;
	cin>>t;
	while(t--){
		ll i,count=0,val,sum=0;
		cin>>val;
		string s;
		cin>>s;
		for(i=1;i<s.size();i++){
			sum+=s[i-1]-'0';
			if(i>sum)
				{
				count+=i-sum;
				sum+=i-sum;
				}
		}
		cout<<"Case #"<<x++<<": "<<count<<endl;
	}
	return 0;
} 