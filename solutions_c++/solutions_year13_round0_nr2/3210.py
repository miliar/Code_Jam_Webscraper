#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main (int argc, char * const argv[])
{
	freopen("input2.txt", "rt", stdin);
	freopen("output2.txt", "wt", stdout);
	
	int T;
	cin >> T;
	
    int a[100][100];
    for(int t = 0; t < T; t++)
    {
        int N, M;
        cin >> N;
        cin >> M;
        
		for (int i = 0; i < N; i++)
        {
            for (int j = 0; j < M; j++)
            {
                cin >> a[i][j];
            }
        }
        
		bool possible = true;
        for (int i = 0; i < N && possible; i++)
        {
            for (int j = 0; j < M; j++)
            {
                bool found1 = true, found2 = true;
                for (int k = 0; k < M; k++)
                {
                    if (k != j && a[i][k] > a[i][j])
                    {
                        found1 = false;
                        break;
                    }
                }
                for (int k = 0; k < N; k++)
                {
                    if (k != i && a[k][j] > a[i][j])
                    {
                        found2 = false;
                        break;
                    }
                }
                
                if (!found1 && !found2)
                {
                    possible = false;
                    break;
                }
            }
        }
        
        if (possible)
            cout << "Case #" << t+1 << ": YES" << endl;
        else
            cout << "Case #" << t+1 << ": NO" << endl;
        
	}
	
	return 0;
}

