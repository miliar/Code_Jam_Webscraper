#include<fstream>
#include<string>
#include<sstream>
#include<iostream>
#include<math.h>
#include<iomanip>
#include<map>
using namespace std;
typedef map<int,map<int,int>> mmap;
string repeater(string s, int t)
{
	stringstream ss;
	for(int i =0;i<t;++i)
		ss<<s;
	return ss.str();
}
int main ()

{
	string ifile = "input.txt", ofile = "output.txt";
	ifstream input;
	input.open(ifile);
	stringstream ss;
	int cases;
	int l,x;
	string sequence;
	mmap ijk;
	ijk[2][2]=-1;ijk[2][3]=4;ijk[2][4]=-3;ijk[2][-2]=1;ijk[2][-3]=-4;ijk[2][-4]=3;
	ijk[-2][2]=1;ijk[-2][3]=-4;ijk[-2][4]=3;ijk[-2][-2]=-1;ijk[-2][-3]=4;ijk[-2][-4]=-3;
	ijk[3][2]=-4;ijk[3][3]=-1;ijk[3][4]=2;ijk[3][-2]=4;ijk[3][-3]=1;ijk[3][-4]=-2;
	ijk[-3][2]=4;ijk[-3][3]=1;ijk[-3][4]=-2;ijk[-3][-2]=-4;ijk[-3][-3]=-1;ijk[-3][-4]=2;
	ijk[4][2]=3;ijk[4][3]=-2;ijk[4][4]=-1;ijk[4][-2]=-3;ijk[4][-3]=2;ijk[4][-4]=1;
	ijk[-4][2]=-3;ijk[-4][3]=2;ijk[-4][4]=1;ijk[-4][-2]=3;ijk[-4][-3]=-2;ijk[-4][-4]=-1;
	map<char,int> chmap;
	chmap['i']=2;chmap['j']=3;chmap['k']=4;
	input>>cases;
	for(int c = 1; c <= cases; ++c)
	{
		input>>l>>x;
		input>>sequence;
		int total;
		char tmp;
		bool ifound=false, ijfound=false;
		string word = repeater(sequence,x);
		tmp = word[0];
		total = chmap[tmp];
		for(int i =1; i < word.size(); ++i)
		{
			if(total == 2) ifound = true;
			if(ifound && total == 4) ijfound = true;
			tmp = word[i];
			if (total == 1 || total == -1)
			{
				total *= chmap[tmp];
			}
			else
			{
				total = ijk[total][chmap[tmp]];
			}
		}
		ss<<"Case #"<<c<<(ifound && ijfound && total == -1? ": YES" :": NO") << "\n";
	}
	input.close();
	ofstream output;
	output.open(ofile);
	output<<ss.rdbuf();
	output.flush();
	output.close();
	return 0;
}