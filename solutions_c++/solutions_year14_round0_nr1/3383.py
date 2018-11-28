#include<iostream>
#include <string>
#include<fstream>
#include<ostream>
#include<vector>
#include<algorithm>
#include<set>
#include<deque>
#include<map>
#include<math.h>
using namespace std;

#define InputOutputToFile

int main(void)
{
#ifdef InputOutputToFile
	
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 
#endif

	int run = 0;
	cin>>run;
	int cs = 1;

	int arr1[4][4];
	int arr2[4][4];

	int ans1=0;
	int ans2=0;
	int matchPos1=-1;
	int matchPos2=-1;
	int matchCount=0;

	int i=0,j=0;
	//resets the arrays
	for(i=0;i<4;i++)
		for(j=0;j<4;j++)
			arr1[i][j]=arr2[i][j]=0;

	bool itrFlg = false;
	while(run--)
	{
		if(itrFlg)
		{
			ans1=0;
			ans2=0;
			matchPos1=-1;
			matchPos2=-1;
			matchCount=0;
			//resets the arrays
			for(i=0;i<4;i++)
				for(j=0;j<4;j++)
					arr1[i][j]=arr2[i][j]=0;
			cout<<endl;
		}
		itrFlg = true;

		cin>>ans1;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>arr1[i][j];

		cin>>ans2;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>arr2[i][j];
	
		//converting them to point correct row in arrays
		ans1--;
		ans2--;

		//Match the rows
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				//cout<<"arr1["<<ans1<<"]["<<i<<"] ::"<<arr1[ans1][i]<<endl;
				//cout<<"arr2["<<ans2<<"]["<<j<<"] ::"<<arr2[ans2][j]<<endl;
				if(arr1[ans1][i] == arr2[ans2][j])
				{
					matchPos1=i;
					matchPos2=j;
					matchCount++;
				}
			}
		}

		if( matchCount>1 )
			cout<<"Case #"<<cs<<": "<<"Bad magician!";
		else if( matchCount == 0 )
			cout<<"Case #"<<cs<<": "<<"Volunteer cheated!";
		else if( matchCount==1 && (arr1[ans1][matchPos1] == arr2[ans2][matchPos2]) )
			cout<<"Case #"<<cs<<": "<<arr1[ans1][matchPos1];

		cs++;

		//logs-start
		/*
		cout<<"Answer one :: "<<ans1<<endl;
		cout<<"arr1 values\n";
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cout<<arr1[i][j];
				if(j<3)
					cout<<" ";
			}
			cout<<endl;
		}
		cout<<"Answer two :: "<<ans2<<endl;
		cout<<"arr2 values\n";
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cout<<arr2[i][j];
				if(j<3)
					cout<<" ";
			}
			cout<<endl;
		}*/
		//logs-end
				
	}

	return 0;
}