#include <bits/stdc++.h>
using namespace std;

int main()
{
	int N;
	cin >> N;

	for (int j = 0; j < N; ++j)
	{
		map<int,int> store_num ;
		int arr[10] ;
		fill_n(arr,10,0);
		long long inp ;
		cin >> inp ;

		bool cond = false ;
		int counter = 1 ;
		long long num = inp ;
		long long res = 0 ;

		while(!store_num[num] && !cond)
		{
			num = inp*(long long)(counter);
			res = num ;
			store_num[num] = 1 ;
			while(num!=0)
			{
				int r = num%10;
				arr[r] = 1 ;
				num = num/10 ;
			}

			int i = 0 ;
			for (i ; i < 10; ++i)
			{
				if(arr[i]==0) break;				
			}

			if(i==10) cond = true ; 
			else counter++ ;
		}

		if(cond)
		{
			cout << "Case #" << j+1 << ": " << res << endl ;
		}
		else
		{
			cout << "Case #" << j+1 << ": INSOMNIA" << endl ;
		}
	}
}