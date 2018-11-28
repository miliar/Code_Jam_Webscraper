#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream f;
	f.open("C://Users//Abhishek//Desktop//Algorithm Coursera//A-small-attempt0.in");
	ofstream fo;
	fo.open("C://Users//Abhishek//Desktop//Algorithm Coursera//A-small-attempt0output.txt");
	int t;
	//cin>>t;
	f>>t;
	for(int k=1;k<=t;k++)
	{
		long long int n,n1,p,i,c=0;
		long long int a[100]={0};
		//cin>>n;
		f>>n;
		fo<<"Case #"<<k<<": ";
		//cout<<"Case #"<<k<<": ";
		if(n==0){
			fo<<"INSOMNIA"<<endl;
			//cout<<"INSOMNIA"<<endl;
		}
		else
		{
			i=1;
			while(true)
			{
				n1=n*i;
				while(n1>0)
				{
					p=n1%10;
					a[(char)(p+48)]++;
					n1/=10;
				}
				for(int j=48;j<=57;j++)
				{
					if(a[j]>=1)
						c++;
				}
				if(c==10)
					break;
				else
					c=0;
				i++;
			}
			fo<<n*i<<endl;
			//cout<<n*i<<endl;
		}
	}
	fo.close();
}
