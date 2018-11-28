#include <fstream>
#include <stdio.h>
using namespace std;

int main()
{
	ifstream in(".\\input.txt");
	FILE *out;
	out = fopen(".\\output.txt", "wt");
	int T;
	in>>T;
	for (int i = 0; i < T; i++)
	{
		//out<<"Case #"<<i+1<<": ";
		fprintf(out, "Case #%d: ", i+1);
		double per = 2;
		double time = 0;
		double c, f, x;
		in>>c>>f>>x;
		while ((x/per) > (c/per+x/(per+f)))
		{
			time+=c/per;
			per+=f;
		}
		time+=x/per;
		fprintf(out, "%.7f\n", time);
		//out<<time<<endl;
	}
	return 0;
}