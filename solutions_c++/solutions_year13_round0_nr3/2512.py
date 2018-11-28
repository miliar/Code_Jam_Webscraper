#include<stdio.h>
#include<math.h>
#include<set>
#include<vector>
#include<algorithm>
#include<time.h>
#define LL long long
using namespace std;
set<LL> S;
set<LL>::iterator it;
vector<LL> V;
LL k[20];
int main()
{
	//freopen("C-large-1.in","r",stdin);
	//freopen("C-large-1.txt","w",stdout);
    LL a,b,c,d,e,f,g,n,s,t;
	for(a=1,k[0]=1;a<15;a++)
		k[a]=k[a-1]*10;
	for(a=1;a<10;a++)
	{
		S.insert(a);
    	S.insert(a*k[1]+a);
    }
    for(a=1;a<10;a++)
        for(b=0;b<10;b++)
        {
        	S.insert(a*k[2]+b*k[1]+a);
			S.insert(a*k[3]+b*k[2]+b*k[1]+a);
		}
	for(a=1;a<10;a++)
		for(b=0;b<10;b++)
			for(c=0;c<10;c++)
			{
				S.insert(a*k[4]+b*k[3]+c*k[2]+b*k[1]+a);
				S.insert(a*k[5]+b*k[4]+c*k[3]+c*k[2]+b*k[1]+a);
			}
	for(a=1;a<10;a++)
		for(b=0;b<10;b++)
			for(c=0;c<10;c++)
				for(d=0;d<10;d++)
				{
					S.insert(a*k[6]+b*k[5]+c*k[4]+d*k[3]+c*k[2]+b*k[1]+a);
					S.insert(a*k[7]+b*k[6]+c*k[5]+d*k[4]+d*k[3]+c*k[2]+b*k[1]+a);
				}
	for(a=1;a<10;a++)
		for(b=0;b<10;b++)
			for(c=0;c<10;c++)
				for(d=0;d<10;d++)
					for(e=0;e<10;e++)
					{
						S.insert(a*k[8]+b*k[7]+c*k[6]+d*k[5]+e*k[4]+d*k[3]+c*k[2]+b*k[1]+a);
						S.insert(a*k[9]+b*k[8]+c*k[7]+d*k[6]+e*k[5]+e*k[4]+d*k[3]+c*k[2]+b*k[1]+a);
					}
	for(a=1;a<10;a++)
		for(b=0;b<10;b++)
			for(c=0;c<10;c++)
				for(d=0;d<10;d++)
					for(e=0;e<10;e++)
						for(f=0;f<10;f++)
						{
							S.insert(a*k[10]+b*k[9]+c*k[8]+d*k[7]+e*k[6]+f*k[5]+e*k[4]+d*k[3]+c*k[2]+b*k[1]+a);
							S.insert(a*k[11]+b*k[10]+c*k[9]+d*k[8]+e*k[7]+f*k[6]+f*k[5]+e*k[4]+d*k[3]+c*k[2]+b*k[1]+a);
						}
	for(a=1;a<10;a++)
		for(b=0;b<10;b++)
			for(c=0;c<10;c++)
				for(d=0;d<10;d++)
					for(e=0;e<10;e++)
						for(f=0;f<10;f++)
							for(g=0;g<10;g++)
							{
								S.insert(a*k[12]+b*k[11]+c*k[10]+d*k[9]+e*k[8]+f*k[7]+g*k[6]+f*k[5]+e*k[4]+d*k[3]+c*k[2]+b*k[1]+a);
								S.insert(a*k[13]+b*k[12]+c*k[11]+d*k[10]+e*k[9]+f*k[8]+g*k[7]+g*k[6]+f*k[5]+e*k[4]+d*k[3]+c*k[2]+b*k[1]+a);
							}
	for(it=S.begin();it!=S.end();it++)
		if(S.find((*it)*(*it))!=S.end())
			V.push_back((*it)*(*it));
	scanf("%lld",&n);
	for(a=0;a<n;a++)
	{
		scanf("%lld%lld",&b,&c);
		printf("Case #%lld: %lld\n",a+1,upper_bound(V.begin(),V.end(),c)-lower_bound(V.begin(),V.end(),b));
	}
	return 0;
}
/* In lagre case 1, time = 1 min, they have 39 number 
1
4
9
121
484
10201
12321
14641
40804
44944
1002001
1234321
4008004
100020001
102030201
104060401
121242121
123454321
125686521
400080004
404090404
10000200001
10221412201
12102420121
12345654321
40000800004
1000002000001
1002003002001
1004006004001
1020304030201
1022325232201
1024348434201
1210024200121
1212225222121
1214428244121
1232346432321
1234567654321
4000008000004
4004009004004

*/
