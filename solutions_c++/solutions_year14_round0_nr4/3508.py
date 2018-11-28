#include<iostream>
#include<cstdio>
#include<algorithm>

using namespace std;

int main()
{
	int t,n;
	double a[1005];
	double b[1005];
	
	scanf("%d",&t);
	for(int k = 1 ; k <= t ; k++)
	{
		scanf("%d",&n);
		for(int i = 0 ; i < n ; i++)
			scanf("%lf",&a[i]);
		for(int i = 0 ; i < n ; i++)
			scanf("%lf",&b[i]);
			
		sort(a,a+n);
		sort(b,b+n);
		
		/*
		for(int i = 0 ; i < n ; i++)
			cout << a[i] << " " ;
		puts("");
		for(int i = 0 ; i < n ; i++)
			cout << b[i] << " ";
		puts("");
		*/
		
		int ans_a = 0;
		for(int i = n-1 , j = n-1 ; i>=0 && j>=0 ; )
		{
			if(a[i] > b[j])
			{
			//	cout << b[i] << ">" <<  a[j] << endl ;
				i--;
				j--;
				ans_a++;
			}
			else
				j--;
		}
		
		int ans_b = n;
		for(int i = n-1 , j = n-1 ; i>=0 && j>=0 ; )
		{
			if(b[i] > a[j])
			{
			//	cout << b[i] << ">" <<  a[j] << endl ;
				i--;
				j--;
				ans_b--;
			}
			else
				j--;
		}
		
		printf("Case #%d: %d %d\n", k , ans_a, ans_b);
	}
	return 0;
}


