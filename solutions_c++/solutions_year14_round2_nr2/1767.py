#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	int t;
	freopen("ainp.txt", "r", stdin);
	freopen("xx.txt", "w", stdout);
	scanf("%d\n",&t);
	for(int tc = 1; tc <= t; tc++){
		printf("Case #%d: ", tc);
	    int a,b,k,res=0;
	    scanf("%d %d %d",&a,&b,&k);
	    for(int i=0; i<a;i++)
	    { for(int j=0;j<b;j++)
	       if(  (i&j) < k )
	       res++;
        }
        printf("%d\n",res);
     }
	return 0;
}
			
