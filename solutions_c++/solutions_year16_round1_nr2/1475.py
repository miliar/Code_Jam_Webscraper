#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int x=0;
	while(t--)
	{x++;
		int n;
		scanf("%d",&n);
		int m=0;
		int m2 = 2501;
		int a[200][51];
		int arr[2501];
		for(int i=0;i<2501;i++)
			arr[i]=0;
		for(int i=0;i<2*n-1;i++)
			 {
			 	for(int j=0;j<n;j++)
			 	{
			 		scanf("%d",&a[i][j]);
			 		arr[a[i][j]]++;
			 		m2 = min(m2,a[i][j]);
			 		m = max(m,a[i][j]);
			 	}
			 }
			
		
        vector<int>v;
        for(int i=0;i<2501;i++)
        {
        	if(arr[i]%2)
        		v.push_back(i);
        }
        sort(v.begin(),v.end());
        printf("Case #%d: ",x);
        for(int i=0;i<(int(v.size()));i++)
        	printf("%d ",v[i]);
        printf("\n");
       }
       return 0;
   }
