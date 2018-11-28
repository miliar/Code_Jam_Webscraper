#include <fstream>

using namespace std;

int num[5]={1,4,9,121,484};

main()
{
	int T,A,B;
	ifstream fin ("input.in");
	ofstream fout ("output.out");
	fin >> T;
	for (int z=1;z<=T;z++)
	{
		fin >> A >> B;
		int s=0;
		for (int i=0;i<5;i++)
			if ((num[i]>=A)&&(num[i]<=B)) s++;
		fout << "Case #" << z << ": " << s << endl;
	}
}
