#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for(int cas=1; cas<=t; ++cas)
	{
		int n;
		double arr1[1011];
		int p1 = 0;
		double arr2[1011];
		int p2 = 0;
		cin >> n;
		for(int i=0; i<n; ++i)
			cin >> arr1[p1++];
		for(int i=0; i<n; ++i)
			cin >> arr2[p2++];
		sort(arr1,arr1+p1);
		sort(arr2,arr2+p2);
		/*
		int t2 = 0;
		int z = 0;
		//min -> max
		for(int i=0; i<n; ++i)
		{
			if(t2==n)
			{
				z = n-i;
				break;
			}
			while(t2<n && arr1[i]>arr2[t2])
			{
				++t2;
			}		
			++t2;
		}*/
		int t2x = 0;
		int t2 = n-1;
		int z = 0;
		for(int i=n-1; i>=0; --i)
		{
			if(arr2[t2]>=arr1[i])
			{
				++z;
				--t2;
			}		
			else
			{
				++t2x;
			}
		}
		z = n-z;
		int t1x = 0;
		int t1 = n-1;
		int y = 0;
		for(int i=n-1; i>=0; --i)
		{
			if(arr1[t1]>=arr2[i])
			{
				++y;
				--t1;
			}
			else	
				++t1x;
		}
		cout << "Case #" << cas << ": " << y << " " << z << endl;
	}
	return 0;
}
//0.1  0.5  0.9
//0.3  0.4  0.6
//0 2  0
//0 1  1
//0 0  2
//1 0  2

//0.1  0.5  0.9
//0.05 0.12 0.
