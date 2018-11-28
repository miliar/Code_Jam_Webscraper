#include<cstdio>
#include<iostream>
#include<cmath>
#include<string>

using namespace std;

int isPalin(int j);
void main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("c_small.out","w",stdout);

	int T,A,B;
	cin>>T;
	for(int i=0;i!=T;++i)
	{
		int count=0;
		cin>>A>>B;
		for(int j=A;j!=B+1;++j)
		{

			if(isPalin(j))
			{
				double temp1;
				int temp2;
				temp1=sqrt(j);
				temp2=temp1;
				if(!(temp1>temp2))
				{
					if(isPalin(temp1))
					{
						++count;
					}
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}

}
int isPalin(int j)
{
	char* num;
	num = new char[10];
	memset(num,NULL,sizeof(num));
	itoa(j,num,10);
	int size=strlen(num);
	int k=0;
	for(k=0;k!=size;++k)
	{
		if(num[k]!=num[size-k-1])
			return 0;
	}
	return 1;
}