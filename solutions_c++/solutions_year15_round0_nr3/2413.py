#include <iostream>
#include <stdio.h>
using namespace std;

char Base[10010];
int  L;
unsigned long long X;

int mul(int  tmp, char a)
// i = 2; j = 3; k = 4; 1 = 1, 
{
	int tmp2;
	if(a == 'i') tmp2 = 2;
	else if (a=='j') tmp2 = 3;
	else if (a=='k') tmp2 = 4;
//	printf("%d %d\n", tmp,tmp2);
	if(tmp == 1) return tmp2;
	if(tmp == -1) return -tmp2;
	if(tmp == tmp2 || tmp == -tmp2) return -(tmp/tmp2);

	int sign = tmp<0? -1:1;
	if(tmp<0) tmp = -tmp;
	if(tmp>tmp2)
	{
		swap(tmp, tmp2);
		sign*=-1;
	}
	if(tmp == 2)
	{
		if(tmp2==3) return sign*4;
		if(tmp2==4) return -1*sign*3;
	}
	else if(tmp == 3) return sign*2;
		
}
bool deal()
{

        int  tot=0;
        int flag=0;
	int tmp=1;
	int pro=1;
//	printf("%d\n" ,tot);
	if(X%4==0) return 0;
        if(X>8) tot=8*L;
	else tot=X*L;
	for(int i=0;i<tot;++i)
	{
		tmp = mul(tmp, Base[i%L]);
		if(i==L-1)
	        {
		    pro=tmp;
		    if(pro == 1) return 0;
		    else if(pro == -1 && X%4==2) return 0;
		    else if(pro!= -1 && X%4!=2) return 0;
		}
		if(flag == 0)
		{
			if(tmp == 2) ++flag; 
		}
		else if(flag == 1)
		{
			if(tmp == 4) ++flag;
			
		}
	//	printf("%d ",tmp);
	}

	if(flag == 2) return 1;
	return 0;
}

int main() {
	// your code goes here
	int T, S, i, cases;
	scanf("%d",&T);
	for(cases=0;cases<T;++cases)
	{
		printf("Case #%d: ", cases+1);
		scanf("%d%lld",&L,&X);
		scanf("%s",Base);
		if(deal()) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
