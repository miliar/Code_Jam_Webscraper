#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
using namespace std;
struct mymap{
	int cnt;
	int nmap[10];
};
typedef struct mymap mymap;

void fillMap(long long n,mymap *m1)
{
	int i=0,dig;
	long long n1=n;
	while(n1>0)
	{
		dig=n1%10;
		if(m1->nmap[dig]==0)
		{
			m1->nmap[dig]=1;
			m1->cnt++;
		}
		n1=n1/10;
	}
}

int main()
{
	mymap *m1=(mymap*)malloc(sizeof(mymap));
	int T,cse=0;
	long long N,i,n;
	scanf("%d",&T);

	while(T--)
	{		
		m1->cnt=0;
		for(i=0;i<10;i++)
		{
			m1->nmap[i]=0;
		}
		cse++;
		scanf("%Ld",&N);
		i=1;
		if(N==0)
		{
			//cout << "Case #" << cse << ": " << "INSOMNIA\n";
			printf("Case #%d: INSOMNIA\n",cse);
			continue;
		}
		else
		{
			while(1)
			{
				n=N*i;
				fillMap(n,m1);
				if(m1->cnt>=10)
				{
					//cout << "Case #" << cse << ": " << n << endl;
					printf("Case #%d: %Ld\n",cse,n);
					break;
				}
				i++;
			}
		}
	}
	return 0;
}