#include<bits/stdc++.h>
using namespace std;

#define N 2000
bool ismax[N];
char s[N];

int main()
{
    int nb_cas;
    scanf("%d", &nb_cas);
    for(int cas=1;cas<=nb_cas;cas++)
    {
	printf("Case #%d: ",cas);
	// solution
	scanf("%s",s);
	char curmax = 0;
	int i=0;
	while(s[i]!=0)
	  {
	    ismax[i]=false;
	    if(s[i]>=curmax)
	      {
		ismax[i]=true;
		curmax=s[i];
	      }
	    i++;
	  }
	i--;
	while(i>=0)
	  {
	    if(ismax[i])
	      printf("%c",s[i]);
	    i--;
	  }
	i=0;
	while(s[i]!=0)
	  {
	    if(!ismax[i])
	      printf("%c",s[i]);
	    i++;
	  }
	printf("\n");
	// end
    }
    return 0;
}
