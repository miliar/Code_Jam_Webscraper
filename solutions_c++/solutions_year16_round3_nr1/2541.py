#include <iostream>
#include <cstdio>
#include <fstream>
using namespace std;
char print(int x)
{
	switch(x)
	{
		case 1:
			return 'A';
		case 2:
			return 'B';
		case 3:
			return 'C';
		case 4:
			return 'D';
		case 5:
			return 'E';	
		case 6:
			return 'F';
		case 7:
			return 'G';
		case 8:
			return 'H';
		case 9:
			return 'I';
		case 10:
			return 'J';
		case 11:
			return 'K';
		case 12:
			return 'L';
		case 13:
			return 'M';
		case 14:
			return 'N';
		case 15:
			return 'O';
		case 16:
			return 'P';
		case 17:
			return 'Q';
		case 18:
			return 'R';
		case 19:
			return 'S';
		case 20:
			return 'T';
		case 21:
			return 'U';
		case 22:
			return 'V';
		case 23:
			return 'W';
		case 24:
			return 'X';
		case 25:
			return 'Y';
		case 26:
			return 'Z';
	}
}
int main()
{
	ifstream input;
	input.open("A-large.in", ios::in);
	ofstream output;
	output.open("Answer-A-large.txt", ios::out);
	int T, Z;
	input>>T;
//	cin>>T;
	Z=T;
	while(Z--)
	{
		int i, N, P[26], Q=0, majority, flag, max, j;
		input>>N;
//		cin>>N;
		for(i=0; i<N; i++)
		{
			input>>P[i];
//			cin>>P[i];
			Q+=P[i];
		}
		output<<"Case #"<<T-Z<<": ";
		while(Q!=0)
		{
			majority=Q/2+1;
			flag=0;
			for(i=0; (i<N && flag<2) ;i++)
			{
				if(P[i]>=majority)
				{
					P[i]--;
					Q--;
					majority=Q/2+1;
					output<<print(i+1);
					flag++;
					i=0;
				}
			}
			if(flag==0)
			{
				for(i=0, max=0; i<N; i++)
					if(P[i]>max)
					{
						max=P[i];
						j=i;
					}
				P[j]--;
				Q--;
				majority=Q/2+1;
				output<<print(j+1);
				flag++;
				for(i=0; (i<N && flag<2) ;i++)
				{
					if(P[i]>=majority)
					{
						P[i]--;
						Q--;
						majority=Q/2+1;
						output<<print(i+1);
						flag++;
						i=0;
					}
				}
			}
			output<<" ";
		}
		output<<"\n";
	}
	input.close();
	output.close();
	return 0;
}
