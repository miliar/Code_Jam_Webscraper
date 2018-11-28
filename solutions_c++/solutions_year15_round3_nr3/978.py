#include <iostream>
#include <algorithm>
#include <cstdio>
#include <string>
#include <cstdlib>
#include <vector>


using namespace std;

int val[100000];
int den[105];
int C,D,V;

int nod;

void build(int sum,int i)
{
	int j;
	
	if(i>=D || sum >=V)
	{
		if(sum>V)
			return;
//		printf("got sum %d\n",sum);
		if(sum>0 && sum<=V && !val[sum])
			nod++;
		val[sum]=1;
	}
	else	
		for(j=0;j<=C;j++)
			build(sum+den[i]*j,i+1);
	
}

void test()
{
	int i,j,mxval=0,ans=0;
	int myden[1005]={0};
	
	nod=0;
	
	cin>>C>>D>>V;
	
//	int den[D];
	for(i=0;i<D;i++)
	{
		cin>>den[i];
		mxval+=C*den[i];
		myden[den[i]]=1;
	}
/*	
	build(0,0);
	
	
	for(i=1;i<=V;i++)
	{
		printf("%d:%d,",i,val[i]);
	}
	
	printf("\nnod=%d\n",nod);
	*/
	
			for(i=1;i<=V;i++)
			val[i]=0;
	j=1;
	while(nod=0,build(0,0),nod<V)
	{
/*		for(i=1;i<=V;i++)
		{
			printf("%d:%d,  ",i,val[i]);
		}
		printf("\nnod=%d\n",nod);
*/		
		for(j=1;j<=V && val[j];j++);
			
		
		for(i=1;i<=V;i++)
			val[i]=0;
/*
		while(myden[j] && j<V && j<105)
			j++;
			*/
//		printf("\t\t\t%d is added\n",j);
//		myden[j]=1;
		den[D++]=j;
		ans++;
	}
/*	
	for(i=1;i<=V;i++)
	{
		printf("%d:%d,  ",i,val[i]);
	}

	printf("\nnod=%d\n",nod);
	printf("answer=%d\n",ans);
*/	cout<<ans;
}




int main()
{
//	test();
//	return 0;

	long long T,i;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cout<<"Case #"<<i<<": ";
		test();
		cout<<"\n";
	}
	return 0;
}
