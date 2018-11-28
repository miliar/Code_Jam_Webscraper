#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
using namespace std;

int main(){
	ifstream input;
	input.open("B-large.in");
	ofstream output("out.txt");
	int casenum;
    input >> casenum;
	//for each case
	for (int k=0;k<casenum;k++){
        int m;
        int n;
        int board[100][100];
        input >> n;
        input >> m;
        for (int i=0; i< n; i++){
            for (int j=0;j<m;j++){
                input >> board[i][j];
            }
        }

        bool res =true;
        for (int i=0;i<n;i++){
            for (int j=0;j<m;j++){
                    //check row
                    bool row = true;
                    for (int ii=0;ii<m;ii++){
                        if (board[i][ii]>board[i][j]){row = false; break;}
                    }
                    //check column
                     bool column = true;
                    for (int ii=0;ii<n;ii++){
                        if (board[ii][j]>board[i][j]){column = false; break;}
                    }

                    if ((column||row)==false){
                        res=false;
                        goto pr;
                    }
                }
        }


     pr:if (res){
        output << "Case #" << k+1 << ": " << "YES" <<endl;
        }else{
        output << "Case #" << k+1 << ": " << "NO" <<endl;
        }
    }
    input.close();
    output.close();
}
