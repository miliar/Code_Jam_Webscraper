#include "mhead.h"
void OpenFile(string fildir,ifstream &fin)
{
	fin.open(fildir);
	if (!fin)
	{
		cout<<"File open fail!"<<endl;
		exit(0);
	}
}
void ReadRow(int* sequence,ifstream &fin)
{
	int answer = 0;
	int relay = 4;
	char tmep[128];
	fin>>answer;
	fin.getline(tmep,128,'\n');
	for (int i=1;i<answer;i++)
	{
		fin.getline(tmep,128,'\n');
		--relay;
	}
	for (int i=0;i<4;i++)
	{
		fin>>sequence[i];
	}
	for (int i=0;i<relay;i++)
	{
		fin.getline(tmep,128,'\n');
	}

}
void MagicMatch(ofstream& outfile,int* seq1,int* seq2,const int& casenum)
{
	int same = 0;
	int result = 0;
	for (int i= 0;i<4;i++)
	{
		for (int j=0;j<4;j++)
		{
			if (seq1[i]==seq2[j])
			{
				same++;
				result = seq1[i];
			}
		}
	}
	if (same==1)
	{
		outfile<<"Case #"<<casenum<<": "<<result<<endl;
	}
	if (same>1)
	{
		outfile<<"Case #"<<casenum<<": Bad magician!"<<endl;
	}
	if (same ==0)
	{
		outfile<<"Case #"<<casenum<<": Volunteer cheated!"<<endl;
	}
}
int main()
{
	int LoopRead = 0;
	int* Sequence1 = new int[4];
	int* Sequence2 = new int[4];
	ifstream filein;
	ofstream fileout;
	const string InDIR = "D:\\A-small-attempt1.in";  //file count
	const string OutDIR = "D:\\Outfile.in";
	OpenFile(InDIR,filein);
	ofstream outfile(OutDIR);
	filein>>LoopRead;
	for(int i = 0;i<LoopRead;i++)
	{
		ReadRow(Sequence1,filein);
		ReadRow(Sequence2,filein);
		MagicMatch(outfile,Sequence1,Sequence2,i+1);
	}
	delete Sequence1;
	delete Sequence2;
	return 0;
}