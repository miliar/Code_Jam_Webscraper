#include <iostream>
#include <stdio.h>
#include <string.h>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <math.h>
#include <utility>
#include <sstream>
#include <queue>
#include <stack>
#include <iomanip>
#include <ctime>
#include <limits.h>
#include <bitset>
#include <functional>
#include <numeric>
#include <complex>
#include <fstream>

typedef long long int lld;
using namespace std;
int compare (const void * a, const void * b)
{
	float x=*(float*)a;
	float y=*(float*)b;
  return ( x>y);
}
int main()
{
	 ifstream read ("input.txt");
	int t;
	 read>>t;
	ofstream myfile;
    myfile.open ("output.txt");
	for(int l=1;l<=t;l++)
	{
		int n,ans=0,ans2=0;
		read>>n;
		//cout<<n;
		float a[n];
		float *b=new float[n];
        for(int i=0;i<n;i++)
			read>>a[i];

        for(int i=0;i<n;i++)
			read>>b[i];
		qsort (a, n, sizeof(float), compare);
		qsort (b, n, sizeof(float), compare);
        int i=n-1,j=n-1,il=0;
		while(i>=0 && j>=0 && i>=il)
		{
			if(a[i]<b[j])
			{
				il++;
				j--;
			}
			else
			{
				i--;j--;ans++;
			}
		}
		int jl=0;
		i=n-1;j=n-1,il=0;

		while(i>=il && j>=jl)
		{
			//cout<<a[i]<<b[j]<<endl;
			if(a[i]>b[j]){ans2++;cout<<ans2;
			i--;jl++;
			}
			else
			{
			j--;i--;
			}
		}

		myfile<<"Case #"<<l<<": "<<ans<<" "<<ans2<<endl;
	}
}

