#include<bits/stdc++.h>
using namespace std;
long long  a[11][17];
int prime[1000001];
int main()
{
	int t1;
	scanf("%d",&t1);
	while(t1--){
	a[0][0]=0;
	a[1][0]=1;
	for(int i=2;i<=10;i++)
	{
		a[i][0]=1;
		for(int j=1;j<17;j++)
		{
			a[i][j] = a[i][j-1]*i;
			
		}
	}
	
	int n,z;
	scanf("%d %d",&n,&z);
	
	int cnt=0;
	vector<vector<long long> >v;
	for(int i=0;i<=(1<<14)-1;i++)
	{
		
		vector<long long>v2;

		int arr[16];
		long long val = a[2][15]+1+i*2;
		
		int c2 = 0;
		int val2 = a[2][15];
		long long r2 = val,a2s=0;
		
		for(int j=0;j<=15;j++ )
		{
			arr[j] = val/val2;
			val = val%val2;
			val2/=2;
			//printf("%d ",arr[j]);
			a2s = a2s * (long long)10 +(long long) arr[j];
		}
		v2.push_back(a2s);
		//printf("\n");
		val = r2;
		int div2 ;
		int f=0;
		long long k1 = 2;
				while(k1*k1<=r2)
				{
					if(r2%k1==0)
					{
						f=1;
						div2=k1;
						break;
					}
					k1++;
				}

		if(f){
			v2.push_back(div2);f=0;
		}
		else {//printf("KK se na ho paya base=%d %d %lld %lld\n",i,2,r2,k1);
		continue;}
	    		//printf("%d\n",i);

		int check = 0;
		for(int j=3;j<=10;j++)
		{
		//	printf("%d %d\n",j,i);
			long long int po = 1;
			long long int res = 0;
			for(int k = 15 ; k>=0 ; k--)
				{ 
					if(arr[k]==1)
						res = res+ po;
					po = po * (long long)j;

				 }
				
				 int div21,f1=0;
				long long k = 2;
				while(k*k<=res)
				{
					if(res%k==0)
					{
						f1=1;
						div21=k;
						break;
					}
					k++;
				}
			if(f1) {check = 1;v2.push_back(k);}
			else {check = 0;//printf("KK se na ho paya base=%d %d %lld %lld\n",i,j,res,k);
			break;}
			
		}
		
		if(check==1) { 
			 cnt++; v.push_back(v2);
			
		}
		if(cnt==z)
			break;
		

	}
	if(cnt==z)
		{printf("Case #%d:\n",1);
	for(int i=0;i<z;i++)
	{
		for(int i1 = 0 ;i1 <10;i1++) printf("%lld ",v[i][i1]);
			printf("\n");
	}
}
	
	}return 0;

}