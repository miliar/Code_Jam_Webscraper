#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

int main () {
	string line;
	int noOfCase,array[100][100];
	char tempChar;
	  
	ifstream myfile ("B-large.in");
	if (myfile.is_open())
	{   
		ofstream myfileOut;
		myfileOut.open("output.out");
		getline(myfile,line);
		
		istringstream(line) >> noOfCase;
		
		for(int k=0;k<noOfCase;k++)
		{
			int N,M;
			getline(myfile,line);
			istringstream(line) >> N>>M;
			
			int rowmax[100]={0}, colmax[100]={0};
			
			for(int i=0;i<N;i++)
			{
				getline(myfile,line);
				int pos=0;			
				
				for(int j=0;j<M;j++)
				{	
					int temp;
					istringstream(line) >>temp;
					if (j!=M-1)
					{
						pos=line.find(" ");
						line=line.substr(pos+1);
					}
					
					if (temp>rowmax[i])
						rowmax[i]=temp;
					if (temp>colmax[j])
						colmax[j]=temp;
						
					array[i][j]=temp;					
				}				
			}
			
			bool valid=true;
			for(int i=0;i<N;i++)
			{
				for(int j=0;j<M;j++)
				{
					if((array[i][j]!=rowmax[i])&&(array[i][j]!=colmax[j]))
					{
						valid=false;
						break;
					}
				}
				if (!valid)
					break;
			}
			
			if (valid)
			{
				cout<<"Case #"<<k+1<<": "<<"YES"<<endl;			
				myfileOut<<"Case #"<<k+1<<": "<<"YES"<<endl;
			}
			else
			{
				cout<<"Case #"<<k+1<<": "<<"NO"<<endl;			
				myfileOut<<"Case #"<<k+1<<": "<<"NO"<<endl;
			}
		}
		
		myfileOut.close();				
		myfile.close();
	}
	else cout << "Unable to open file";
	
	return 0;
}