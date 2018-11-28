#include <iostream>
#include <cstdio>

using namespace std;


int main()
{
	
		freopen("in","r",stdin);
		freopen("out","w",stdout);
		double C,F,X;
		int n;
		
		cin >> n;
		
		for (int i=0;i<n;i++)
		{
			cin >> C >> F >> X;
			
			double arr1[100005],arr2[100005];
			
			double quot=2;
			
			for (int h=0;h<100005;h++)
			{
				arr1[h]=X/quot;
				quot+=F;
			}
			
			quot=2;
			
			arr2[0]=0;
			for (int h=1;h<100005;h++)
			{
					arr2[h]=arr2[h-1]+C/quot;
					quot+=F;
			}
			
			double res[100005];
			
			for (int h=0;h<100005;h++)
				res[h]=arr1[h]+arr2[h];
				
			double min=res[0];
			
			for (int h=1;h<100005;h++)
				if (min > res[h])
					min=res[h];
			
			cout << "Case #"<<i+1<<": ";
			printf("%.7lf\n",min);
			
		}
	
		return 0;
}
