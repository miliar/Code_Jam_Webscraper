#include <iostream>

using namespace std;

int max(int a, int b)
{
	return (a>b)?a:b;
}

int main()
{
	int T = 0;
	cin >> T;
	for(int t=1;t<=T;t++)
	{
		int N = 0, M = 0;
		cin >> N >> M;
		int X[N][M];
		int R_MAX[N];
		int C_MAX[M];

		for(int n=0;n<N;n++) R_MAX[n] = 0;
		for(int m=0;m<M;m++) C_MAX[m] = 0;

		for(int n=0;n<N;n++)
		{
			for(int m=0;m<M;m++)
			{
				cin >> X[n][m];
				R_MAX[n] = max(R_MAX[n],X[n][m]);
				C_MAX[m] = max(C_MAX[m],X[n][m]);
			}
		}
		//cout << "input" << endl; for(int n=0;n<N;n++) { for(int m=0;m<M;m++) { cout << X[n][m] << " "; } cout << endl; }
		//cout << "r max" << endl; for(int n=0;n<N;n++) cout << R_MAX[n] << " "; cout << endl;
		//cout << "c max" << endl; for(int m=0;m<M;m++) cout << C_MAX[m] << " "; cout << endl;

		bool flag = true;
		for(int n=0;n<N && flag==true;n++)
		{
			for(int m=0;m<M && flag==true;m++)
			{
				//cout << n << ":" << m << " :: " << X[n][m] << " :: " << R_MAX[n] << " :: " << C_MAX[m] << endl;
				if((X[n][m] < R_MAX[n] && X[n][m] != C_MAX[m]) || (X[n][m] < C_MAX[m] && X[n][m] != R_MAX[n]))
					flag = false;
			}
		}
		if(!flag)
			cout << "Case #" << t << ": NO" << endl;
		else
			cout << "Case #" << t << ": YES" << endl;
	}
	return 0;
}
