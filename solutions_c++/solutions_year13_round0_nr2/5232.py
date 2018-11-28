#include<iostream>
#include<sstream>
#include<string>
using namespace std;

#define ll long long
bool checkRowCol(int row, int col, int** mat, int n, int m){
    //check whether all elems in the row are small than mat[row][col]
    bool isRowSmall = true;
    for(unsigned i=0; i<m; i++)
        if(mat[row][i] > mat[row][col]){
            isRowSmall = false;
            break;
        }

    bool isColSmall = true;
    for(unsigned i=0; i<n; i++)
        if(mat[i][col] > mat[row][col]){
            isColSmall = false;
            break;
        }

    return isRowSmall || isColSmall;
}
int main()
{
    unsigned ts;
    cin>>ts;
    int **mat = new int*[100];
    for(unsigned i=0; i<100; i++){
        mat[i] = new int[100];
    }
    for(unsigned t=1; t<=ts; t++){
        int n, m;
        cin>>n>>m;
        for(unsigned i=0; i<n; i++){
            for(unsigned j=0; j<m; j++)
                cin>>mat[i][j];
        }
        string ans = "YES"; bool breaked = false;
        for(unsigned i=0; i<n && !breaked; i++){
            for(unsigned j=0; j<m && !breaked; j++){
                if(checkRowCol(i,j, mat, n, m)){
                    //cout<<"DEBUG: "<<mat[i][j]<<" at "<<i<<","<<j<<" correct.\n";
                    continue;
                }else{
                    //cout<<"DEBUG: "<<mat[i][j]<<" at "<<i<<","<<j<<" INcorrect.\n";
                    ans = "NO";
                    //cout<<"Case #"<<t<<": NO"<<endl;
                    breaked = true;
                }
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
    }
        for(unsigned i=0; i<100; i++)
            delete[] mat[i];
        delete[] mat;
    return 0;
}
