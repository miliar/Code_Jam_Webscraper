#include <iostream>
#include <conio.h>
#include <string>
#include <fstream>


using namespace std;


void main()
{
	
	std::freopen("output_MagicTrick.txt", "w", stdout);
	ifstream file("A-small-attempt0.in", ios::in);
	
	if(!file)
		cout<<"File not opened\n";
	
	int A=0;
	int n=0;
	int count;
	
	file>>count;
	
	int r1, r2;
	int m1[4][4], m2[4][4];
	
	for(int i=0;i<count;i++)
	{
		printf("Case #%d: ",i+1);

		file>>r1;
		r1--;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				file>>m1[j][k];
			}
		}

		file>>r2;
		r2--;
		int ans=0;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				file>>m2[j][k];
			}
		}

		int matches=0;

		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(m1[r1][j] == m2[r2][k]){
					ans = m1[r1][j];
					matches++;
				}
			}
		}

		if(matches == 0)
			cout<<"Volunteer cheated!\n";
		else if(matches == 1)
			cout<<ans<<endl;
		else
			cout<<"Bad magician!\n";
	}
}

