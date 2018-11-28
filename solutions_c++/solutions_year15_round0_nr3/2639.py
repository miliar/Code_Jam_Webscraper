//
//  main.cpp
//  GCJC
//
//  Created by Nathaniel Faulkner on 11/04/15.
//  Copyright (c) 2015 Nathaniel Faulkner. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>

using namespace std;

int N,L,X;
string expr;

class quatern{
public:
    char val;
    bool neg;
    quatern(char _val,bool _neg):val(_val),neg(_neg){};
    bool pos(int i);//if is positive i for 0, j for 1, k for 2
};

bool quatern::pos(int i){
    bool out = false;
    if (i==0 && val=='i' && !neg){
        out = true;
    }else if(i==1 && val=='j' && !neg){
        out = true;
    }else if(i==2 && val=='k' && !neg){
        out = true;
    }
    return out;
}

quatern operator*(const quatern &a,const quatern &b){
    bool negFlag = false;
    if ((a.neg&&!b.neg)||(b.neg&&!a.neg)){
        negFlag = true;
    }
    char valOut = 0;
    
    if (a.val=='1'){
        valOut = b.val;
    }else if(b.val=='1'){
        valOut = a.val;
    }else if(a.val==b.val){
        valOut = '1';
        negFlag=!negFlag;
    }else if(a.val == 'i'){
        if(b.val=='j'){
            valOut = 'k';
        }else if (b.val == 'k'){
            valOut = 'j';
            negFlag=!negFlag;
        }
    }else if(a.val == 'j'){
        if(b.val=='i'){
            valOut = 'k';
            negFlag=!negFlag;
        }else if (b.val == 'k'){
            valOut = 'i';
        }
    }else if(a.val == 'k'){
        if(b.val=='i'){
            valOut = 'j';
        }else if (b.val == 'j'){
            valOut = 'i';
            negFlag=!negFlag;
        }
    }
    
    if(valOut == 0){
        cout<<"error in mult func"<<endl;
    }
    
    return quatern(valOut, negFlag);
}

int main(int argc, const char * argv[]) {
    if (argc<2){
        cout<<"Needs input and output flags!";
        exit(EXIT_FAILURE);
    }
    
    string temp;
    
    ifstream fin(argv[1]);
    if(!fin.is_open())
    {
        cout<<"Unable to open input file"<<endl;
        cout<<argv[1];
        exit(EXIT_FAILURE);
    }
    
    ofstream fout(argv[2]);
    
    getline(fin,temp);
    N = atoi(temp.c_str());
    
    cout<<N<<" test cases following"<<endl;
    
    for(int i =0; i<N; i++){
        expr="";
        getline(fin,temp);
        stringstream  tempstream(temp);
        tempstream >> L;
        tempstream >> X;
        cout<<"L: "<<L<<" X: "<<X<<endl;
        getline(fin,temp);
        
        for(int numApps = 0; numApps<X;numApps++){
            expr.append(temp);
        }
        
        quatern lhs(expr[0], false);
        int current = 0;//if 0 i, if 1 j, if 2 k
        
        
        for(int jj = 1; jj <expr.size();jj++){
            if(lhs.neg)cout<<"-";
            cout<<lhs.val<<endl;
            if(lhs.pos(current)&&current <2){
                current++;
                lhs = quatern(expr[jj],false);
            }else{
                lhs = lhs*quatern(expr[jj], false);
            }
        }
        
        if(current==2 and lhs.pos(2)){
            fout<<"Case #"<<i+1<<": YES"<<endl;
        }else{
            fout<<"Case #"<<i+1<<": NO"<<endl;
        }
        
        
        /*
        for(int jj = 0; jj<sMax+1; jj++){
            if (tot<jj){
                extras+=jj-tot;
                tot = jj;
            }
            
            tot+=peopleLevels[jj]-'0';
        }
        
        fout<<"Case #"<<i+1<<": "<<extras<<endl;
        */
        
        
        //c = atoi(temp.c_str());
        
        
        /*
         getline(fin,temp);
         l = atoi(temp.c_str());
         cout<<"Number "<<i<<": credit - "<<c<<", number items - "<<l<<endl;
         getline(fin,temp);
         
         stringstream  tempstream(temp);
         int *tempArray = new int[l];
         for(int j = 0; j<l;j++){
         tempArray[j];
         //cout<<tempArray[j]<<" item number "<<j<<endl;
         }
         //code here
         
         for(int ii = 0;ii<l-1;ii++){
         for(int jj=ii+1;jj<l;jj++){
         if (tempArray[ii]+tempArray[jj] == c){
         fout<<"Case #"<<i+1<<": "<<ii+1<<" "<<jj+1<<endl;
         break;
         }
         
         }
         }
         
         delete [] tempArray;
         
         */
        
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}
