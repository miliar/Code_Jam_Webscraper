/*
*	Nick: Varaquilex
*	Name: Volkan İlbeyli
*	Mail: volkan@ilbeyli.info
*/


#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <list>

using namespace std;

/// STL typedefs ///
//1D vectors
typedef vector<int> vi;
typedef vector<double> vd;
//iterators
typedef vector<int>::iterator viit;
typedef vector<double>::iterator vdit;


//STL macros
#define IterateJ for(j = 0 ; j < 4 ; j++)
#define IterateK for(k = 0 ; k < 4 ; k++)
#define whole(v) v.begin(), v.end()

bool checkRow(char[4], int&);

int main(int argc, char** argv) {

    FILE* fp, *out;
//    fp = fopen(argv[1], "r");
//    if(fp == NULL){
//        cout << "error opening file: " << argv[1] << endl;
//        return -1;
//    }

    fp = fopen("a-small.in", "r");
    if(fp == NULL){
        cout << "error opening file: " << endl;
        return -1;
    }
    
    string line;
    int n;
    char table[4][4];
    char lineBuffer[127];
    fscanf(fp, "%d\n", &n);
    int j, k;
    for(int i = 0 ; i < n ; i++){
        for(j = 0; j<4 ; j++){
            fscanf(fp, "%s", lineBuffer);
            for(k=0 ; k<4 ; k++)
                table[j][k] = lineBuffer[k];
        }
        
        //check winner
        int l;
        bool X = false, O = false;
        int dotCount = 0;
        char test;
        IterateJ{
            IterateK{
                if(k==0 && j==0){ //control 1st row, 1st column, diagonal
                    test = table[j][k];
                    if(test == 'T') test = table[j][k+1];
                    if(test == '.'){ dotCount ++; continue; }
                    if(checkRow(table[j], dotCount) == true){  //win row
                       cout << i << " WON!! row " << endl;
                       goto Winner;
                   }
                   else{    //check column
                       for(l = 1 ; l < 4 ; l++){
                           //cout << "comparing(col)[" << l << "] with " << table[l][k] << endl;
                           if(test == 'T') test = table[l][k];
                           if(table[l][k] == test || table[l][k] == 'T')
                               continue;
                           else
                               break;
                       }
                   }
                   if(l == 4){  //win column
                       cout << i << " WON!! column" << endl;
                       goto Winner;
                   }
                   else{    //check diag downwards
                       for(l = 1 ; l < 4 ; l++){
                           //cout << "comparing(diag)[" << l << "] with " << table[l][l] << endl;
                           if(test == 'T') test = table[l][l];
                           if(table[l][l] == test || table[l][l] == 'T')
                               continue;
                           else
                               break;
                       }
                   }
                   if(l==4){ //win diagonal
                       cout << i << " WON!! diagonal" << endl;
                       goto Winner;
                   }
                   else
                       continue;
                }
                else if(j==0 && k!=0){ //check for 1st row, column-wise
                    test = table[j][k];
                    //cout << i << " [" << j << "][" << k << "]: " << test << endl;
                    if(test == '.'){ dotCount ++; continue; } 
                    if(test == 'T') test = table[l][k];
                    for(l=1 ; l<4 ; l++){
                        //cout << "comparing(col)[" << l << "] with " << table[l][k] << endl;
                        if(test == table[l][k] || test == 'T')
                            continue;
                        else
                            break;
                    }
                    if(l==4){
                        cout << "WON!! col" << endl;
                        goto Winner;
                    }
                }
            }   //end of 1st row control
            test = table[j][0]; //check other rows now (only row check)
            if(test == 'T') test = table[j][1];
            if(checkRow(table[j], dotCount) == true){
                cout << "WON!! row12  " << j << endl;
                goto Winner;
            }
            if(j==3){   //check last rows diagonal upwards
                test = table[j][0];
                if(test == 'T') test = table[2][1];
                if(test == '.') continue;
                int a,b;
                for(a=2, b=1 ; a>=0 && b<=3 ; a--, b++){
                    if(test == table[a][b])
                        continue;
                    else
                        break;
                }
                if(a==-1 && b==4){  //diagonal check wins
                    cout << "WON!! upwards diag" << endl;
                    goto Winner;
                }
            }
        }
        if(j == 4){ //no one wins.
            cout << "no win" << endl << endl;
            out = fopen("a-small.out","a");
            if(out == NULL){
                cout << "error opening out file" << endl;
                return -1;
            }
            if(dotCount == 0)
                fprintf(out,"Case #%d: Draw\n", i+1);
            else
                fprintf(out, "Case #%d: Game has not completed\n", i+1);
            fclose(out);
            continue;
        }
        Winner:
        out = fopen("a-small.out","a");
        if(out == NULL){
            cout << "error opening out file" << endl;
            return -1;
        }
        fprintf(out,"Case #%d: %c won\n",i+1,test);
        fclose(out);
        cout << "Winner of Case#" << i+1 << " is: " << test << endl;
        cout << endl;
    }    
    fclose(fp);
            
    return 0;
}

bool checkRow(char row[4], int& dotCount){
    int l;
    char test = row[0];
    if(test == 'T') test = row[1];
    if(test == '.'){ 
        dotCount ++; 
        return false;
    }
    for(l = 1 ; l < 4 ; l++){
        //cout << "comparing(row)[" << l << "] with " << row[l] << endl;
        if(row[l] == test || row[l] == 'T')
            continue;
        else
            break;
    }
    if(l==4)
        return true;
    
    return false;
}