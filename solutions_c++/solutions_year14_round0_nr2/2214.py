#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin>>T;
	double C, F, X;
	for(int i=0; i<T; i++)
	{
		cin>>C>>F>>X;
		bool check=true;
		double sum, sum1;
		double k=1;
		sum=X/2;
		sum1=0;
		double temp;
		while(check)
		{
			temp=X/(2+k*F);
			sum1+=C/(2+(k-1)*F);
			if(sum1+temp<sum)
				sum=sum1+temp;
			else
				check=false;
			k++;
		}
		cout<<"Case #"<<i+1<<": ";
		printf("%.10f\n", sum);
	}
	//system("pause");
	return 0;
}