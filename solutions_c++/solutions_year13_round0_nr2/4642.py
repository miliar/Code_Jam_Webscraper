#include<fstream>
using namespace std;

int main()
{
	ifstream in;
	ofstream out;
	in.open("input.txt");
	out.open("output.txt");
	int num_of_cases;
	int lawn[100][100];
	in >> num_of_cases;
	for(int i=0; i<num_of_cases; i++)
	{
		int N, M;
		in >> N >> M;
		for(int j=0; j<N; j++)
			for(int k=0; k<M; k++)
				in >> lawn[j][k];
		bool flag = false;
		for(int j=0; j<N; j++)
		{
			for(int k=0; k<M; k++)
			{
				bool flag1 = false, flag2 = false;
				for(int cnt=0; cnt<N; cnt++)
				{
					if(lawn[j][k] < lawn[cnt][k])
					{
						flag1 = true;
						break;
					}
				}
				for(int cnt=0; cnt<M; cnt++)
				{
					if(lawn[j][k] < lawn[j][cnt])
					{
						flag2 = true;
						break;
					}
				}
				if(flag1 && flag2) flag = true;
			}
		}
		if(flag)
			out << "Case #" << i+1 << ": NO" << endl;
		else
			out << "Case #" << i+1 << ": YES" << endl;
	}
	return 0;
}