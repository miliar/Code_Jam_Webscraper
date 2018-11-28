#include <bits/stdc++.h>
using namespace std;
int dp[110];
char arr[110];
int main()
{
	int t;
	cin>>t;
	int p=1;
	while(t--){
		int cnt=0;
		scanf("%s",(arr));
		int n=strlen(arr);
		for(int i=n-1;i>=0;i--)
		{
			if(arr[i]=='+'){
//				cout<<"@";
			continue;
			}
			else 
			{
//				cout<<"#";
				arr[i]='+';
				cnt++;
				int j;
				for( j=i-1;j>=1;j--)
				{
				if(arr[j]=='-'){
					arr[j]='+';
					continue;
				}
				else 
				break;
			    }
				i=j;
				for(int k=i;k>=0;k--)
				arr[k]=='+'?arr[k]='-':arr[k]='+';
//				for(int k=0;k<n;k++)cout<<arr[k]<<" ";cout<<"\n";
				i++;
			}
		}
		cout<<"Case #"<<p<<": "<<cnt<<"\n";
		p++;
	}
}
