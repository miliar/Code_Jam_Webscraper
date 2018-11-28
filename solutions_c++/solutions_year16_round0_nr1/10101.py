#include<iostream>
using namespace std;
int check(int c[])
{
	for(int i=0;i<=9;i++)
	{
		if(c[i]==0)
			return 1;
	}
	return 0;
}
int main()
{
	int t;
//	ifstream fin;
//	ofstream fout;
//	fin.open("A-small-attempt0.in");
//	fout.open("output1.txt");
	cin>>t;
	int x=t;
	while(t--)
	{
		int a[10]={0};
		int n,sum,i=0;
		cin>>n;
		while(check(a)==1&&i<=100)
		{
			i++;
			sum=i*n;
			while(sum!=0)
			{
				int d;
				d=sum%10;
				a[d]=true;
				sum=sum/10;
			}
		}
		if(i==101)
		cout<<"Case"<<" "<<"#"<<x-t<<":"<<" "<<"INSOMNIA"<<endl;
		else
			cout<<"Case"<<" "<<"#"<<x-t<<":"<<" "<<i*n<<endl;
	}
}
