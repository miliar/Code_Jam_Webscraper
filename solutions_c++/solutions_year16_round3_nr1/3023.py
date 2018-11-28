#include <iostream>
#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;

struct code
{
	int x;
	char c;
};
int compare(const void *s1, const void *s2)
{
  struct code *e1 = (struct code *)s1;
  struct code *e2 = (struct code *)s2;
  return e1->x - e2->x;
}
int main() {
	// your code goes here
	int t,r=1;
	scanf("%d",&t);
	while(t--)
	{
        int n,i;
		scanf("%d",&n);
		struct code a[n];
		for(i=0;i<n;i++)
		{
			scanf("%d",&a[i].x);
			a[i].c=(char)(i+65);
		}
		qsort(a, n, sizeof(struct code), compare);
        /*i=n-1;
        int j=i-1;
            int di=a[i].x-a[j].x;
            for(int k=1;k<=(di/2);k++)
                printf("%c%c ",a[i].c,a[i].c);
            if(di%2!=0)
                printf("%c ",a[i].c);
            a[i].x=a[j].x;
            di=0;
        for(i=n-2;i>=1;i--)
        {
           j=i-1;
            di=a[i].x-a[j].x;
            for(int k=1;k<=di;k++)
                {
                printf("%c%c ",a[i].c,a[j].c);
                a[j].x--;
            }
        }
            for(i=1;i<=a[0].x;i++)
                {
                if(n==3)
                printf("%c %c%c ",a[0].c,a[1].c,a[2].c);
                else printf("%c%c ",a[0].c,a[1].c);
            }
        printf("\n");*/
        printf("Case #%d: ",r);
        r++;
    if(n==3)
        {
    int d=a[2].x-a[1].x;
    for(i=1;i<=d;i++)
        printf("%c ",a[2].c);
    a[2].x=a[1].x;
    d=a[1].x-a[0].x;
       for(i=1;i<=d;i++)
        printf("%c%c ",a[2].c,a[1].c); 
        a[1].x=a[0].x;a[2].x=a[1].x;
        for(i=1;i<=a[0].x;i++)
            printf("%c %c%c ",a[2].c,a[1].c,a[0].c);
    }
    else if(n==2)
        {
        int d=a[1].x-a[0].x;
       for(i=1;i<=d;i++)
           printf("%c ",a[1].c);
        for(i=1;i<=a[0].x;i++)
            printf("%c%c ",a[0].c,a[1].c);
    } 
    printf("\n");
} 
	return 0;
}