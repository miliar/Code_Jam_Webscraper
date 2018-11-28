#include<fstream>
using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");
int main()
{
	int T;
	in >> T;
	for(int t=0;t<T;t++)
	{
		int S,E;
		int Arr[5][5]={0,};
		int Arr2[5][5]={0,};
		in >> S;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				in>>Arr[i][j];
		in>>E;
		for(int i=1;i<=4;i++)
			for(int j=1;j<=4;j++)
				in>>Arr2[i][j];


		int Ans=0;
		int cnt=0;
		for(int i=1;i<=4;i++)
		{
			for(int j=1;j<=4;j++)
			{
				if(Arr[S][i] == Arr2[E][j])
				{
					Ans=Arr[S][i];
					cnt++;
				}
			}
		}
		out << "Case #" << t+1 << ": ";
		if(cnt==0)
			out << "Volunteer cheated!" << endl;
		else if(cnt > 1)
			out << "Bad magician!" << endl;
		else if(cnt == 1)
			out << Ans << endl;


	}
	return 0;
}