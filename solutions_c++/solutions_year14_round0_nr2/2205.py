#include<iostream>
#include<cstdio>
#include <vector>
using namespace std;

int t;
double c,f,x;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	cin>>t;
	for(int g=0;g<t;g++)
	{
		cout<<"case #"<<g+1<<": ";
		cin>>c>>f>>x;
		double sum=0;
		double min=x/2;
		double tmp;
		int k=1;
		bool check=true;
		while(check)
		{
			sum+=c/(2+(k-1)*f);
			tmp=((x/(2+k*f))+sum);
			if(min>tmp)min=tmp;
			else check=false;
			k++;
		}
		printf("%.10lf\n",min);
	}
	return 0;
}