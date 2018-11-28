#include<iostream>
#include<vector>
#include<stdio.h>
#include<algorithm>
#include<math.h>
#include<string>
#include<cmath>
using namespace std;
int arr[1000002];
int main()
{
	freopen ("output.txt","w",stdout);
	freopen ("input.txt","r",stdin);
	long long T,n,x,y;//,s,arr[103],arr2[103]={0};
	string s;
	cin>>T;
	for(int F=1;F<=T;F++)
	{
		int ans=0;
		cin>>s>>n;
		arr[0]=0;
		if(s[0]=='a'||s[0]=='e'||s[0]=='i'||s[0]=='o'||s[0]=='u')
			arr[1]=0;
		else
			arr[1]=1;
		for(int f=1;f<s.length();f++)
		{
			if(s[f]=='a'||s[f]=='e'||s[f]=='i'||s[f]=='o'||s[f]=='u')
				arr[f+1]=0;
			else
				arr[f+1]=1;
			arr[f+1]+=arr[f];
		}
		int temp=0;
		for(int f=n;f<s.length()+1;f++)
		{
			if(arr[f]==arr[f-n]+n)
			{
				temp=f-n+1;
			}
			ans+=temp;
		}
		cout<<"Case #"<<F<<": "<<ans<<endl;
	}
}