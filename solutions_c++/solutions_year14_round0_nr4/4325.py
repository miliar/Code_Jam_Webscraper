#include <cstdio>
#include <cstdlib>
#include <algorithm>

using std::sort;

struct Data{
	double weigh[1000];
};
int main()
{
	int t, number, count, ans, j, k;
	Data a[2];
	//double weigh[2][1000];
	scanf("%d", &t);
	for( int i = 0; i < t; i++) {
	  scanf("%d", &number);
	  for( j = 0; j < 2; j++) {
		for(  k = 0; k < number; k++)
		  scanf("%lf", &a[j].weigh[k]);
	  	sort(a[j].weigh, a[j].weigh + number);
	  }
	  count = 0;
	  for( j = 0, k = 0; j < number; 1) {
		if( a[0].weigh[j] > a[1].weigh[k]) {
		  count++;
		  j++;
		  k++;
		}
		else
		  j++;
	  }
	  ans = count;
	  count = 0;
	  for(  j = 0, k = 0;  k < number; k++) {
		if( a[0].weigh[j] < a[1].weigh[k]) {
		  count++;
		  j++;
		}
	  }
	  printf("Case #%d: %d %d\n", i+1, ans, number - count);
	}
}
