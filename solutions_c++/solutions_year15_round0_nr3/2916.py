#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

typedef pair<bool,char> Number;

Number eval(Number a, Number b)
{
	Number ret;
	ret.first = ! (a.first ^ b.first);
	if (a.second == '1')
	{
		ret.second = b.second;
		return ret;
	}
	if (b.second == '1')
	{
		ret.second = a.second;
		return ret;
	}
	
	if (a.second == b.second)
	{
		ret.first = !ret.first;
		ret.second = '1';
		return ret;
	}
	
	if (a.second == 'i' && b.second == 'j')
	{
		ret.second = 'k';
		return ret;
	}
	if (a.second == 'i' && b.second == 'k')
	{
		ret.first = !ret.first;
		ret.second = 'j';
		return ret;
	}
	if (a.second == 'j' && b.second == 'k')
	{
		ret.second = 'i';
		return ret;
	}
	if (a.second == 'j' && b.second == 'i')
	{
		ret.first = !ret.first;
		ret.second = 'k';
		return ret;
	}
	if (a.second == 'k' && b.second == 'i')
	{
		ret.second = 'j';
		return ret;
	}
	if (a.second == 'k' && b.second == 'j')
	{
		ret.first = !ret.first;
		ret.second = 'i';
		return ret;
	}
	
	return make_pair(true,'e');
	
}


int main(int argc, char *argv[])
{
    if (argc!=3) 
    {
	cout << "Missing arguments." << endl;
	return -1;
    }
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;

    for (int i = 0; i < T; ++i)
    {
		cout << "Test Case # " << i << endl;
		int L, X;
		fin >> L >> X;
		string S;
		fin >> S;
		
		string s;
		for (int j = 0; j < X; ++j)
		{
			s += S;
		}
		
		vector<vector<Number> > table(s.size());
		for (int j = 0; j < table.size(); ++j)
		{
			table[j].resize(s.size());
			table[j][j] = make_pair(true,s[j]);
		}
		
		for (int j = 0; j < table.size(); ++j)
		{
			for (int k = j+1; k < table.size(); ++k)
			{
				table[j][k] = eval(table[j][k-1],table[k][k]);
			}
		}
		
	
		bool result = false;
		for (int j = 0; j < table.size()-2; ++j)
		{
			if (result) break;
			
			if (table[0][j] == make_pair(true,'i'))
			{
				//cout << "Splitting for i at: " << j << endl;
				for (int k = j+1; k < table.size()-1; ++k)
					if (table[j+1][k] == make_pair(true,'j'))
					{
						//cout << j+1 << "," << k << " is " << table[j+1][k].second << endl;
						//cout << k+1 << "," << table.size()-1 << " is " << table[k+1][table.size()-1].second << endl;
						if (table[k+1][table.size()-1] == make_pair(true,'k'))
						{
							//cout << "Splitting for jk at: " << k << endl;
							result = true;
							break;
						}
					}
			}
		}
			
	
		
		
		if (result) fout << "Case #" << i+1 << ": YES";	
		else fout << "Case #" << i+1 << ": NO";	
		fout << endl;
    }
    return 0;
}
