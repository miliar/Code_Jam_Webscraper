/* 
 * File:   main.cpp
 * Author: tamer
 *
 * Created on April 13, 2013, 2:03 AM
 */

#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

/*
 * 
 */
bool testCase(vector< vector <int> > &matrix);
bool check(vector< vector <int> > & matrix, int i,int  j);

int main(int argc, char** argv) {

    int N,M,T;
    char* yes="YES\0";
    char* no="NO\0";
    
    char str [80];
    FILE * pFile;
    FILE * oFile;    
    
    pFile = fopen ("/Users/tamer/Desktop/B-large.in","r");
    oFile = fopen ("/Users/tamer/Desktop/out.txt","w+");
    fscanf (pFile, "%d", &T);
    
    for(int t=1;t<=T;t++){
        fscanf (pFile, "%d %d\n", &N,&M);
        vector< vector <int> > lawn =   vector<vector<int> >(N, vector<int>(M, 100));
        for(int n=0;n<N;n++){
            for(int m=0;m<M;m++){
                fscanf (pFile, "%d", &lawn[n][m]);
//                cout<< lawn[n][m]<< " ";
            }
//            cout<<endl;
        }
        

        if(testCase(lawn)==true)
            fprintf (oFile, "Case #%d: %s\n", t, yes);
        else
            fprintf (oFile, "Case #%d: %s\n", t, no);
    }
    
    fclose (oFile);
    fclose (pFile);
    return 0;
}

bool testCase(vector< vector <int> > &matrix){
    double N=matrix.size();
    double M=matrix[0].size();
    for(int i=0;i<N;i++){
        for(int j=0;j<M;j++){
            if(!check(matrix,i,j))
                return false;
        }
    }
    return true;
}

bool check(vector< vector <int> > & matrix, int i,int  j){
    double N=matrix.size();
    double M=matrix[0].size();
    bool rowCheck=true,colCheck=true;
    for(int n=0;n<N;n++){
        if(matrix[n][j]>matrix[i][j]){
            colCheck=false;
            break;
        }
    }
    
    if(colCheck==true)
        return true;
    for(int m=0;m<M;m++){
        if(matrix[i][m]>matrix[i][j]){
            rowCheck=false;
            break;
        }
    }
    
    return rowCheck;
    
}