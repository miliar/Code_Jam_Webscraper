#include <fstream>
using namespace std;
int main()
{
	ifstream fin("B-small-attempt0 (1).in");
	ofstream fout("yayz.out");
	int a; fin >> a;
	for (int g=0; g<a; g++)
	{
		int c,d,e; fin >> c >> d >> e;int ans=0;
		for (int g=0; g<c; g++)
		{
			for (int y=0; y<d; y++)
			{
				if ((g&y)<e)
				{
					ans+=1;
				}
			}
		}
		fout << "Case #" << g+1 << ": " << ans << '\n';
	}
	
	
	
	
}
