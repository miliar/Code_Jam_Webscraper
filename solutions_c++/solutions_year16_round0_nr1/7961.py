#include<iostream>
using namespace std;
struct test{
	bool t[10];
};
int main(){
	char *x;
	x=new char[10];
	test test;
	FILE *f,*g;
	f=fopen("C:\\Users\\hasee\\Downloads\\A-large.in","r");
	g=fopen("C:\\Users\\hasee\\Downloads\\A-large.out","w");
	fscanf(f,"%s",x);
	int t=0;
	while (!feof(f))
	{
		for (int i = 0; i < 10; i++)
			test.t[i]=0;
		long long int n,k;
		t++;
		fscanf(f,"%s ",x);
		n=atoi(x);
		k=n;
		int i=1;
		if (n==0)
		{
			fprintf(g,"Case #%d: INSOMNIA\n",t);
			i=100;
		}
		for (; i < 100; i++)
		{
			n=k;
			n*=i;
			while (n!=0)
			{
				test.t[n%10]=1;
				n/=10;
			}
			for (int j = 0; j < 10; j++)
			{
				if(test.t[j]==0)
					break;
				if (j==9)
				{
					fprintf(g,"Case #%d: %d\n",t,k*i);
					cout<<k*i;
					i=100;
				}
			}
			if (i==99)
			{
				fprintf(g,"Case #%d: INSOMNIA\n",t);
			}
		}
	}
	fclose(f);
	fclose(g);
	return 0;
};