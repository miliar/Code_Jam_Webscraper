#include<iostream>
#include<stdio.h>
using namespace std;
#define FOR(i,a,b)				for (i=a;i<b;i++)
#define s(n)					scanf("%d",&n)

int fair[]={1,4,9,121,484};

int main()
{
   freopen("input.txt","r",stdin);
   freopen("output.txt","w",stdout);
	int t;
	s(t);
	int i,j,a,b,count;
	char line[2];
	gets(line);
	FOR(j,0,t)
	{
      count=0;
	  scanf("%d %d",&a,&b);
	  printf("Case #%d: ",j+1);
	  for(i=0;i<5;i++)
	    if(fair[i]>=a && fair[i]<=b){
	    //cout<<fair[i];
	       count++;
	    }

	   printf("%d \n",count);
	}

return 0;
}
