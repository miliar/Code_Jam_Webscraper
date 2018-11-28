#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
    int TestCases = 0;
    ofstream fout ("A-small-attempt3.out");
    ifstream fin ("A-small-attempt3.in");
    string Matrix [4];
    fin>>TestCases;
    
    for(int i=0;i<TestCases;i++){
            int xRow = 0, oRow = 0, xColm = 0, oColm = 0;
            bool xBool = false, oBool = false, DotBool = false;
            fin>>Matrix[0];
            fin>>Matrix[1];
            fin>>Matrix[2];
            fin>>Matrix[3];
            
            for(int j=0;j<4;j++){
                    xRow = oRow = xColm = oColm = 0;
                    for(int k=0;k<4;k++){
                            if(Matrix[j][k]=='.'&&!DotBool){
                                                            DotBool = 1 ;
                            }
                            if(Matrix[j][k]=='X'||Matrix[j][k]=='T'){
                                 xRow++;
                            }
                            if(Matrix[j][k]=='O'||Matrix[j][k]=='T'){
                                 oRow++;     
                            }
                            if(Matrix[k][j]=='X'||Matrix[k][j]=='T'){
                                 xColm++;
                            }
                            if(Matrix[k][j]=='O'||Matrix[k][j]=='T'){
                                 oColm++;
                            }
                    }
                    if(xRow==4 || xColm==4){
                         xBool = 1;
                         break;
                    }
                    else if(oColm==4 || xColm==4){
                         oBool = 1;
                         break;                         
                    }
            }
            if(!xBool && !oBool){
                                xRow = oRow = 0;
                         for(int j=0;j<4;j++){
                                 if(Matrix[j][j]=='X'||Matrix[j][j]=='T'){
                                                                          xRow++;
                                 }
                                 if(Matrix[j][j]=='O'||Matrix[j][j]=='T'){
                                                                          oRow++;     
                                 }
                         }
                         if(xRow == 4){
                                    xBool = 1;
                         }
                         else if(oRow == 4){
                              oBool = 1;                       
                         }    
            }
            if(xBool && !oBool){
                     fout<<"Case #"<<i+1<<": X won\n";
            }
            else if(oBool && !xBool){
                 fout<<"Case #"<<i+1<<": O won\n";
            }
            else if(!oBool && !xBool && !DotBool){
                 fout<<"Case #"<<i+1<<": Draw\n";
            }
            else if(!oBool && !xBool && DotBool){
                 fout<<"Case #"<<i+1<<": Game has not completed\n";
            }
            
    }
    fin.close();
    fout.close();
    return 0;    
}
