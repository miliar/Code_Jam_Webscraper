#include <iostream>
#include <vector>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <set>
#include <math.h>
using namespace std;




#define SMALL
//#define LARGE

int main ()
{
	//freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small-attempt0.out","wt",stdout);
#endif
//#ifdef LARGE
//	freopen("B-large.in","rt",stdin);
//	freopen("B-large.out","wt",stdout);
//#endif
//
//	
	
	int T,t,r;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>r>>t;
		int count=0;

		double tt=t;
		int k=1;
		while(true)
		{
			double paint=pow((double)(r+k),2)-pow((double)(r+k-1),2);
			if(tt>=paint)
			{
			tt-=paint;
			k+=2;
			count++;	
			}
			else
				break;
		}
		printf("Case #%d: ",i+1 );
		cout<<count<<endl;
	}
	
		

	
	

	return 0;
}