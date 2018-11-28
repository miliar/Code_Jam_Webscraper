#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i,n,D,maxima,temp1,temp2,temp,A[1012],time,j=0,k;
	double A1,A2;
	cin>>t;
	int res;
	while(t--)
	{
		j++;
		cin>>D;
		maxima=0;
		for(i=0;i<D;i++)
		{
			cin>>A[i];
			if(A[i]>maxima)
				maxima=A[i];
		}
		time=maxima;
		res=time;
		for(i=1;i<maxima;i++)
		{
			res=0;
			for(k=0;k<D;k++)
			{
				if(A[k]>i)
				{
					A1=(double)A[k];
					A2=(double)i;
					temp=ceil(A1/A2)-1;
					res=res+(ceil((double)A[k]/(double)i)-1);
				}
			}
			res=res+i;
			if(res<time)
				time=res;
		}
		cout<<"Case #"<<j<<": "<<time<<"\n";
	}
	return 0;
}