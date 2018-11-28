#include <fstream>

using namespace std;

main()
{
	int T;
	int map[100][100];
	ifstream fin ("input.in");
	ofstream fout ("output.out");
	fin >> T;
	for (int z=1;z<=T;z++)
	{
		int N,M;
		fin >> N >> M;
		bool iC[100][100]={false};
		for (int i=0;i<N;i++)
			for (int j=0;j<M;j++)
				fin >> map[i][j];
		for (int i=0;i<N;i++)
		{
			int max=0;
			for (int j=0;j<M;j++)
				if (max<map[i][j]) max=map[i][j];
			for (int j=0;j<M;j++)
				if (max==map[i][j]) iC[i][j]=true;
		}
		for (int j=0;j<M;j++)
		{
			int max=0;
			for (int i=0;i<N;i++)
				if (max<map[i][j]) max=map[i][j];
			for (int i=0;i<N;i++)
				if (max==map[i][j]) iC[i][j]=true;
		}
		for (int i=0;i<N;i++)
			for (int j=0;j<M;j++)
				if (!iC[i][j])
				{
					fout << "Case #" << z << ": NO" << endl;
					goto mend;
				}
		fout << "Case #" << z << ": YES" << endl;
		mend:;
	}
}
