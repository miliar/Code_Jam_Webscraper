#include<iostream>
#include <fstream>
using namespace std;

ifstream fin("in.txt");
ofstream fout("out.txt");


int main(){

    int t;
    fin>>t;
    int ans[17];
    for( int cs = 1; cs <= t; cs++ ){
        for( int i = 0; i < 17; i++ ) ans[i] = 0;
        int board[4][4];
        int row;
        fin>>row;
        row--;
        for( int i = 0; i < 4; i++ )
            for( int j = 0; j < 4; j++ ) fin>>board[i][j];
        for( int i = 0; i < 4; i++ ){
            ans[ board[row][i] ]++;
        }


        fin>>row;
        row--;
        for( int i = 0; i < 4; i++ )
            for( int j = 0; j < 4; j++ ) fin>>board[i][j];

        int matchCount = 0, matchColumn = -1;

        for( int i = 0; i < 4; i++ ){
            if( ans[ board[row][i] ] == 1 ){
                matchCount++;
                matchColumn = board[row][i];
            }
        }

        if( cs > 1 ) fout<<endl;
        fout<<"Case #"<<cs<<": ";
        if( matchCount == 0 )fout<<"Volunteer cheated!";
        else if( matchCount > 1 ) fout<<"Bad magician!";
        else fout<<matchColumn;

    }


    return 0;
}
