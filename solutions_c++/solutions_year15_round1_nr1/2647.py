#include <cstdio>
#include <cstring>
#include <algorithm>

#include<bits/stdc++.h>

 int read_int(){
	char r;
	bool start=false,neg=false;
	 int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}
using namespace std ;
int main()
{

	 // freopen("abc.txt","r",stdin);
	 //  freopen("pqr.txt","w",stdout);

int nooftest;
	nooftest=read_int();
	// cout<<nooftest<<endl;
	int xam;

	for(xam=0;xam<nooftest;xam++)
	{
		int n;
	    n=read_int();



		int ama[n];
		int jam;



		for(jam=0;jam<n;jam++)

		  ama[jam]=read_int();



		int cka=ama[0];


		jam=1;


		while(jam<n)
		{

			if(ama[jam]>cka)cka=ama[jam];

			jam++;

		}
		int maximum=cka,s;
		int i;
		for(i=1;i<cka+1;i++)
		{
			s=i;

			for(jam=0;jam<n;jam++)
			{
				if(ama[jam]>i)
				{
					if(ama[jam]%i==0)

						s+=((ama[jam]/i)-1);

					else

						s+=ama[jam]/i;
				}

			}
			maximum=min(maximum,s);
		}
		int r=maximum;
		printf("Case #%d: %d\n",xam+1,r);
	}

	return 0;
}
