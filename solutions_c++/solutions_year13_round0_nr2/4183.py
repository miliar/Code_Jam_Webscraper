#include<fstream>
using namespace std;
int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T, N, M, nowVal;
	int arr[100][100];
	bool good = true, row = true, col = true;

	in >> T;

	for(int i = 0; i < T; i++)
	//this for loop deals with each case...
	{
		in >> N >> M;
		
		row = true, col = true, good = true;

		for(int j = 0; j < N; j++)
		{
			for(int k = 0; k < M; k++)
			{
				in >> arr[j][k];
			}
		}
		for(int j = 0; j < N; j++){
			for(int k = 0; k < M; k++){
				col = true, row = true;
				nowVal = arr[j][k];
				for(int a = 0; a < N; a++){
					if(nowVal < arr[a][k])
						col = false;
				}
				for(int b = 0; b < M; b++){
					if(nowVal < arr[j][b])
						row = false;
				}
				if(!col && !row)
					good = false;
			}
		}
		if(good)
			out << "Case #" << i+1 << ": YES" << endl; 
		else
			out << "Case #" << i+1 << ": NO" << endl; 
	}
}