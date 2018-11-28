#include <iostream>
#include <cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

bool check(int a[])
{
	int i;
	for(i=0;i<=9;i++)
		if(a[i]==0)
			return true;
	return false;
}
int main() {
    char pri[100],com[10]="Case #";
    FILE *fp;
	int t,a[10],d,tc;
	long long i,n,nc;
    char tmp[100],tmp1[100];
	cin>>t;
	tc=1;
	fp=fopen("out.txt","a");
	while(t--)
	{
		cin>>n;
		for(i=0;i<=9;i++)
			a[i]=0;
		i=1;
            strcpy(pri,com);
		if(n!=0)
		{
			while(check(a))
			{
				nc=n*i;
				while(nc!=0)
				{
					d=nc%10;
					a[d]=1;
					nc=nc/10;
				}
				i++;
			}
            ltoa(tc,tmp,10);
            ltoa((n*(i-1)),tmp1,10);
            strcat(pri,tmp);
            strcat(pri,": ");
            strcat(pri,tmp1);
            strcat(pri,"\n");
			cout<<"Case #"<<tc<<": "<<n*(i-1)<<endl;
			fprintf(fp,pri);
		}
		else
        {
            ltoa(tc,tmp,10);
            strcat(pri,tmp);
            strcat(pri,": INSOMNIA\n");
            fprintf(fp,pri);
            cout<<"Case #"<<tc<<": INSOMNIA"<<endl;
        }
		tc++;
	}
	fclose(fp);
	return 0;
}
