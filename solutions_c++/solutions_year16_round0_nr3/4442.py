#include <bits/stdc++.h>
using namespace std;

//https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
long long int gcd( long long int a, long long int b) {
	long long int remainder;
	while (b != 0) {
		remainder = a % b;
		a = b;
		b = remainder;
	}
	return a;
}

long long int find_fact(long long int number,long long int x = 2) {

	long long int x_fixed = 2,cycle_size = 2,factor = 1;

	while (factor == 1) {

		for (long long int count=1;count <= cycle_size && factor <= 1;count++) {
			x = (x*x+1)%number;
			factor = gcd(x - x_fixed, number);
		}

		cycle_size *= 2;
		x_fixed = x;
	}
	return factor;
}
void khaali(int from,int to,int till,int a[])
{
	int p;
	for(p=from;p<to;p++)
		a[p]=0;
	a[to] = 1;
	for(p=to+1;p<=till;p++)
		a[p]=0;
}

long long int tobase(int a[],long long int ba,int n)
{
	long long int num = 0,mul=1;
	int i;
	for(i=0;i<n;i++)
	{
		num+=a[i]*mul;
		mul*=ba;
	}
	return num;
}
//find next no. div by 3 , if no factor found , find new number

int main()
{
	int t,cs=0;
	int n,j;
	int a[50];
	long long int cno,bfact[12];
	int i,cnt=0,ba,skip,first,d,e,f,g,h;
	scanf("%d",&t);
	while(t--)
	{	
		cs++;
		memset(a,0,sizeof(a));
		printf("Case #%d:\n",cs);
		scanf("%d %d",&n,&j);
		a[0] = 1;
		a[n-1] = 1;
		cnt =0;
		skip=0;
		first=0;
				for(i=1;i<=14;i++)
				{
					khaali(1,i,14,a);

					//inner most loop
					skip=0;
					
						for(ba = 2;ba<=10;ba++)
								{
									cno = tobase(a,ba,n);
									bfact[ba] = find_fact(cno);
									if(bfact[ba]==-1)
									{
										bfact[ba] = find_fact(cno,3);
										if(bfact[ba]==-1)
										{
											skip=1;
											break;
										}
									}
								}
								if(!skip)
								{
									//printf("%d\n",cnt);
									//for(d=0;d<n;d++)
									//printf("%d",a[d]);
									
								printf("%lld",tobase(a,10,n));

									for(ba=2;ba<=10;ba++)
										printf(" %lld",bfact[ba]);
									printf("\n");
									cnt++;
									first++;
									if(cnt==j)
										break;

								}
					
					/*	for(d=0;d<n;d++)
									printf("%d ",a[d]);	
									printf("\n");	
					*/
				}

								if(cnt==j)
									break;

				for(h=1;h<=11;h++)
				{
				for(e=h+1;e<=12;e++)
				{

					/*
					for(p=1;p<e;p++)
						a[p]=0;
					a[e] = 1;
					for(p=e+1;p<=14;p++)
						a[p]=0;
					*/
					//khaali(1,e,12,a);
					for(f=e+1;f<=13;f++)
					{
						//khaali(e+1,f,13,a);
						for(g=f+1;g<=14;g++)
						{
							//khaali(f+1,g,14,a);
							for(i=0;i<16;i++)
								a[i] = 0;
							a[0] = 1;
							a[15] = 1;
							a[h]=1;
							a[e] =1;
							a[f] =1;
							a[g] =1;
							//for(d=0;d<n;d++)
							//		printf("%d ",a[d]);	
							//		printf("\n");	

								
								//innermost loop
							skip=0;
								for(ba = 2;ba<=10;ba++)
								{
									cno = tobase(a,ba,n);
									bfact[ba] = find_fact(cno);
									if(bfact[ba]==-1)
									{
										bfact[ba] = find_fact(cno,3);
										if(bfact[ba]==-1)
										{
											skip=1;
											break;
										}
									}
								}
								if(!skip)
								{
									//printf("%d\n",cnt);
									//for(d=0;d<n;d++)								//for(d=0;d<n;d++)
									//printf("%d",a[d]);
								printf("%lld",tobase(a,10,n));

									for(ba=2;ba<=10;ba++)
									{
										//printf("base %d num %lld ",ba ,tobase(a,ba,n));
										printf(" %lld",bfact[ba]);
										//printf("\n");
									}
									printf("\n");
									cnt++;
								}


								if(cnt==j)
									break;
								
						}

								if(cnt==j)
									break;
					}

								if(cnt==j)
									break;
				}

				if(cnt==j)
									break;

				}
				
			
		
		
	}

	return 0;
}