#include <bits/stdc++.h>
using namespace std;

int main() 
{
#ifndef ONLINE_JUDGE
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
#endif
  ios_base::sync_with_stdio(false);
	int t;cin>>t;
	for(int m=0;m<t;m++)
	{
// 		cout<<"inside for-1\nm="<<m<<endl; 
		int required=0;int sum=0;
		int smax;cin>>smax;
		string s;cin>>s;
// 		cout<< s.length()<<endl;
		for(int i=0;i<s.length();i++)
		{
// 			cout<<"inside for-2\ni="<<i<<endl;
		  
			if(sum<i)
			{
// 				cout<<"inside if"<<endl;
				required+=(i-sum);
				sum+= (i-sum);
				
			}/*
			else
			{
				
				required+=(i-sum);
				sum+= (required+(s.at(i)-48));
			}*/
			sum+= (s.at(i)-48);
		}
		cout<<"Case #"<<(m+1)<<": "<<required<<endl;
 
	}
 
	return 0;
}