#include <iostream>
#include <vector>

using namespace std;

const int Grass_Initial_Height = 100;

class Landmower
{
public:
    Landmower(int N, int M)
        : field(N, vector<int>(M, Grass_Initial_Height)),
          row_max(N, 0),
          col_max(M, 0),
          N(N),
          M(M)
    {
    }

    void add(int i, int j, int h)
    {
        field[i][j] = h;
        if (row_max[i] < h)
            row_max[i] = h;
        if (col_max[j] < h)
            col_max[j] = h;
    }

    bool solve()
    {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                int h = field[i][j];
                if (h < row_max[i] && h < col_max[j])
                    return false;
            }
        }
        return true;
    }

private:
    vector<vector<int> > field;
    vector<int> row_max;
    vector<int> col_max;
    int N;
    int M;
};

int main()
{
    int num_cases;
    cin >> num_cases;
    for (int current_case = 1; current_case <= num_cases; current_case++) {
        int N, M, h;
        cin >> N >> M;
        Landmower task(N, M);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                cin >> h;
                task.add(i, j, h);
            }
        }

        cout << "Case #" << current_case << ": "
             << (task.solve()? "YES" : "NO") << "\n";
    }
}

