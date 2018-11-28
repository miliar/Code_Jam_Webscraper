#include <fstream>

int a,b,k;
float count=0;
int main()
{
	std::ifstream file1("B-small-attempt0 (1).in");
	std::ofstream file2("output.txt");
	int t;
	file1>>t;
	for(int i=1;i<=t;i++)
	{
		count=0;
		file1>>a>>b>>k;
		for(int j=0;j<a;j++)
			for(int l=0;l<b;l++)
				if((j & l)<k)
					count++;
		file2<<"Case #"<<i<<": "<<count<<"\n";
		
	}
	return 0;
}