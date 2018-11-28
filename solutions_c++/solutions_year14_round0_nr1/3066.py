#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main () {
	string line;
	int noOfCase,array1[4][4],array2[4][4];
	
	  
	ifstream myfile ("A-small-attempt0.in");
	if (myfile.is_open())
	{   
		ofstream myfileOut;
		myfileOut.open("output.out");
		getline(myfile,line);
		
		istringstream(line) >> noOfCase;
		
		for(int k=0;k<noOfCase;k++)
		{
			int ans1,ans2;
			int no_of_match,sol;
			getline(myfile,line);
			istringstream(line)>>ans1;

			for(int i=0;i<4;i++){
				getline(myfile,line);
				istringstream(line)>>array1[i][0]>>array1[i][1]>>array1[i][2]>>array1[i][3];
			}
			
			getline(myfile,line);
			istringstream(line)>>ans2;
			
			for(int i=0;i<4;i++){
				getline(myfile,line);
				istringstream(line)>>array2[i][0]>>array2[i][1]>>array2[i][2]>>array2[i][3];
			}
			no_of_match=0;
			for(int p=0;p<4;p++)
			{
				for(int q=0;q<4;q++)
				{
					if (array1[ans1-1][p]==array2[ans2-1][q])
					{
						sol=array1[ans1-1][p];
						no_of_match++;
					}
				}
			}
			
			if (no_of_match==1)
			{
				cout<<"Case #"<<k+1<<": "<<sol<<endl;			
				myfileOut<<"Case #"<<k+1<<": "<<sol<<endl;
			}
			if (no_of_match>1)
			{
				cout<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;			
				myfileOut<<"Case #"<<k+1<<": "<<"Bad magician!"<<endl;
			}
			if (no_of_match==0)
			{
				cout<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;			
				myfileOut<<"Case #"<<k+1<<": "<<"Volunteer cheated!"<<endl;
			}
		}
		
		myfileOut.close();				
		myfile.close();
	}
	else cout << "Unable to open file";

	return 0;
}