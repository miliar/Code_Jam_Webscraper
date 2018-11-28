#include<iostream>

using namespace std;
int maxi(int *a,int b)
{
	int max=0;
	for(int i=0;i<b;i++)
		if(a[i]>max)
			max=a[i];
	return max;
}

int func(int *v,int n)
{
	int v1[n];int v2[n+1];

	for(int i=0;i<n;i++)
	{
		v2[i]=v[i];
		if(v[i]>0)
		v1[i]=v[i]-1;
		else v1[i]=0;
	}

	int m=maxi(v,n);
	if(m==0)
		return 0;
	if(m==1)
		return 1;
	for(int i=0;i<n;i++)
	{
		if(v2[i]==m)
		{
			if(m==2) {v2[i]=1;v2[n]=1;}
			else if(m==3) {v2[i]=1;v2[n]=2;break;}
			else if(m==4) {v2[i]=2;v2[n]=2;break;}
			else if(m==5) {v2[i]=2;v2[n]=3;break;}
			else if(m==6) {v2[i]=3;v2[n]=3;break;}
			else if(m==7) {v2[i]=3;v2[n]=4;break;}
			else if(m==8) {v2[i]=4;v2[n]=4;break;}
			else if(m==9) {v2[i]=3;v2[n]=6;break;}
		}
	}

		int ans=(1+min(func(v1,n),func(v2,n+1)));
		return ans;
}

int main()
{
	int t,num=1;
	cin>>t;
	while(t--)
	{
		int d;
		cin>>d;
		int pan[d];

		for(int i=0;i<d;i++)
		{
			cin>>pan[i];
			//if(pan[i]>maximum)
				//maximum=pan[i];
		}
		int ans=func(pan,d);

		cout<<"Case #"<<num<<": "<<ans<<endl;
		num++;
	}
		return 0;
}
