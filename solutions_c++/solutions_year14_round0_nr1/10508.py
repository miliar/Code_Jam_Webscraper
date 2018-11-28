#include<fstream>

using namespace std;
ifstream cin("1.in");
ofstream cout("1.out");
int arr[100][100];
int rr[100][100];
int rra[100];
int rar[100];
int arrr[100];
int ar[100];
int main()
{
	int a,b,c,d=0,f=1,e;
	cin>>a;
	for(int i=1;i<=a;i++)
	{
		cin>>b;
		for(int l=1;l<=4;l++)
		{
			for(int j=1;j<=4;j++)
			{
				cin>>arr[l][j];
				if(l==b)
				rra[j]=arr[l][j];
			}
		}
		cin>>c;
		for(int l=1;l<=4;l++)
		{
			for(int j=1;j<=4;j++)
			{
				cin>>rr[l][j];	
				if(l==c)
				rar[j]=rr[l][j];
			}
		}
		for(int k=1;k<=4;k++)
		{
			for(int m=1;m<=4;m++)
			{
				if(rra[k]==rar[m])
				{
					d++;	
					e=rra[k];
					rar[m]=0-m;
				}
			}
		}
		arrr[i]=d;
		if(d==1)
		{
			ar[f]=e;
			f++;
		}
		d=0;
	}
	f=1;
	for(int i=1;i<=a;i++)
	{
		if(arrr[i]==1)
		{
			cout<<"Case #"<<i<<": "<<ar[f]<<endl;
			f++;
		}
		else if(arrr[i]==0)
		cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
		else
		cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
	}
	return 0;
}
