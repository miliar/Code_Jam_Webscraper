#include<bits/stdc++.h>
using namespace std;
struct node{int a;int b;};
bool op(struct node A,struct node B){return A.a>B.a;}
int main()
{
int t,pp,i;
scanf("%d",&t);
for( pp=1;pp<=t;pp++)
{
int n;
scanf("%d",&n);
struct node array[28]={0};
for(i=0;i<n;i++)
	{
	scanf("%d",&array[i].a);
	array[i].b=i;
	}
sort(array,array+27,op);
//for(i=0;i<=n;i++)
	printf("case #%d: ",pp);
while(array[0].a!=0)
	{
	int count=1;
	while(array[count].a==array[0].a)count++;
	if(count&1){printf("%c ",array[0].b+65);array[0].a--;}
	else {printf("%c%c ",array[0].b+65,array[1].b+65);array[0].a--;array[1].a--;}
	sort(array,array+27,op);
	}
printf("\n");
}
return 0;
}
