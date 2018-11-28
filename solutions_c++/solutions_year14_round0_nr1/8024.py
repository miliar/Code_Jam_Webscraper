#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>


using namespace std;

int main(int argc, char **argv)
{
	ifstream input("input.in",ios::in);
    ofstream output("output.out", ios::out);
	
	//number of test cases
	int t;
	int fst, snd;
	int m1[4][4];
	int m2[4][4];
	
	input>>t;
	
	for(unsigned i=0; i<t; ++i){
		
		input>>fst;
		
		for(unsigned i=0;i<4;i++){
			input>>m1[i][0]>>m1[i][1]>>m1[i][2]>>m1[i][3];
			//scanf("%d %d %d %d\n",m1[i][0],m1[i][1],m1[i][2],m1[i][3]);
		}
			
		cout<<m1[1];
			
		input>>snd;
		
		for(unsigned i=0;i<4;i++){
			input>>m2[i][0]>>m2[i][1]>>m2[i][2]>>m2[i][3];
			//scanf("%d %d %d %d\n",m2[i][0],m2[i][1],m2[i][2],m2[i][3]);
		}
		
		cout<<m2[1];	
			
		}
		
		int found=0;
		int sol;
		for(unsigned i=0;i<4;i++)
			for(unsigned j=0;j<4;j++)
				if(m1[fst][i]==m2[snd][j]){
						found++;
						sol=m1[fst][i];
				}
		
		if(found==0)
			output<<"Volunteer cheated!"<<"\n";
		else if(found==1)
			output<<sol;
		else
			output<<"Bad magician!"<<"\n";
			
		}
		
		
	}
	
	return 0;
}
