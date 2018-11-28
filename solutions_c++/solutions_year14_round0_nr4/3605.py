#include<iostream>
#include<algorithm>

using namespace std;



int dWar(long double a[],long double b[],int N)
{
	long double  a1[1001];
	long double  b1[1001];

	copy(a,a+N,a1);
	copy(b,b+N,b1);

	sort(a1,a1+N);
	sort(b1,b1+N);
	long double chk1=0;
	int count=N-1;
	int beg=0;
	int naomi=0;
	while(count>=0)
	{
		
	/*if(a[beg]>b[count])
		{
			naomi++;
			beg++;
			count--;
		}
	*/	
		
		
		//else
	//	{
		chk1=b[count]-0.000001;
		
				

		for(int i=0;i<N;i++)
		   {
			   if(a1[i]>b1[count])
			   {
				   a1[i]=0;
				   b1[count]=0;
				 naomi++;
				   break;
			   }
			 	 
		   }//for
		
		
		count--;
	}//while
	return naomi;
}


int war(long double a[],long double b[],int N)
{
	sort(b,b+N);
	sort(a,a+N);
	int naomi=0;
	for(int beg=0;beg<N;beg++)
	
		for(int i=0;i<N;i++)
		
			if(b[i]>a[beg])
			{
				b[i]=-1;
				naomi++;
				break;
			}
		
			naomi=N-naomi;
	
	return naomi;
}


void main()
{
	int T=0;
	int N=0;
	long double a[1001],b[1001];
	
	scanf("%d",&T);
	int count=0;
	for(int i=1;i<=T;i++)
	{
		scanf("%d",&N);
		count=N;
		for(int j=0;j<N;j++)
			cin>>a[j];

		
		for(int j=0;j<N;j++)
			cin>>b[j];
				
		int y = dWar(a,b,N);
		int z= war(a,b,N);
		cout<<"Case #"<<i<<": "<<y<<" "<<z<<endl;

	}


	//system("pause");
}