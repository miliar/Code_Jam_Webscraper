#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

main()
{int T;

freopen("D-large.in","r",stdin);
scanf("%d",&T);	
freopen ("Q4Ishan.txt","w",stdout);
for(int k=1;k<=T;++k)
{     printf("Case #%d: ",k);

	int N;
	scanf("%d",&N);
	double A[N];
	int t1=0;
	int t2=0;
	double B[N];
	for(int i=0;i<N;++i)
	{scanf("%lf",&A[i]);
	}
	for(int i=0;i<N;++i)
	{scanf("%lf",&B[i]);
	}
	vector <double> Av(A,A+N);
	vector <double> Bv(B,B+N);
	sort(Bv.begin(),Bv.end());
	sort(Av.begin(),Av.end());
	for(int i=0;i<N;++i)
	{A[i]=Av[i];
	B[i]=Bv[i];
	
	}
	int tot;
	int ctr=0;
	int end=N-1;
	//for deceitful war
	for(tot=0;tot<N;++tot)
	{if(A[t1]>B[end])
	{ctr+=N-tot;
	break;
	}
	if(A[t1]>B[t2])
		{++ctr;
		++t1;
		++t2;
		}
	else
	{++t1;
	--end;
	}
	}
printf("%d ",ctr);

	
	//for War
	int i,j;
	i=0;
	j=0;
	int c=0;
	while(1)
	{if(j==N)
		break;
	if(A[i]>B[j])
		++j;
	else
	{++i;
	++j;
	++c;
	}
	}
	printf("%d\n",N-c);
}
}
