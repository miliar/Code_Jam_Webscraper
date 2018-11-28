#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
#define rep(i,a,b) for(int i=a;i<b;i++)
int main()
{
	int times;
	int cur_clapping=0;
	int friends_required,max_shyness,k=0;
	string s;
	cin>>times;
	while(times--)
	{
	   k++;
	   cin>>max_shyness;
		cin>>s;
		cur_clapping=s[0]-'0';
		friends_required=0;
		rep(i,1,s.length())
		{
			
			if(i>cur_clapping+friends_required && s[i]-'0'!=0) 
				friends_required+=i-(cur_clapping+friends_required);

			cur_clapping+=s[i]-'0';
		//cout<<"For i:"<<i<<" current clapping are: "<<cur_clapping<<endl;		
		}
	cout<<"Case #"<<k<<": "<<friends_required<<endl;
	}
	


	return 0;
}
