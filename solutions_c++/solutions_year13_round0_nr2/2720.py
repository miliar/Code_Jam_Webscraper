#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool check(const int*, const int, const int, const bool);

int main(int argc, const char * argv[])
{
    ifstream fin;
    ofstream fout;
    fin.open("B-small-attempt2.in");
    fout.open("B-small.out");
    
    int T, N, M;
    fin >> T;
    
    for(int i = 1; i <= T; i++){
        fin >> N >> M;
        int* lawn0 = new int[N*M+1];
        
        for(int j = 0; j < N*M; j++)
            fin >> lawn0[j];
        
    
        fout << "Case #" << i << ": ";

        if(check(lawn0, N, M, true) && (check(lawn0, N, M, false)))
            fout << "YES";
        else
            fout << "NO";
        fout << endl;

        delete lawn0;
    }
    
    
    fout.close();
    fin.close();
    return 0;
}

bool check(const int* lawn, const int N, const int M, const bool dir){
    for(int offset = 0; offset < (dir?(N*M):M); dir?(offset+=M):(offset++)){
        for(int i = 0; i < (dir?M:(N*M)); dir?(i++):(i+=M)){
            if(lawn[offset + i] > lawn[offset]){
                for(int j = 0; j < (dir?(N*M):M); dir?(j+=M):(j++))
                    if(lawn[offset] < lawn[j])
                        return false;
            }
            else if(lawn[offset + i] < lawn[offset]){
                for(int j = 0; j < (dir?(N*M):M); dir?(j+=M):(j++)){
                    if(lawn[offset + i] < lawn[i + j])
                        return false;
                }
            }
        }
    }
    return true;
}