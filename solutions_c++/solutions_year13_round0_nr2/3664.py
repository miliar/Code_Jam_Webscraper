#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;
void printArr(int **a, int n, int m);
int getMaxRows(int *t, int s);
int getMaxCols(int **t, int s,int ind);
void printArr(int *a, int n);
int checkArr(int **a, int r, int c, int *rMax, int *cMax);
//getNumbers
int main()
{
    vector <string> outputStr;
    int T = 0;
    ifstream inFile;
    ofstream outFile;
    stringstream ss;
    string line;
    //stringstream ss;
    int temp;
    double dtemp;
    string output;

    inFile.open("B-large.in");
    if(!inFile.is_open())
    {
        printf("Input file is invalid\n");
    }
    getline(inFile, line);
    //std::istringstream ss(line);
    ss << line;

    ss >> T;
    ss.clear();

    cout << T << endl;

    for (int case_ = 0; case_ < T; case_++ ){
        getline(inFile, line);
        std::stringstream stream(line);
        int count = 0;
        int N, M;
        while(1) {
           int n;
           stream >> n;
           if(!stream)
              break;
           if (count==0) N = n;
           else M = n;
           count ++;

        }
        cout << "N: " << N<< ", M:" << M << endl;
        int **dynamicArray = 0;
        int ROWS = N; int COLS = M;
        dynamicArray = new int *[ROWS] ;
        for( int i = 0 ; i < ROWS ; i++ )
        dynamicArray[i] = new int[COLS];
        int *colsMax = new int[COLS];
        int *rowsMax = new int[ROWS];
        for (int  r = 0; r < ROWS; r++ ){
            count = 0;
            getline(inFile, line);
            std::stringstream stream(line);
            //cout << line << endl;
            while(1) {
               int n;
               stream >> n;
               //cout << "ldl "<< n <<" ";
               if(!stream)
                  break;
                  dynamicArray[r][count] = n;
               count ++;
            }
        }
        //printArr(dynamicArray, ROWS, COLS);
        for( int i = 0 ; i < ROWS ; i++ ) rowsMax[i] = getMaxRows(dynamicArray[i], COLS);
        for( int i = 0 ; i < COLS ; i++ ) colsMax[i] = getMaxCols(dynamicArray, ROWS,i);
        //cout << "ooooooooooooooooo" << endl;
        //printArr(rowsMax,ROWS);
        //printArr(colsMax, COLS);
        int res = checkArr(dynamicArray,ROWS, COLS, rowsMax, colsMax);

        string yes("YES");
        string no("NO");
        string resLine("Case #");
        stringstream s2;
        s2 << case_+1;
        //ss.str();
        resLine.append(s2.str()).append(": ");
        s2.clear();
        cout << case_+1 << endl;
        if (res == 1) {
            cout << yes << endl;
            resLine.append(yes);
        } else {
            cout << no << endl;
            resLine.append(no);
        }
        resLine.append("\n");
        outputStr.push_back(resLine);


        for( int i = 0 ; i < ROWS ; i++ ) delete [] dynamicArray[i];
        delete [] dynamicArray ;
        delete [] colsMax;
        delete [] rowsMax;
    }
    inFile.close();
    fstream plik( "output.in", ios::out );

    for (int i = 0; i < T; i++){
        plik << outputStr.at(i);
    }
    plik.close();
    return 0;
}
int getMaxRows(int *t, int s){
    int max = 0;
    for (int i = 0; i < s; i++){
        if (t[i] > max) max = t[i];
    }
    return max;
}
int getMaxCols(int **t, int s,int ind){
    int max = 0;
    for (int i = 0; i < s; i++){
        if (t[i][ind] > max) max = t[i][ind];
    }
    return max;
}
void printArr(int **a, int n, int m){
    for( int i = 0 ; i < n ; i++ ){
        for( int j = 0 ; j < m ; j++ ){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}
int checkArr(int **a, int r, int c, int *rMax, int *cMax){
    for( int i = 0 ; i < r ; i++ ){
        for( int j = 0 ; j < c ; j++ ){
            if (a[i][j] < rMax[i] && a[i][j] < cMax[j]) return 0;
        }
    }
    return 1;// mozna
}
void printArr(int *a, int n){
    for( int i = 0 ; i < n ; i++ ){
        cout << a[i] << " ";
    }
    cout << endl;
}
