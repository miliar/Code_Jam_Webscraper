#include <iostream>
#include <cstring>

using namespace std;

bool line(int lawn[101][101], int x, int y, int N, int M)
{
    bool ver, hor;
    ver = hor = true;

	for(int ix = x; ix < M && ver; ix++)
	{
		if(lawn[x][y] < lawn[x][ix])
			ver = false;
	}

	for(int ix = x; ix >= 0 && ver; ix--)
	{
		if(lawn[x][y] < lawn[x][ix])
			ver = false;
	}

	for(int ix = x; ix < N && hor; ix++)
	{
		if(lawn[x][y] < lawn[ix][y])
			hor = false;
	}

	for(int ix = x; ix >= 0 && hor; ix--)
	{
		if(lawn[x][y] < lawn[ix][y])
			hor = false;
	}

	return (ver || hor);
}

int main()
{
	int T, N, M;
    int lawn[101][101];
    bool check;

	cin >> T;

	for(int ix = 0; ix < T; ix++)
	{
        cin >> N;
        cin >> M;

        memset(lawn, -1, sizeof(lawn));

        for(int iy = 0; iy < N; iy++)
        {
        	for(int iz = 0; iz < M; iz++)
        		cin >> lawn[iy][iz];
        }

        if(N == 1 || M == 1)
        {
        	cout << "Case #" << ix+1 << ": YES" << endl;
        	continue;
        }

        check = true;

        for(int iy = 0; iy < N && check; iy++)
        {
        	for(int iz = 0; iz < M && check; iz++)
                check = line(lawn, iy, iz, N, M);
        }

        if(check)
            cout << "Case #" << ix+1 << ": YES" << endl;
        else
        	cout << "Case #" << ix+1 << ": NO" << endl;
	}


	return 0;
}