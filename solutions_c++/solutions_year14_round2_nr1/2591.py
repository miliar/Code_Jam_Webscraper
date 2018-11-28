#include <iostream>
#include <string>
#include <vector>
#define INF 1000000
using namespace std;

int sol(vector<vector<int>> &A, int i, int j, string a, string b) {
    if(A[i][j] != -1) {
        return A[i][j];
    }
    else {
        if(i == 0 && j == 0) {
            if(a[i] == b[i])
            {
                A[i][j] = 0;
                return 0;
            }
            else {
                A[i][j] = INF;
                return INF;
            }
        }
        else if (i == 0) {
            if(a[i] == b[j]) {
                A[i][j] = 1+sol(A, i, j-1, a, b);
                return A[i][j];
            }
        }
        else if (j == 0) {
            if(a[i] == b[j]) {
                A[i][j] = 1+sol(A, i-1, j, a, b);
                return A[i][j];
            }
        }
        //Sinon i > 0 et j > 0:
        
        int r = INF;
        if(a[i] == b[j]) {
            r = min(r, sol(A, i-1, j-1, a, b));
        }
        if(a[i-1] == a[i]) {
            r = min(r, 1+sol(A, i-1, j, a, b));
        }
        if(b[j-1] == b[j]) {
            r = min(r, 1+sol(A, i, j-1, a, b));
        }
        A[i][j] = r;
        return r;
        
    }
}

int main()
{
    int nb_examples;
    cin >> nb_examples;
    for(int i = 1; i <= nb_examples; i++) {
        int nb;
        cin >> nb;
        if(nb == 2) {
            string a, b;
            cin >> a >> b;
            vector<vector<int>> A(a.length(), vector<int>(b.length(), -1));
            int r = sol(A, a.length()-1, b.length()-1, a, b);
            cout << "Case #" << i << ": ";
            if(r < INF) {
                cout << r << endl;
            }
            else
                cout << "Fegla Won" << endl;
        }
        else {
            for(int k = 1; k <= nb; k++) {
                string s;
                cin >> s;
            }
        }
    }
    return 0;
}