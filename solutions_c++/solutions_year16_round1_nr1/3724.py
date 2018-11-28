#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int t,a,b,c,d,e,f=0;
	scanf("%d",&t);
	char A[1001],B[2002];
	while(t--)
	{
      scanf("%s",A);
      a=strlen(A);
      b=1000;
      e=1001;
      B[b]=A[0];
      for(c=1;c<a;c++)
      {
      	if(A[c]<B[b])
      	{
           B[e]=A[c];e++;
      	}
      	if(A[c]>=B[b])
      	{
            b--;
            B[b]=A[c];
      	}
      }
      printf("Case #%d: ",++f);
      for(c=b;c<e;c++)
      {
      	printf("%c",B[c]);
      }
      printf("\n");
	}
	return 0;
}