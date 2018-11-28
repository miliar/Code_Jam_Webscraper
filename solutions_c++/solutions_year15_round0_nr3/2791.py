#include<iostream>
using namespace std;
#define P_1 1
#define P_I 2
#define P_J 3
#define P_K 4
#define N_1 -1
#define N_I -2
#define N_J -3
#define N_K -4

int MTAB[4][4]=
{
	1,2,3,4,
	2,-1,4,-3,
	3,-4,-1,2,
	4,3,-2,-1
};

int multiply(int a,int b)//a*b
{
	int sign=1;
	int ma=a,mb=b;
	int ans;
	if(ma<0) {ma=-ma;sign*=-1;}
	if(mb<0) {mb=-mb;sign*=-1;}
	ans=MTAB[ma-1][mb-1];

	return sign*ans;
}
int divide(int a,int b)//b^-1 * a   i.e b*res=a
{
	int x;
	int sign;
	for(int i=1;i<=4;i++)
	{	sign=1;
		x=multiply(b,i);
		if(x<0) {x=-x;sign*=-1;}
		if(a<0) {a=-a;sign*=-1;}
		if(x==a) {return sign*i;}
	}
}
int main()
{


	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		long X,L;
		cin>>L>>X;
		char str[20001];
		cin>>str;
		int list[20000];
		for(int j=0;j<L;j++)
			{
				if(str[j]=='i') list[j]= 2;
				else if(str[j]=='j') list[j]= 3;
				else if(str[j]=='k') list[j]= 4;
				
			}
		int multi[20001];
		multi[0]=1;
		for(int j=1;j<=L;j++)
			multi[j]=multiply(multi[j-1],list[j-1]);

		int x[4]={1,1,1,1},xl;

		switch(multi[L])
		{
			case N_I:	x[1]=-1;x[3]=-1;
			case P_I:	x[1]*=P_I;x[2]*=N_1;x[3]*=N_I;x[0]*=P_1;xl=4;
						break;
			case N_J:	x[1]=-1;x[3]=-1;
			case P_J:	x[1]*=P_J;x[2]*=N_1;x[3]*=N_I;x[0]*=P_1;xl=4;
						break;
			case N_K:	x[1]=-1;x[3]=-1;
			case P_K:	x[1]*=P_I;x[2]*=N_1;x[3]*=N_I;x[0]*=P_1;xl=4;
						break;
		
			case N_1 :	 x[1]=N_1;x[0]=P_1;xl=2;
							break;
			case P_1 :	 x[1]=P_1;xl=1;
							break;

		}	
		//cout<<"\n>";
		//for(int j=0;j<=L;j++)
		//	cout<<multi[j]<<' ';
		//cout<<endl;

		int flag=0;
		int cc=x[X%xl];
		if(cc==N_1)
		{
		for(int a=0;a<=L*X;a++)
		{
			for(int b=a;b<=L*X;b++)
			{
				int aa=multiply(x[(a/L)%xl],multi[a%L]);
				int bb=multiply(x[(b/L)%xl],multi[b%L]);
				if(aa==P_I && bb==P_K) {flag=1;break;}
			}
		if(flag) break;
		}

		}
		cout<<"Case #"<<i+1<<": ";
		if(flag) cout<<"YES\n";
		else cout<<"NO\n";
	/*	
		int y[3][4];
		
		for(int j=0;j<3;j++)
		{
			y[j][0]=divide(j+1,x[xl-1]);
			for(int k=1;k<xl;k++)
				y[j][k]=divide(j+1,x[k-1]);

		}
		int flag=0;
		int A[3][4][10001];	//a,b,c | xl   | list
		int Al[3][4]={0}; 
		for(int k=0;k<3;k++)
		{
			for(int j=0;j<xl;j++)
				for(int z=0;z<=L;z++)
				if(y[k][j]==multi[z])
				{
					A[k][j][Al[k][j]++]=multi[j];
						
				}
				
		}
		
*/

	}

	return 0;
}