#include<bits/stdc++.h>
using namespace std;

typedef unsigned long long ull;

int main()
{
    int nb_cas;
    scanf("%d", &nb_cas);
    for(int cas=1;cas<=nb_cas;cas++)
    {
	printf("Case #%d:",cas);
	// solution
	int k,c,s;
	scanf("%d%d%d",&k,&c,&s);
	if(k>c*s)printf(" IMPOSSIBLE\n");
	else
	  {
	    for(int i=0;i<(k+c-1)/c;i++)
	      {
		ull pk = 1, pos = 0;
		for(int j=0;j<c && i*c+j < k;j++)
		  {
		    pos += (i*c+j)*pk;
		    pk*=k;
		  }
		printf(" %llu",pos+1);
	      }
	    printf("\n");
	  }
	// end
    }
    return 0;
}
