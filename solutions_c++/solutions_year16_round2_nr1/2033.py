#include<iostream>
#include<vector>
#include<string>
#include<fstream>

using namespace std;

int T;
string st;
vector<int> a;
vector<int> ans;

int main()
{
	ifstream fin;
	ofstream fout;
	
	fin.open("input.txt");
	fout.open("output.txt");
	
	fin >> T;
	for(int tc = 1; tc <= T; tc++)
	{
		fin >> st;
		
		a.clear();
		a = vector<int>(26, 0);
		for(int i = 0; i < st.size(); i++)
		{
			a[st[i] - 'A']++;
		}
		
		ans.clear();
		ans = vector<int>(10, 0);
		
		if(a['Z' - 'A'] != 0)
		{
			a['E' - 'A'] -= a['Z' - 'A'];
			a['R' - 'A'] -= a['Z' - 'A'];
			a['O' - 'A'] -= a['Z' - 'A'];
			
			ans[0] += a['Z' - 'A'];
			a['Z' - 'A'] = 0;
		}
		if(a['W' - 'A'] != 0)
		{
			a['T' - 'A'] -= a['W' - 'A'];
			a['O' - 'A'] -= a['W' - 'A'];
			
			ans[2] += a['W' - 'A'];
			a['W' - 'A'] = 0;
		}
		if(a['U' - 'A'] != 0)
		{
			a['F' - 'A'] -= a['U' - 'A'];
			a['O' - 'A'] -= a['U' - 'A'];
			a['R' - 'A'] -= a['U' - 'A'];
			
			ans[4] += a['U' - 'A'];
			a['U' - 'A'] = 0;
		}
		if(a['X' - 'A'] != 0)
		{
			a['S' - 'A'] -= a['X' - 'A'];
			a['I' - 'A'] -= a['X' - 'A'];
			
			ans[6] += a['X' - 'A'];
			a['X' - 'A'] = 0;
		}
		if(a['G' - 'A'] != 0)
		{
			a['E' - 'A'] -= a['G' - 'A'];
			a['I' - 'A'] -= a['G' - 'A'];
			a['H' - 'A'] -= a['G' - 'A'];
			a['T' - 'A'] -= a['G' - 'A'];
			
			ans[8] += a['G' - 'A'];
			a['G' - 'A'] = 0;
		}
		if(a['O' - 'A'] != 0)
		{
			a['N' - 'A'] -= a['O' - 'A'];
			a['E' - 'A'] -= a['O' - 'A'];
			
			ans[1] += a['O' - 'A'];
			a['O' - 'A'] = 0;
		}
		if(a['H' - 'A'] != 0)
		{
			a['T' - 'A'] -= a['H' - 'A'];
			a['R' - 'A'] -= a['H' - 'A'];
			a['E' - 'A'] -= 2 * a['H' - 'A'];
			
			ans[3] += a['H' - 'A'];
			a['H' - 'A'] = 0;
		}
		if(a['F' - 'A'] != 0)
		{
			a['I' - 'A'] -= a['F' - 'A'];
			a['V' - 'A'] -= a['F' - 'A'];
			a['E' - 'A'] -= a['F' - 'A'];
			
			ans[5] += a['F' - 'A'];
			a['F' - 'A'] = 0;
		}
		if(a['S' - 'A'] != 0)
		{
			a['E' - 'A'] -= 2 * a['S' - 'A'];
			a['V' - 'A'] -= a['S' - 'A'];
			a['N' - 'A'] -= a['S' - 'A'];
			
			ans[7] += a['S' - 'A'];
			a['S' - 'A'] = 0;
		}
		if(a['I' - 'A'] != 0)
		{
			a['N' - 'A'] -= 2 * a['I' - 'A'];
			a['E' - 'A'] -= a['I' - 'A'];
			
			ans[9] += a['I' - 'A'];
			a['I' - 'A'] = 0;
		}
		
		fout << "Case #" << tc << ": ";
		for(int i = 0; i < 10; i++)
		{
			for(int j = 0; j < ans[i]; j++)
			{
				fout << i;
			}
		}
		fout << endl;
	}
}
