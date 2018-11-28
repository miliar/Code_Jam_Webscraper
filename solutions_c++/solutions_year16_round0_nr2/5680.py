#include <fstream>
#include <vector>

using namespace std;
typedef vector<int> vi;

ifstream in("b.in"); ofstream out("b.out");
int T, l=1;

int main()
{
	in>>T;
	while(T--)
	{
		string seqs; int mul = 1, result = 0; vi seqv;
		
		in>>seqs;
		for(int i=0;i<seqs.size();i++)	if(seqs[i]=='+') seqv.push_back(1); else seqv.push_back(-1);
		for(int i = seqv.size()-1; i>=0; i--) if (mul*seqv[i]== -1) { result += 1; mul *= -1;} else continue;		

		out<<"Case #"<<l<<": "<<result<<endl;
		seqv.clear(); l++;
		
	}
}




