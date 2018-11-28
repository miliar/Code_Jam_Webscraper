#include <bits/stdc++.h>

#define in(n) scanf("%d",&n)
using namespace std;

int main() {
	// your code goes here
	int t;
	string s;
	
	cin>>t;
	
	for(int i=1;i<=t;i++)
	{
		cin>>s;
		int arr[26];
		for(int j=0;j<26;j++)
		arr[j]=0;
		
		int ans[10];
		for(int j=0;j<10;j++)
		ans[j]=0;
		
		for(int j=0;j<s.length();j++)
		{
			arr[s[j]-'A']++;
		}
		
		ans[0]=arr['Z'-'A'];
		ans[2]=arr['W'-'A'];
		ans[8]=arr['G'-'A'];
		ans[3]=arr['H'-'A']-ans[8];
		ans[6]=arr['X'-'A'];
		ans[4]=arr['U'-'A'];
		ans[5]=arr['F'-'A']-ans[4];
		ans[7]=arr['V'-'A']-ans[5];
		ans[1]=arr['O'-'A']-ans[4]-ans[2]-ans[0];
		ans[9]=arr['I'-'A']-ans[5]-ans[6]-ans[8];
		
		printf("Case #%d: ",i);
		for(int j=0;j<10;j++)
		{
			while(ans[j]>0)
			{
				printf("%d",j);
				ans[j]--;
			}
		}
		printf("\n");
	}
	return 0;
}