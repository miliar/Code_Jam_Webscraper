#include<iostream>
#include<vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <string>
#include <queue>
#include <sstream>
#include <iostream>
#include<string.h>
#include <iomanip>
#include <cstdio>
#include<math.h>
#include <cmath>
#include <cstdlib>
#include <ctime>
#define ull unsigned long long 
#define pi 3.141592653589793
#define ARRAY_SIZE(A) sizeof(A)/sizeof(A[0])
#define PB push_back
#define INF 1<<30
using namespace std;
int main()
{
	int n =0;
	cin>>n;int tt =1;
	while(n--)
	{
		int c =0;
		cin>>c;
		vector<double>arr(c);
		vector<double>brr(c);
		for(int i =0;i<c;i++)
		{
			scanf("%f",&arr[i]);
		}
		sort(arr.begin(),arr.end());
		for(int i =0;i<c;i++)
		{
			scanf("%f",&brr[i]);
		}
		sort(brr.begin(),brr.end());
		int bstart =0;int bend =c-1;int ans =0;
		for(int i =0;i<c && bstart<=bend;i++)
		{
			if(arr[i]<brr[bstart])
			{
				bend--;
			}
			else
			{
				bstart++;
				ans++;
			}
		}
	int sec =0;
		for(int i =0;i<arr.size();i++)
		{
			for(int j =0;j<brr.size();j++)
			{
				if(brr[j]>arr[i])
				{
					if(j!=0 && brr[j-1]<arr[i])
					{
						brr.erase(brr.begin()+j);sec++;
					}
					else if(j == 0)
						{brr.erase(brr.begin()+j);sec++;}
				}
			}
		}
		cout<<"Case #"<<tt++<<": ";
		cout<<ans<<" "<<c-sec<<endl;
	}
	return 0;
}