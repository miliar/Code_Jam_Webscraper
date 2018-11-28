#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	ofstream myfile;
  	myfile.open ("C:\\Users\\jat-wad\\Desktop\\output_yo.txt");
	  int t,k=1;
	cin>>t;
	while(t--)
	{
		
	int i,j,ans=0,a,b,x[5][5],y[5][5];
	cin>>a;
	
  //ofstream outfile ("Desktop\\output.txt");
	for(i=1;i<5;i++)
	{
		for(j=1;j<5;j++)
		{
			cin>>x[i][j];
		}
	}
	cin>>b;
	for(i=1;i<5;i++)
	{
		for(j=1;j<5;j++)
		{
			cin>>y[i][j];
		}
	}

	
	int count=1;
	int req;
	while(count<5)
	{
		for(i=1;i<5;i++)
		{
			
			if(x[a][count]==y[b][i])
			{
				
				req=x[a][count];
				ans++;
			}
		}
		count++;
	}

	//myfile << "Writing this to a file.\n";
	myfile << "Case #"<<k<<": ";
		
		if(ans==1)
		{
			myfile<<req<<"\n";//<<endl;
		}
		else if(ans==0)
		{
			myfile << "Volunteer cheated! \n";//<<endl;
		}
		else if(ans>1)
		{
			myfile << "Bad magician! \n";//<<endl;
		}
		k++;
		
	}

myfile.close();
}
