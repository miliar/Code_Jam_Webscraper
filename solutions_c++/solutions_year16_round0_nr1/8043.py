#include<iostream>
#include <fstream>
using namespace std;
int main()
{
	int n,i=0,j=0,k;
	int check[10];
	int cal=0,cal2=0,cal3=0,succ;
	ifstream inFile("A-small-attempt0.in");
	ofstream outFile("output.txt");
	cin>>n;
	//inFile>>n;
	for(i=1;i<=n;i++)
	{
		cin>>cal;
		//inFile>>cal;
		for(j=0;j<=9;j++)
		{
			check[j]=0;
		}
		j=1;
		if(cal==0) cout<<"Case #"<<i<<": INSOMNIA"<<endl;
			
		//if(cal==0) outFile<<"Case #"<<i<<": INSOMNIA"<<endl;
		else
		{
			while(1)
			{
				cal2=cal*j;
				while(1)
				{
					check[cal2%10]=1;
					if(cal2<10)break;
					cal2=cal2/10;
				}
				succ=0;

				for(k=0;k<=9;k++)
				{
					if(check[k]==0)
					{
						succ=1;
						break;
					}
				}
				if(succ==0)
				{
					cout<<"Case #"<<i<<": "<<(cal*j)<<endl;
					//outFile<<"Case #"<<i<<": "<<(cal*j)<<endl;
					break;
				}
				j++;
			}
		}
	}
	
	outFile.close();
    inFile.close();

	return 0;
}