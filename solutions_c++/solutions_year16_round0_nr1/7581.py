#include<iostream>
#include<cstdio>
#include<vector>
#include<stack>
#include<queue>
#include<cmath>
#include<algorithm>
#include<string>
#include<set>
#include<utility>
#include<functional>
#include<map>
#include<sstream>
#define PB push_back
#define FOR(N,i) for(int i =0; i < N; i++)
#define lli long long int

using namespace std;

int main()
{
	//freopen("input.txt","r",stdin);
	//freopen("output.txt", "w", stdout);
 	int t;
 	scanf("%d",&t);
 	for(int i = 0 ;i < t; i++)
 	{
 		int N;
 		cin >> N;
 		
 		bool A[10] = {0};
 		int cnt = 0;
 		lli sum = 0;
 		if(N == 0)
 			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
 		else
 		{
 			int end = 0;
 			while(1)
 			{	
	 			sum += N;
	 			int x = sum;
	 			while(x >0)
	 			{
	 				int temp = x % 10;
	 				if(A[temp] == 0)
	 				{
	 					A[temp] = 1;
	 					cnt ++;
	 					if(cnt == 10)
	 					{
	 						end = 1;
	 						break;
	 					}
	 				}
	 				x/= 10;
	 			}
	 			if(end == 1)
	 			{
	 				cout << "Case #" << i+1 << ": "<< sum << endl;
	 				break;
	 			}
	 		}		
 		}

 	}

}

