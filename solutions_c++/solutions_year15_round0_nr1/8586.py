#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("in", "r", stdin);
 	freopen("out", "w", stdout);
	
	int t;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ", i);
		int sm;
		cin>>sm;
		string s;
		cin>>s;
		s = " "+s;
		int n = s.size();
		int arr[n+1];
		memset(arr,0 , sizeof arr);
			
		arr[1] = s[1]-'0';
		for(int j=2;j<n;j++)
			arr[j] = arr[j-1] + s[j] - '0';
		//for(int j=1;j<n;j++)
		//	cout<<arr[j]<<" ";
		//cout<<endl;
		
		int ans=0;
		for(int j=1;j<n;j++)
		{
			if(j > arr[j]){
				int tmp = j-arr[j];
				ans += tmp;
				for(int k=j+1;k<n;k++)
					arr[k] += tmp; 	
			}
		}
		cout<<ans<<endl;
	
	}

}
