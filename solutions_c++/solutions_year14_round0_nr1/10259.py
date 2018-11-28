#include <iostream>
#include<fstream>
using namespace std;

int MagicianTrick(int,int [][4],int,int [][4]);
int main()
{
	int i,j,k;
	int T;
	int card_set[4][4];
	int rearranged_card_set[4][4];
	int rownumber1;
	int rownumber2;
	int answer[100];

	ifstream fin("A-small-attempt2.in",ios::in);
	if(!fin)
		return EXIT_FAILURE;
	ofstream fout("Problem_A.out",ios::out);

	while(fin.peek() != EOF)
	{
		
	
	fin>>T;

	for(i=0;i<T;i++)
	{
		fin>>rownumber1;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				fin>>card_set[j][k];
			}
		}
		fin>>rownumber2;
		for(j=0;j<4;j++)
		{
			for(k=0;k<4;k++)
			{
				fin>>rearranged_card_set[j][k];
			}
		}
		answer[i] = MagicianTrick(rownumber1,card_set,rownumber2,rearranged_card_set);
	}

	for(i=0;i<T;i++)
	{
		fout<<"Case #"<<i+1<<": ";
		switch(answer[i])
		{
		case 1  : fout<< 1  <<endl;break;
		case 2  : fout<< 2  <<endl;break;
		case 3  : fout<< 3  <<endl;break;
		case 4  : fout<< 4  <<endl;break;
		case 5  : fout<< 5  <<endl;break;
		case 6  : fout<< 6  <<endl;break;
		case 7  : fout<< 7  <<endl;break;
		case 8  : fout<< 8  <<endl;break;
		case 9  : fout<< 9  <<endl;break;
		case 10 : fout<< 10 <<endl;break;
		case 11 : fout<< 11 <<endl;break;
		case 12 : fout<< 12 <<endl;break;
		case 13 : fout<< 13 <<endl;break;
		case 14 : fout<< 14 <<endl;break;
		case 15 : fout<< 15 <<endl;break;
		case 16 : fout<< 16 <<endl;break;
		case 17 : fout<< "Bad magician!" <<endl;break;
		case 18 : fout<< "Volunteer cheated!" <<endl;break;
		}
	}
	}
//	for(k=0;k<10000000000;k++);
	return 0;
}

int MagicianTrick(int rownumber1,int card_set[][4],int rownumber2,int rearranged_card_set[][4])
{
	int count=0;
	int answer;

	int i,j,k;

	//for(i=0;i<4;i++) fout<<card_set[rownumber1][i]<<"         "<<rearranged_card_set[rownumber2][i]<<endl;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(card_set[rownumber1-1][i]==rearranged_card_set[rownumber2-1][j])
			{
				count++;
				answer = card_set[rownumber1-1][i];
			}
		}
	}

	//fout<<"count is "<<count;
	//fout<<"answer is "<<answer;
	//fout<<endl;

	if(count==0) return 18;
	else if(count==1) return answer;
	else if(count>1&&count<17) return 17;
}