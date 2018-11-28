#include <iostream>
using namespace std;

int main() {
int i,j;
long int k;
i=j=k=0;
int T;
long int N;
long int res[100];
int dig[10];
long int num,temp;
int cnt=0;

cin>>T;

for(i=0;i<T;i++)
{
	cin>>N;
	for(int l=0;l<10;l++)
		dig[l]=0;
	cnt=0;

	for(j=1;j<=10000000;j++)
	{
		num=j*N;
		temp=num;
		while(num!=0)
		{
			k=num%10;
			if(dig[k]!=1)
			{
				dig[k]=1;
				cnt++;
			}
			num=num/10;
		}
		if(cnt==10)
		{
			res[i]=temp;
			break;
		}


	}
	if(cnt!=10)
	{
		res[i]=0;
	}

}
for(i=0;i<T;i++)
{
	if(res[i]!=0)
	cout<<"Case #"<<i+1<<": "<<res[i]<<"\n";
	else
		cout<<"Case #"<<i+1<<": INSOMNIA\n";
}

	return 0;
}

