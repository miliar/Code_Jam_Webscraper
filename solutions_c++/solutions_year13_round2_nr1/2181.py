#include<iostream>
#include<stdio.h>
#include<cstring>
#include<algorithm>
#define SIZE 100
using namespace std;
int motes[SIZE+1];
int main()
{
	freopen("A-small-attempt2.in","r",stdin);
	freopen("a.txt","w",stdout);
	int cases,t,A,N,i,counter,tmp,c;
	cin>>t;
	for(cases=1;cases<=t;cases++)
	{
		cin>>A>>N;
		for(i=0;i<N;i++)
			cin>>motes[i];
		if(A==1)
		{
			printf("Case #%d: %d\n",cases,N);
			continue;
		}
		sort(motes,motes+N);
		counter=0;
		for(i=0;i<N;i++)
		{
			if(A>motes[i])
				A+=motes[i];
			else
			{
				tmp=A;
				c=0;
				while(tmp<=motes[i])
				{
					c++;
					tmp+=tmp-1;
				}
				//cout<<tmp<<endl;
				if(c>=N-i)
				{
					counter+=N-i;
					break;
				}
				else
					counter+=c;
				A=tmp;
				i--;
			}
		}
		printf("Case #%d: %d\n",cases, counter);
	}
	return 0;
}