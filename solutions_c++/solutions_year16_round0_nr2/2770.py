#include<stdio.h>
#include<math.h>
#include<iostream>

#include<vector>
using namespace std;

int main()
{
	freopen ("B-large.in","r",stdin);
	freopen("B_large_output.out", "w", stdout);
	
	int T;
	scanf("%d", &T);

	//For each string
	for(int t=1;t<=T;t++){
		string str;
		cin>>str;
		int count=0;
		for(int i=0;i<str.length()-1;i++)
		{
			if(str[i]!=str[i+1]) count++;
		}
		if(str[str.length()-1]=='-') 
			count++;
		printf("Case #%d: %d\n",t,count);
	}
	return 0;
}