#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("A-large.in");
	fout.open("out.txt");
		
	int cases=0,v=1;
	fin>>cases;
	while(cases>=1 && cases<=100)
	{
		int n;
		fin>>n;
		if(n==0)
		{
			fout<<"Case #"<<v<<": INSOMNIA"<<endl;
		}
		else
		{
			int i=2,prod,yes=0;
			int arr[10]={0,1,2,3,4,5,6,7,8,9};
			prod=n;
					
			while(yes<=9)
			{
			
				while(prod!=0)
				{
					for(int a=0;a<10;a++)
					{
						if(arr[a]==prod%10)
						{
							yes++;
							arr[a]=-1;
							break;
						}
					}
					prod=prod/10;
				}
			
				prod=i*n;
				i++;
			}
			fout<<"Case #"<<v<<": "<<n*(i-2)<<endl;
		
		}
		cases--;
		v++;
	}
}

