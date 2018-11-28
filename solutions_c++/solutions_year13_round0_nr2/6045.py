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

typedef vector< vector<int> > vvi;
typedef vector<int> vi;
//STL macros
#define Iterate(it,c) for(__typeof(c.begin()) it = c.begin() ; it != c.end() ; it++)
#define whole(v) v.begin(), v.end()

bool checkRow(int* row, int size);
bool checkCol(vector< vector<int> >&, int, int);

int main(int argc, char** argv) {

//    if (argc != 1) { //program input error check
//        cout << "Invalid argument count." << endl;
//        cout << "Example: ./a.out **FORMAT**" << endl;
//        cout << "Returning from main()..." << endl;
//        return -1;
//    }
    FILE* fp, *out;
    
    fp = fopen("b-small.in","r");
    if(fp == NULL){
        cout << "error opening file: " << endl;
        return -1;
    }
    out = fopen("b-small.out","w");
    if(out == NULL){
        cout << "error opening file: " << endl;
        return -1;
    }
    
    int n;
    fscanf(fp, "%d\n", &n);
    
    for(int i=0 ; i<n ; i++){
        int a,b,j,k;
        fscanf(fp, "%d %d\n", &a, &b);
        fprintf(out, "Case #%d: ",i+1);
        vvi vtable;
        vi row;
        
        //allocate table
        int** table;
        table = new int*[a];
        for(j=0; j<a ; j++){
            table[j] = new int[b];
        }
        cout << a << " " << b << endl;
        
        //read from file
        for(j = 0 ; j < a ; j++){
            for(k = 0 ; k < b ; k++){
                if( k != b-1)
                    fscanf(fp,"%d ",&table[j][k]);
                else
                    fscanf(fp,"%d\n",&table[j][k]);
                row.push_back(table[j][k]);
            }
            vtable.push_back(row);
            row.clear();
        }
        /*
        Iterate(it,vtable){
            Iterate(ite, (*it)){
                cout << *ite << " ";
            }
            cout << endl;
        }*/

        //algorithm
        bool result = true;
        for(j = 0 ; j < a ; j++){
            for(k = 0 ; k < b ; k++){
                cout << "j = " << j << "  k = " << k << endl;
                if(k != 0 && table[j][k] == 1){
                    if(checkCol(vtable, j, k) == false){
                        cout << "NO" << endl;
                        result = false;
                        break;
                    }
                    else{
                        cout << "no problem  " << endl;
                    }
                }
                else if(k==0 && table[j][k] == 1){
                    cout << "checking row " << endl;
                    if(checkRow(table[j], b) == true){
                        if(j != a-1){ 
                            j++;    //next row
                            k=-1;
                            cout << "continue" << endl;
                            continue;
                        }
                        else{
                            break;
                        }
                    }
                    else{
                        if(checkCol(vtable, j, k) == false)
                            result= false;
                    }
                }
            }
            if(result == false) break;
            //if(j==a-1 && result ==true) {fprintf(out, "YES\n"); break; }
        }
        
        cout << endl << "Result for case #" << i+1 << " is " << result << endl;
        if(result == true)
            fprintf(out, "YES\n");
        else
            fprintf(out,"NO\n");
        
        //deallocate table
        for(int j=0; j<a ; j++){
            delete table[j]; 
        }
        delete table;
        vtable.clear();
    }

    fclose(fp);
    fclose(out);
    return 0;
}

bool checkRow(int* row, int size){
    
    for(int i = 0 ; i < size ; i ++){
        if(row[i] != 1)
            return false;
    }
    return true;
}
bool checkCol(vector< vector<int> >& v, int r, int c){
    int rowSize = v.size();
    cout << "checking col:" << c << " row:" << r << endl;
    //go upwards
    for(int i=r ; i>=0 ; i--){
        cout << "comparing w u v[" << i << "][" << c << "] = " << v[i][c] << endl;
        if(v[i][c] != 1)
            return false;
    }
    
    //go downwards
    for(int i=r ; i<rowSize ; i++){
        cout << "comparing w d v[" << i << "][" << c << "] = " << v[i][c] << endl;
        if(v[i][c] != 1)
            return false;
    }
    return true;
}