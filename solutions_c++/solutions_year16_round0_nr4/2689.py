#include<fstream>
#include<vector>
using namespace std;

int main()
{
	ifstream in("D.in");
	ofstream out("D.out");
	
	int t;
	in >> t;
	
	for(int i = 0;i < t;++i)
	{
		int K, C, S;
		
		in >> K >> C >> S;
		out<<"Case #"<<i + 1<<": ";
		for(int j = 1;j <= K;++j)
		{
			out<<j<<" ";
		}
		out<<"\n";
	}
	in.close();
	out.close();
}
