#include <iostream>
#include<cstdio>
using namespace std;

int main() {
	int t,z,j,i;
	double c,f,x,temp1,temp2,ans;
	FILE *fp;
	FILE *fp2;
	fp2=fopen("i4.txt","r");
	fp=fopen("s4.txt","w");
	//cin>>t;
	fscanf(fp2,"%d",&t);
	//t=100;
	//cout<<t;
	for(i=0;i<t;i++)
	{
	    fscanf(fp2,"%lf%lf%lf",&c,&f,&x);
	    //cout<<c<<f<<x;
		//cin>>c>>f>>x;
		z=1;
		temp1=x/2;
		temp2=(c/2)+(x/(2+f));
		while(1)
		{
			if(temp1>temp2)
			{
				z++;
				temp1=temp2;
				temp2=0;
				for(j=0;j<z;j++)
				{
					temp2+=(c/(2+j*f));
				}
				temp2+=(x/(2+(z*f)));
			}
			else
			{
				ans=temp1;
				break;
			}
		}
		fprintf(fp,"%s%d%s%.7f\n","Case #",i+1,": ",ans);
		//cout<<"Case #"<<i+1<<": ";
		//printf("%.7f\n",ans);
	}
	return 0;
}
