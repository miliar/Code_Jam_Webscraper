//
//  main.cpp
//  GCodeJams
//
//  Created by Ahmed SALMI on 08/04/2016.
//  Copyright © 2016 Ahmed SALMI. All rights reserved.
//
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <sstream>
using namespace std;
int tester(int *v){
    for(int i=0;i<10;i++)
        if(v[i]==0)
            return 0;
    
    return 1;
}
void printva(int *v){
    for(int i=0;i<10;i++)
    {
        cout << v[i] << " ";
    }
    cout << endl;
}
void resoudre(int N,int Ca){
    stringstream ss;
    int S=N;
    int v[10];
    for(int i=0;i<10;i++)
    {v[i]=0;}
    
    int soluce =0;
    
    if(N==0)
    {
        cout <<"Case #"<< Ca+1 << ": INSOMNIA" << endl;
    }
    else{
            while(!soluce){
                ss.str(to_string(S));
                string myS = ss.str();
                
                for(int i=0;i<10;i++)
                {
                    if(v[i]==0){
                        char *pch;
                        pch=strchr(myS.c_str(), to_string(i).c_str()[0]);
                        
                 //      cout << "myS" << myS << "i" <<to_string(i) << endl;
                       
                        if(pch!=NULL)
                        {v[i]=1;
                            //cout << "entrer ici" << endl;
                        }
                    }
                }
               // printva(v);
                //cout << tester(v) << " res test " <<endl;
                //cout << "S " << ss.str()<< endl;
                if(tester(v)){
                    soluce = 1;
                    cout <<"Case #"<< Ca+1 << ": "<< S << endl;
                        
                }
                S=S+N;
                    
                
            }
    }
    
}

int main(int argc, const char * argv[]) {
    // insert code here...
    int nbCase =0;
    int v[10];
    for(int i=0;i<10;i++)
        v[i]=0;
    int N=0;
    string file_t(argv[1]);
    ifstream  file (file_t.c_str());
    //file.open(argv[0]);
    if(file.fail()){
        cout << "le fichier " << file_t << " n existe pas " << endl;
        
    }else{
        file >> nbCase;
        //cout << nbCase << endl;
        
        for (int i=0;i<nbCase;i++){
            
            file >> N;
            //cout << "N " << N << "NbCase "<<nbCase << endl;
            resoudre(N,i);
            
            
        }
        file.close();
    }
        
    
  
    return 0;
}
