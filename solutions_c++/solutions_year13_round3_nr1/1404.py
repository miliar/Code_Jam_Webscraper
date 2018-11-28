#include<fstream>
#include<set>
#include<string>

using namespace std;


long calc(long bg, long l, long len, set<pair<long, long> >& appear)
{
	long t=0;
	for (long i=0; i<=bg; ++i)
		for (long j=len-1; j>=bg+l-1; --j)
		{
			if (!appear.count(make_pair(i,j)))
			{
				++t;
				appear.insert(make_pair(i,j));
			}
		}
	return t;
}

long work(const string& name, long l, const set<char>& consonants)
{
	long t=0;
	long len=strlen(name.c_str());
	set<pair<long, long> > appear;
	for (long bg=0; bg<=len-l; ++bg)
	{
		bool flag=true;
		for (long i=0; i!=l; ++i)
		{
			if (!consonants.count(name[bg+i]))
			{
				flag=false;
				break;
			}
		}
		if (flag)
		{
			t+=calc(bg, l, len, appear);
		}
	}
	return t;
}


int main()
{
	set<char> vowels;
	vowels.insert('a');
	vowels.insert('e');
	vowels.insert('i');
	vowels.insert('o');
	vowels.insert('u');
	set<char> consonants;
	for (char c='a'; c<='z'; ++c)
		if (!vowels.count(c))
			consonants.insert(c);
	
	long n,l;
	string name;
	
	ifstream infile("R1CA.in");
	ofstream ofile("R1CA.txt");

	infile>>n;
	for (long i=0; i!=n; ++i)
	{
		infile>>name;
		infile>>l;
		ofile<<"Case #"<<i+1<<": "<<work(name, l, consonants)<<endl;
	}

	infile.close();
	ofile.close();
}
