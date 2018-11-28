#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ofstream fout ("o.out");
    ifstream fin ("in.in");
	int tetC;
	fin >> tetC;
	for(int cnt = 0; cnt < tetC; cnt++)
	{
		unsigned int ol,nw,wn;
		fin >> ol >> nw >> wn;
		long long ret = 0;
		for(unsigned int ct = 0; ct < ol; ct++)
			for(unsigned int ctc = 0; ctc < nw; ctc++)
			{
				if( (ct & ctc) < wn)
					ret++;
			}	
			
			
		fout << "Case #" << cnt+1 << ": " << ret << endl;
	}
	return 0;
}

