#include<bits/stdc++.h>
using namespace std;

char s[101];

int main()
{
    int nb_cas;
    scanf("%d", &nb_cas);
    for(int cas=1;cas<=nb_cas;cas++)
    {
	printf("Case #%d: ",cas);
	// solution
	scanf("%s",s);
	int i=1, n=0;
	while(s[i]!=0)
	  {
	    if(s[i]!=s[i-1])n++;
	    i++;
	  }
	if(s[i-1]=='-')n++;
	printf("%d\n",n);
	// end
    }
    return 0;
}
