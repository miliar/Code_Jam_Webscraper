#include<bits/stdc++.h>
using namespace std;

long long m;
int d;

void f(int n)
{
  while(n>0)
    {
      d |= 1<<(n%10);
      n /= 10;
    }
}

int main()
{
    int nb_cas;
    scanf("%d", &nb_cas);
    for(int cas=1;cas<=nb_cas;cas++)
    {
	printf("Case #%d: ",cas);
	// solution
	int n;
	scanf("%d",&n);
	if(n==0)
	  printf("INSOMNIA\n");
	else
	  {
	    m = 0, d = 0;
	    while(d != (1<<10) - 1)
	      {
		m += n;
		f(m);
	      }
	    printf("%llu\n",m);
	  }
	// end
    }
    return 0;
}
