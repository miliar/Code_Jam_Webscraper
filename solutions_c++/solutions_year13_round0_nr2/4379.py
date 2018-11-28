/*
    ID: darkangl3
    LANG: C++
    PROB:
*/
#include<iostream>
#include<fstream>
#include<string>
#include<conio.h>

using namespace std;

class Lawn{
    int arr[101][101];
    int n, m;
    int maxRow[101];
    int maxCol[101];
    public:
        Lawn(int n, int m, int a[101][101]) {
            this->n = n;
            this->m = m;
            for(int i = 0; i < n; i++)
                for(int j = 0; j < m; j++)
                    this->arr[i][j] = a[i][j];
        }
        
        string solve() {
            for(int i = 0; i < n; i++)
                maxRow[i] = findMaxRow(i);
                
            for(int i = 0; i < m; i++)
                maxCol[i] = findMaxCol(i);
                
            //each row
            for(int i = 0; i < n; i++) {
                //find place lower
                for (int j = 0; j < m; j++)
                    if (arr[i][j] < maxRow[i] && arr[i][j] < maxCol[j]) {
                        return "NO";
                    }
            }
            return "YES";
        }
        
        int findMaxRow(int row) {
            int maxR = -1;
            for(int i = 0; i < m; i++)
                if (maxR < arr[row][i]) {
                    maxR = arr[row][i];
                }
            return maxR;
        }
        
        int findMaxCol(int col) {
            int maxC = -1;
            for(int i = 0; i < n; i++)
                if (maxC < arr[i][col]) {
                    maxC = arr[i][col];
                }
            return maxC;
        }
};

int Test,n,m;
int a[101][101];

int main()
{
    ofstream fout ("test.out");
    ifstream fin ("test.in");
    
    fin >> Test;
    for(int t = 1; t <= Test; t++) {
        fin >> n >> m;
        for(int i = 0; i < n; i++) 
            for(int j = 0; j < m; j++)
                fin >> a[i][j];
        
        Lawn l(n, m, a);
        string res = l.solve();
        
        fout << "Case #" << t << ": " << res << endl;
    }
    return 0;
}
