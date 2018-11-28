// DeceitWar.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <iomanip>

using namespace std;

int cmpfunc (const void * a, const void * b)
{
	if (*(double*)a > *(double*)b) return -1;
	else if (*(double*)a < *(double*)b) return 1;
	else return 0;  
}

int main()
{
	int T,testCounter = 1;
	cin>>T;
	while (T--)
	{
		int n, wpoints = 0, dpoints = 0;
		cin>>n;

		double* naomi, *ken;
		bool* nburn, *kburn;

		naomi = new double[n];
		ken = new double[n];
		nburn = new bool[n];
		kburn = new bool[n];

		for (int i=0; i<n; i++)
		{
			cin>>naomi[i];
			nburn[i] = false;
		}

		for (int i=0; i<n; i++)
		{
			cin>>ken[i];
			kburn[i] = false;
		}

		qsort(naomi, n, sizeof(double), cmpfunc);
		qsort(ken, n, sizeof(double), cmpfunc);

		//Play normal war
		int nstart=0, kstart=0, kend = n-1;
		while (nstart < n)
		{
			if (naomi[nstart] > ken[kstart])
			{
				kend--;								
				wpoints++;
			}
			else
			{
				kstart++;
			}
			nstart++;
		}

		//Play D war
		int kindex = 0, nindex = 0, nlast = n-1;
		while (kindex < n)
		{
			//Get N's optimal value i.e least of max values
			int i=0;
			nindex = -1;
			for (i=0; i<n; i++)
			{
				if (naomi[i] > ken[kindex])
				{
					if (!nburn[i])
					{
						nindex = i;
					}
				}
				else
				{
					break;
				}
			}

			if ((i>0) && (nindex!= -1))
			{
				dpoints++;
				nburn[nindex] = true;
			}
			else
			{
				nburn[nlast] = true;
				nlast--;
			}
			kburn[kindex] = true;
			kindex++;
		}

		printf("Case #%d: %d %d\n",testCounter,dpoints, wpoints);
		testCounter++;	

		delete[] naomi;
		delete[] ken;
		delete[] nburn;
		delete[] kburn;
	}

	return 0;
}


