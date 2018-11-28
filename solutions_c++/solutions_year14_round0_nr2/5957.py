#include <cstdio>

int T;
double Xd, Cd, Fd, ans;
double D2=double(2);

double getvalue(int n) //u(n+1)-u(n)
{
	return Xd/(D2+double(n+1)*Fd) + Cd/(D2+double(n)*Fd) - Xd/(D2+double(n)*Fd);
}

int main()
{
	FILE *fp;
	FILE *fout;
	fp=fopen("boda", "r");
	fout=fopen("boda2", "w");
	fscanf(fp, "%d", &T);
	for(int i=0; i<T; i++)
	{
		fscanf(fp, "%lf %lf %lf", &Cd, &Fd, &Xd);
		/*int nlow=0, nhigh=1000000000, n;
		bool found=false;
		while(found==false)
		{
			n=(nlow+nhigh)/2;
			printf("%d %d %d %d %lf %lf\n", i, n, nlow, nhigh, getvalue(n), getvalue(n+1));
			if(n==nlow && getvalue(n)>=0) //correct value is nlow
				found=true;
			else if(nhigh = nlow+1 && getvalue(nhigh-1)<0 && getvalue(nhigh)>=0)
				n=nhigh;
			else if(getvalue(n-1)<0 && getvalue(n)>=0)
				found=true;
			else if(getvalue(n)<0) //descending part, use more farms
				nlow=n;
			else if(getvalue(n)>0) //ascending part, use less farms
				nhigh=n;
		}
		
		ans=Xd/D2;
		if(n!=0)
			for(int j=0; j<n; j++)
				ans+=getvalue(j);*/
		ans=Xd/D2;
		bool found=false;
		for(int j=0; !found; j++)
		{
			double temp=getvalue(j);
			if(temp<0)
				ans+=temp;
			else
				found=true;
		}
		fprintf(fout, "Case #%d: %.7lf\n", i+1, ans);
	}
	return 0;
}

