//
//  main.cpp
//  codejam_1
//
//  Created by Hasan Unlu on 11/04/15.
//  Copyright (c) 2015 Hasan Unlu. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;


                  //1 -1  i  j  k -i -j -k
int table[8][8]={ { 0, 1,   2, 3, 4,   5, 6, 7},
                  { 1, 0,   5, 6, 7,   2, 3, 4},
    
                  { 2, 5,   1, 4, 6,   0, 7, 3},
                  { 3, 6,   7, 1, 2,   4, 0, 5},
                  { 4, 7,   3, 5, 1,   6, 2, 0},
    
                  { 5, 2,   0, 7, 3,   1, 4, 6},
                  { 6, 3,   4, 0, 5,   7, 1, 2},
                  { 7, 4,   6, 2, 0,   3, 5, 1} };

void  disp(int i){
    switch(i){
            case 0: cout<<" 1";
            break;
            case 1: cout<<"-1";
            break;
            case 2: cout<<" i";
            break;
            case 3: cout<<" j";
            break;
            case 4: cout<<" k";
            break;
            case 5: cout<<"-i";
            break;
            case 6: cout<<"-j";
            break;
            case 7: cout<<"-k";
            break;
    }


}

int main(int argc, const char * argv[]) {
    
    string line;
    
    ifstream infile ("/Users/hasanunlu/Desktop/codejam_1/codejam_1/input.txt");
    ofstream outfile ("/Users/hasanunlu/Desktop/codejam_1/codejam_1/output.txt");
    
    if (!infile.is_open())
        cout << "Unable to open file";
    
    int T, L, X;
    
    getline (infile,line);
    
    T=atoi(line.c_str());
    
    cout << T << endl;
    
    
    for(int i=0; i<T; i++){
        
        getline (infile,line);

        char *input = const_cast<char*>(line.c_str());
        
        char *token = strtok(input, " ");
        
        L=atoi(token);
        
        token = strtok(NULL, " ");
        
        X=atoi(token);
        
        cout <<"L="<<L<<" X="<<X<<endl;
        
        getline (infile,line);
        
        int *subset;
        subset=new int[L];
        input = const_cast<char*>(line.c_str());

        
        for(int k=0; k<L;  k++){
            subset[k]=*(input++)-105+2;
            //cout<<subset[k]<<endl;
        }
        
        int *allset;
        allset=new int[L*X];
        int cnt=0;
        
        for(int j=0; j<X; j++){
            for(int k=0; k<L; k++){
                allset[cnt++]=subset[k];
            }
        }
        
        int result=allset[0];
        
        int state=0;
        
        cout<<"len="<<cnt<<endl;
        
        for(int j=1; j<cnt; j++){
 
            switch(state){
                case 0:
                    if(result==2){
                        state=1;
                        cout<<"i"<<endl;
                        result=allset[j];
                    
                    } else {
                        
                        result=table[result][allset[j]];
                    }
                    
                    //cout<<result<<" ";
                    
                break;
                case 1:
                    if(result==3){
                        
                        state=2;
                        cout<<"j"<<endl;
                        result=allset[j];
                        
                    } else {
                        
                        result=table[result][allset[j]];
                    }
                    
                    //cout<<result<<" ";
                break;
                case 2:
                    result=table[result][allset[j]];
                break;
            }
                
            
        }
        
        if(result==4 && state==2){
            cout<<"Case #"<<i+1<<": YES"<<endl;
            outfile<<"Case #"<<i+1<<": YES"<<endl;
        } else {
            cout<<"Case #"<<i+1<<": NO"<<endl;
            outfile<<"Case #"<<i+1<<": NO"<<endl;
        }
        //cout<<   "Case #"<<i+1<<": "<<diff<<endl;
        //outfile<<"Case #"<<i+1<<": "<<diff<<endl;
        

        cout<<"*******************************************"<<endl;
    }
    
    
    for(int i=0; i<8; i++){
        for(int j=0; j<8; j++){
            disp(table[i][j]);
            cout<<" ";
        
        }
        cout<<endl;
    }

    cout<<table[3][2]<<endl;
    infile.close();

    outfile.close();
    
    
    
    return 0;
}
