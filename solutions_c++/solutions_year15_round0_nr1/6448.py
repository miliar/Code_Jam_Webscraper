#include <cstdio>

using namespace std;

int main()
{
  int tc, ti;
  scanf("%d",&tc);
  for (ti =1 ; ti <= tc; ++ti) {
    int smax,i;
	scanf("%d", &smax);
	int shies[smax + 1];
	char str[smax+2];
	scanf("%s", str);
	
	for ( i = 0; i <= smax;++i) {
	shies[i] = str[i] - '0';
	//printf("%d ", shies[i]);
	}
	//printf("\n");
	
	int persons = 0, reqd = 0;
	for ( i = 0; i <= smax;++i) {
	  if (persons >= i) {
	    persons += shies[i];
	  } else {
	    reqd += i - persons;
		persons = i  + shies[i];
		
	  }
	  
	}
	printf("Case #%d: %d\n", ti, reqd);
	
	
  }
  return 0;
}