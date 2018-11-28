#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]){
	ifstream in(argv[1],ios::in);
	ofstream out("output",ios::out);

	int cases;
	in>>cases;
	int count=0;
	while(count<cases)
	{	int cards[2][4];
		int row[2];
		in>>row[0];
		int card[4][4];
		for(int i=0; i<4; i++)
			for(int j=0; j<4;j++)
	 	        {   
			      in>>card[i][j];
                        }
		
		in>>row[1];
		for(int i=0;i<4;i++)
		{   cards[0][i]=card[row[0]-1][i];
			
		}
		
		for(int i=0; i<4; i++)
			for(int j=0; j<4;j++)
	 	        {   
			      in>>card[i][j];
                        }
		for(int i=0;i<4;i++)
		{   cards[1][i]=card[row[1]-1][i];
		}
		int count1=0;
		int cd[4];
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				{ 
					if(cards[0][i]==cards[1][j]){count1++;cd[count1-1]=cards[0][i];}
				}
					

		if(count1==0)out<<"Case #"<<(count+1)<<": Volunteer cheated!"<<endl;
		if(count1==1)out<<"Case #"<<(count+1)<<": "<<cd[0]<<endl;
		else if(count1>1)out<<"Case #"<<(count+1)<<": Bad magician!"<<endl;

		count++;
}

}
		


		
		
