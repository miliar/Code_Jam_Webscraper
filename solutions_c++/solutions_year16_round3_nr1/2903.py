// Sheep

#include <iostream>
#include <string.h>
#include <math.h>
#include <stdlib.h>
using namespace std;

#define N 30

int a[N][2], n;
char str[10000];

int mycmp(const void* p1, const void* p2)
{
	return *(int*)p2 - *(int*)p1;
}

int main() {
	int tc,tst;
	cin >> tst;

	for(tc=1 ; tc<=tst ; ++tc)
	{
		int i,j,k=0;

		cin >> n;
		for(i=0 ; i<n ; ++i)
		{
			a[i][1] = i;
			cin >> a[i][0];
		}	
		qsort(a,n,sizeof(a[0]),mycmp);
#if 0
		for(i=0 ; i<n ; ++i)
			cout << a[i][0] << " ";
		cout << endl;
#endif
		while(1)
		{
			char m = a[0][0];
			if(!m)
				break;
			for(i=0,j=0 ; i<n && a[i][0]==m ; ++i)
			{
				a[i][0]--;
				str[k++] = a[i][1]+'A';
				j++;
				if(j==2)
				{
					str[k++] = ' ';
					j = 0;
				}
			}
			if(j)
			{
				str[k++] = ' ';
			}
		}
		str[--k] = 0;
		if(str[k-2]==' ')
		{ 
			if(str[k-4]==' ')
			{
				str[k-2] = str[k-1];
				str[k-1] = 0;
			}
			else
			{
				str[k-2] = str[k-3];
				str[k-3] = ' ';
			}
		}
		cout << "Case #" << tc << ": " << str << endl;
	}
	return 0;
}
