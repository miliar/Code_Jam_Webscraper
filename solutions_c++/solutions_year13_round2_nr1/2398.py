#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cmath>

using namespace std;

int main()
{
	int t = 0, T;
	int a, n;
	int motes[100];
	long long motes_sum[101];
	int i;
	int temp, additions;;
	//bool is_motes_remaining;
	int operations;
	scanf("%d", &T);
	while(t<T)
	{
		t++;
		//is_motes_remaining = false;
		operations = 0;
		scanf("%d %d", &a, &n);
		for(i=0; i<n; i++)
		{
			scanf("%d", motes + i);
		}
		sort(motes, motes + n);
		motes_sum[0] = a;
		for(i=0; i<n; i++)
		{
			//printf("a_size = %lld\nmotes[i] = %d\n", motes_sum[i], motes[i]);
			if(motes[i] >= motes_sum[i])
			{
				additions = 0; temp = motes_sum[i];
				if(temp == 1)
				{
					operations += (n-i);
					break;
				}

				while(temp <= motes[i])
				{
					temp += (temp - 1);
					additions++;
				}
				if(additions >= (n-i))
				{
					operations += (n-i);
					break;
				}
				else
				{
					operations += (additions);
					motes_sum[i] = temp;
				}
			}

			motes_sum[i+1] = motes_sum[i] + motes[i];
		}

		printf("Case #%d: %d\n", t, operations);


	}



	return 0;
}
