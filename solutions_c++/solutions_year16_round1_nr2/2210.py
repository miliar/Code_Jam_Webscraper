#include <fstream>
#include <iostream>
#include <queue>
#include <vector>
#include <string>
#include <climits>
#include <map>
#include <algorithm>

using namespace std;

bool MyComp(vector<int> &lhs, vector<int> &rhs){
    return (lhs[0] < rhs[0]);
}

vector<int> findMin(int n, int head, vector<vector<int>> &v){
    vector<int> sol;
    int Min;
    for (int i = head; i < v.size(); i++){
        if (sol.size() == 0){
            Min = v[i][n];
            sol.push_back(i);
        }
        else if (v[i][n] == Min)
            sol.push_back(i);
        else if (v[i][n] < Min){
            Min = v[i][n];
            sol.assign(1, i);
        }
    }
    return sol;
}

int main(){
    ifstream fin("in2");
    ofstream fout("out2");
    int T;
    string S;

    fin >> T;
    for (int t = 1; t <= T; t++){
        fout << "Case #" << t << ": ";

        int MIN = INT_MAX;
        int N;
        fin >> N;
        vector<vector<int>> V(2 * N - 1, vector<int>(N, 0));
        for (int i = 0; i < 2 * N - 1; i++){
            for (int j = 0; j < N; j++)
                fin >> V[i][j];
            MIN = min(MIN, V[i][0]);
        }
        
        int n = 0;
        while (n < N){
            vector<int> v = findMin(n, 2 * n, V);
            V[2 * n].swap(V[v[0]]);
            if (v.size() == 1)
                break;
            V[2 * n + 1].swap(V[v[1]]);
            n++;
        }

        /*
        for (int i = 0; i < V.size(); i++){
            for (int j = 0; j < N; j++)
                cout << V[i][j] << " ";
            cout << endl;
        }
        */

        vector<int> sol(N, 0);
        for (int i = 0; i < n; i++){
            if (V[2 * i][n] != V[2 * n][i])
                sol[i] = V[2 * i][n];
            else
                sol[i] = V[2 * i + 1][n];
        }
        sol[n] = V[2 * n][n];

        int i = n + 1;
        while (i < N){
            vector<int> v = findMin(i, 2 * i - 1, V);
            V[2 * i - 1].swap(V[v[0]]);
            V[2 * i].swap(V[v[1]]);
            if (V[2 * i - 1][n] != V[2 * n][i])
                sol[i] = V[2 * i - 1][n];
            else
                sol[i] = V[2 * i][n];
            i++;
        }

        for (int i = 0; i < N; i++){
            fout << sol[i] << " ";
        }
        fout << endl;
    }

    fin.close();
    fout.close();
}
