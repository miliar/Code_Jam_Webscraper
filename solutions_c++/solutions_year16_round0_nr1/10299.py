#include<string>
#include<fstream>
#include<sstream>
#include<iomanip>
#include<set>
using namespace std;

int main()
{
	int cases,n,i;
	string ifile = "large.in",ofile= "output.txt";
	stringstream ss;
	ifstream input;
	input.open(ifile);
	input>>cases;
	set<char> found;
	for( int round = 1 ; round<=cases ; ++round )
	{
		found.clear();
		input>>n;
		string answer = "INSOMNIA";
		i = 1;
		string mstring;
		while (found.size() < 10 && n != 0)
		{
			int multiple = i * n;
			mstring = std::to_string(multiple); 
			for(int idx = 0 ; idx < (int)mstring.length() ; ++idx)
			{
				found.insert(mstring[idx]);
			}
			i++;
		}
		if (found.size() == 10)answer = mstring;
		ss<<"Case #"<<round<<": "<<answer<<"\n";
	}
	input.close();
	ofstream output;
	output.open(ofile);
	output<<ss.rdbuf();
	output.flush();
	output.close();
	return 0;
}