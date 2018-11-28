#include <bits/stdc++.h>

using namespace std;

bool func(double x,double y)
{
	return(x>y);
}

int main()
{
	int T;
	cin>>T;
	for(int iter=1;iter<=T;iter++)
	{
		int N,res1=0,res2=0;
		cin>>N;
		double a[N],b[N];
		int mark[N],f=0,idx;
		memset(mark,0,sizeof(mark));
		for(int i=0;i<N;i++)	cin>>a[i];
		for(int i=0;i<N;i++)	cin>>b[i];
		sort(a,a+N,func);
		sort(b,b+N);
		for(int i=0;i<N;i++)
		{
			f=0;idx=-1;
			for(int j=0;j<N;j++)
			{
				if(idx==-1 && !mark[j])
				{
					idx=j;
				}
				if(b[j]>a[i] && !mark[j])
				{
					f=1;
					//cout<<a[i]<<" "<<b[j]<<endl;
					mark[j]=1;
					break;
				}
			}
			if(f==0)
			{
				//cout<<a[i]<<" "<<b[idx]<<endl;
				res1++;
				mark[idx]=1;
			}	
		}
		sort(a,a+N);
		sort(b,b+N,func);
		memset(mark,0,sizeof(mark));
		for(int i=0;i<N;i++)
		{
			f=0;idx=-1;
			for(int j=0;j<N;j++)
			{
				if(idx==-1 && !mark[j])
				{
					idx=j;
				}
				if(a[j]>b[i] && !mark[j])
				{
					f=1;
					res2++;
					//cout<<a[i]<<" "<<b[j]<<endl;
					mark[j]=1;
					break;
				}
			}
			if(f==0)
			{
				//cout<<a[i]<<" "<<b[idx]<<endl;
				//res1++;
				mark[idx]=1;
			}	
		}


		/*for(int i=0;i<N;i++)
		{
			if(a[i]>b[i])	res2++;
		}*/
		cout<<"Case #"<<iter<<": "<<res2<<" "<<res1<<endl;		
	}



}
