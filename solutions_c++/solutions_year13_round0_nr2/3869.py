#include <iostream>
#include <fstream>
#include <stdlib.h>     /* srand, rand */
#include <time.h>  

#define MAX 100
using namespace std;

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

//	FILE * input;
//	input = fopen("input.txt","r");
	 srand (time(NULL));
	int t;

	int n,m;
//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input>>t;// cout<<n<<endl;
	unsigned short a[MAX][MAX];
	for(int i=0;i<MAX;i++)
		for(int j=0;j<MAX;j++)
		{
			a[i][j]=0;
		}

	bool result=1;
	for(int k=0;k<t;k++)
	{
		input>>n>>m;
//		n=rand()%100+1;
//		m=rand()%100+1;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
			{
//				c=fgetc(input); cout<<c<<endl;
				input>>a[i][j]; //cout<<c<<endl;
//				a[i][j]=rand()%3+1;
				
			}
		}


		//cout<<"*********************************"<<k+1<<"****************************"<<endl;
		//for(int i=0;i<n;i++)
		//{
		//	for(int j=0;j<m;j++)
		//	{
		//		cout<<a[i][j]<<" "; //cout<<c<<endl;
		//		
		//	}
		//	cout<<endl;
		//}
		//cout<<endl<<endl;

		result=1;
		int N[MAX]={0},M[MAX]={0};
		int temp=0;
		for(int i=0;i<n;i++)
		{
			temp=0;
			for(int j=0;j<m;j++)
				if(a[i][j]>temp)
					temp=a[i][j];
			N[i]=temp;// cout<<"N[i]= "<<temp<<endl;
		}
		for(int j=0;j<m;j++)
		{
			temp=0;
			for(int i=0;i<n;i++)
				if(a[i][j]>temp)
					temp=a[i][j];
			M[j]=temp;// cout<<"M[i]= "<<temp<<endl;
		}

		for(int i=0;i<n;i++)
		{
			if(!result)
				break;
			for(int j=0;j<m;j++)
				if(a[i][j]<min(N[i],M[j]))
				{
					result = 0;
					break;
				}
		}

		output<<"Case #"<<k+1<<": "; 
		if(result)
			output<<"YES";
		else
			output<<"NO";
		output<<endl;
	}
//	fclose(input);
	input.close();
	output.close();
//	system("pause");
	return 0;
}
