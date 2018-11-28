#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>
#include <cassert>
using namespace std;

int n_matches(int a[4] , int b[4], int *ans)
{
	int count=0;

	for(int i=0; i<4 ;i++)
		for(int j=0;j <4; j++)
			if(a[i]==b[j]) { *ans = a[i];count++; }
	return count;
}
int main()
{
	ofstream outfile("output.txt");
	ifstream infile("input.txt");
	if(!infile)
		{
			cout<<"Could not open file for input...";
			return -1;
	}
	int n_cases;
	infile>>n_cases;
	vector<string> ans_string=vector<string>();
	
	ostringstream str;
	int arr1[4][4],arr2[4][4];

	for(int n=1; n<= n_cases; n++)
	{
		
		
		int choice1,choice2;
		infile>>choice1;
		
		for(int i=0;i<4;i++)
			for(int j=0; j<4; j++)
				infile>>arr1[i][j];


		infile>>choice2;
		
		for(int i=0;i<4;i++)
			for(int j=0; j<4; j++)
				infile>>arr2[i][j];
		
		int ch;
		int ans= n_matches(arr1[choice1-1], arr2[choice2-1],&ch);
		
		switch(ans)
		{
		case 1:
			//str.append("Case #").append(n);
			//ans_string.pushBack("Case #"+n+": "+ch+"\n");
			outfile<<"Case #"<<n<<": "<<ch<<endl;
			break;
		case 0:
			//ans_string.pushBack("Case #3: Volunteer cheated!\n");
			outfile<<"Case #"<<n<<": Volunteer cheated!"<<endl;
			break;
		default:
			//ans_string.pushBack("Case #2: Bad magician!\n");
			outfile<<"Case #"<<n<<": Bad magician!"<<endl;
		}
		
	}
	//outfile<<str.str();
	//cin.ignore();
	//int n;
	//cin>>n;
return 0;
}



