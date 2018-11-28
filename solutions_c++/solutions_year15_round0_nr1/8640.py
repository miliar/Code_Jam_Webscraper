#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
int k,t,n,count,j,pen,mv,no;
string s;
scanf("%d",&t);
for(j=1;j<=t;j++)
{	k=0;
	scanf("%d",&n);
	cin >> s ;
	
	count = 0;
	pen   = 0;
	mv    = -1;
	while(n--)
	{	no = s[k++]-48;
		count += no;
		mv ++ ;
		if(count <= mv)
		{
			count++;
			pen++;
		}
	}
	
	printf("Case #%d: %d\n",j,pen);
}
return 0;
}	
