using namespace std;
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cctype>
#include <climits>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <string>

typedef long long L;
typedef unsigned long long U;
typedef pair<int,int> ii;
typedef pair<int,ii> iii;

main()
{
	int tc;
	cin>>tc;
	for(int t = 1;t <= tc; t++)
	{
		int n;
		cin>>n;
		int arr[n];
		map<int,int>mp;
		for(int i = 0;i< n;i++)
		{
			scanf("%d", &arr[i]);
			mp[arr[i]] = i;
		}
		int m = n*n;
		sort(arr, arr+n);
		do{
			/*for(int i = 0;i<n;i++)
				cout<<arr[i]<<" ";
			cout<<endl;*/
			int i;
			for(i = 1;i<n;i++)
			{
				if(arr[i] < arr[i-1])
					break;
			}
			bool flag = 1;
			for(;i<n;i++)
			{
				if(arr[i] > arr[i-1])
				{
					flag = 0;
					break;
				}
			}
			if(flag)
			{
				int c = 0;
				int A[n];
				for(int i = 0;i<n;i++)
					A[i] = mp[arr[i]];
				/*for(int i = 0;i<n;i++)
					cout<<A[i]<<" ";
				cout<<endl;*/
			
				for(int i = 0;i<n;i++)
				{
					for(int j = 0;j<n-1-i;j++)
					{
						if(A[j] > A[j+1])
						{
							c++;
							int tmp = A[j];
							A[j] = A[j+1];
							A[j+1] = tmp;
							//cout<<"Swap "<<A[j]<<" "<<A[j+1]<<endl;	
						}
					}
				}
				if(c < m)
					m = c;
				//cout<<"#"<<c<<endl;
			}
		}while(next_permutation(arr, arr+n));
		printf("Case #%d: %d\n", t, m);
	}
}
