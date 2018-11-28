#include <iostream>
#include <fstream>

using namespace std;
ifstream fin("input.txt");
ofstream fout("output.txt");
int main()
{
	
	int N;
	fin>>N;
	int T = 0;
	while(T < N)
	{
	int card1[4][4];
	int card2[4][4];
	int C1;
	fin>>C1;
	C1--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				fin>>card1[i][j];
			}
		}
		
		int C2;
		fin>>C2;		
		C2--;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4; j++){
				fin>>card2[i][j];
			}
		}
		int ary1[4];
		int ary2[4];
		for(int i = 0; i < 4; i++)
		{
			ary1[i] = card1[C1][i];
		}
		for(int i = 0; i < 4; i++)
		{
			ary2[i] = card2[C2][i];
		}
		int ct = 0;
		int ans;
		for(int i = 0; i < 4; i++)
		{
			for(int j = 0; j < 4; j++)
			{
				if(ary1[i] == ary2[j])
				{
					if(ct == 0)ans = ary1[i];
					ct++;
				}
			}
		}
		//int T = 0;
		if(ct > 1){fout<<"Case #"<<T+1<<":  Bad magician!"<<endl;}
		else if(ct == 1){fout<<"Case #"<<T+1<<": "<<ans<<endl;}
		else {fout<<"Case #"<<T+1<<": Volunteer cheated!"<<endl;}
		T++;
	}
}
