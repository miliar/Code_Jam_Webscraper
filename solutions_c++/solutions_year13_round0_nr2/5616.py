#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;


bool check(int row, int col, int N, int M, vector< vector<int> > &lawn)
{
    bool rowCheck = true;
    bool colCheck = true;

    if (lawn[row][col] == 1)
    {
        // either row "row" or column col must have all same
        int rowElem = lawn[row][0];
        for (int i = 0; i < M; i++) {
            if (lawn[row][i] != 1) {            
                    rowCheck =  false;
                    break;            
            }
        }

        int colElem = lawn[0][col];
        for (int i = 0; i < N; i++) {
            if (lawn[i][col] != 1) {            
                    colCheck =  false;
                    break;            
            }
        }
    }

    if (rowCheck || colCheck) 
        return true;
    return false;

    return true;
}

int getRowSum(vector< vector<int> > &lawn, int row, int N, int M)
{
    int sum = 0;
    for (int i = 0; i < M; i++) {
        sum += lawn[row][i];
    }
    return sum;
}

int getColSum(vector< vector<int> > &lawn, int col, int N, int M)
{
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += lawn[i][col];
    }
    return sum;
}

bool solve( vector< vector<int> > &lawn, int N, int M)
{
    for (int i = 0; i < M; i++) {
        if (lawn[0][i] == 1) {
            int rowSum = getRowSum(lawn, 0, N, M);
            int colSum = getColSum(lawn, i, N, M);

            if (rowSum != M && colSum != N)
                return false;;
        }
        if (lawn[N-1][i] == 1) {
            int rowSum = getRowSum(lawn, N-1, N, M);
            int colSum = getColSum(lawn, i, N, M);

            if (rowSum != M && colSum != N)
                return false;;
        }
    }



    for (int i = 0; i < N; i++) {
        if (lawn[i][0] == 1) {
            int rowSum = getRowSum(lawn, i, N, M);
            int colSum = getColSum(lawn, 0, N, M);

            if (rowSum != M && colSum != N)
                return false;;
        }
        if (lawn[i][M-1] == 1) {
            int rowSum = getRowSum(lawn, i, N, M);
            int colSum = getColSum(lawn, M-1, N, M);

            if (rowSum != M && colSum != N)
                return false;;
        }
    }

    

    // check sub - matrix
    for (int i = 1; i < N-1; i++) {
        for (int j = 1; j < M-1; j++) {
            if ( !check(i, j, N, M, lawn) )
                return false;
        }
    }
    return true;
}


int main()
{
    FILE *fp = fopen("prob_small.in", "r");  
    
    bool special = false;
	int N, M, height, testcase;
    fscanf(fp, "%d\n", &testcase);


	for (int caseId = 1; caseId <= testcase; caseId++)
	{
        fscanf(fp, "%d", &N);
        fscanf(fp, "%d", &M);

        if (N == 1 || M == 1) {
            special = true;            
        }

        vector< vector<int> > lawn;

        for (int i = 0; i < N; i++) {
            
            vector<int> row;
            for (int j = 0; j < M; j++) {                
                fscanf(fp, "%d", &height);
                
                if (height > 100) {
                    printf("Case #%d: %s\n", caseId, "NO");
                    continue;
                }

                row.push_back(height);
            }
            lawn.push_back(row);
        }

        if (special) {
            printf("Case #%d: %s\n", caseId, "YES");
            special = false;
        } else {
            printf("Case #%d: %s\n", caseId, solve(lawn, N, M) == true ? "YES" : "NO" );
        }

        fscanf(fp, "\n");
	}
	return 0;
}
