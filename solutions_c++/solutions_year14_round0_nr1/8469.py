#include <fstream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;
int main()
{
	int tt=1;
	
	ofstream fout("yay.out");
	ifstream fin ("A-small-attempt0.in");
	int a; fin >> a;
	for (int g=0; g<a; g++)
	{
		string o=""; 
		vector <int> hello;
		vector <int> compare;
		vector <int> similar;
		int b; fin >> b;
		for (int t=0; t<4; t++)
		{
			int o,i,u,y; fin >> o >> i >> u >> y;
			if (t==b-1)
			{
				hello.push_back(o); hello.push_back(i); hello.push_back(u); hello.push_back(y);
			}
		}
		int c; fin >> c;
		for (int t=0; t<4; t++)
		{
			int q,w,e,r; fin >> q >> w >> e >> r;
			if (t==c-1)
			{
				compare.push_back(q); compare.push_back(w); compare.push_back(e); compare.push_back(r);
			}
		}
		for (int g=0; g<hello.size(); g++)
		{
			for (int y=0; y<compare.size(); y++)
			{
				if (hello[g]==compare[y])
				{
					similar.push_back(hello[g]);
				}
			}
		}
		if (similar.size()==0)
		{
			stringstream cool;
			cool << tt;
			string legit= cool.str();
			cool.str(" ");
			o+="Case #"+legit+": "+"Volunteer cheated!";
		}
		else if (similar.size()==1)
		{
			stringstream cool;
			cool << tt;
			string legit= cool.str();
			cool.str(" ");
			stringstream xo;
			xo << similar[0];
			string yay= xo.str();
			xo.str(" ");
			o+="Case #" + legit + ": " + yay;
		}
		else
		{
			stringstream cool;
			cool << tt;
			string legit= cool.str();
			cool.str(" ");
			o+="Case #"+legit+": "+"Bad magician!";
		}
		fout<< o << endl;
		similar.clear(); compare.clear(); hello.clear();
		
		tt+=1;
			
		
	}
}
