#include <fstream>

using namespace std;

int main()
{
    ifstream in("m.in");
    ofstream out("m.out");

    int times = 0;
    in >> times;

    for (int num = 0;num < times;num++)
    {
        int N,M;
        in >> N >> M;
        int **matrix = new int*[N];
        for (int i = 0;i < N;i++)
        {
            matrix[i] = new int[M];
            for (int j = 0;j < M;j++)
            {
                in >> matrix[i][j];
            }
        }

        int *iMax = new int[N];
        int *jMax = new int[M];

        for (int i = 0;i < N;i++)
        {
            int temp = matrix[i][0];
            for (int j = 1;j < M;j++)
                if (matrix[i][j] > temp) temp = matrix[i][j];
            iMax[i] = temp;
        }
        for (int j = 0;j < M;j++)
        {
            int temp = matrix[0][j];
            for (int i = 1;i < N;i++)
                if (matrix[i][j] > temp) temp = matrix[i][j];
            jMax[j] = temp;
        }
        bool ans = true;
        for (int i = 0;i < N;i++)
            for (int j = 0;j < M;j++)
                if (matrix[i][j] < iMax[i] && matrix[i][j] < jMax[j]) ans = false;

        out << "Case #" << num + 1;
        if (ans) out << ": YES\n";
        else out << ": NO\n";


    }

    return 0;
}
