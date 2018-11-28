//
//  main.cpp
//  pancakes
//
//  Created by Dziugas Simaitis on 09/04/16.
//  Copyright © 2016 Dziugas Simaitis. All rights reserved.
//

#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char * argv[]) {
    ifstream cin("B-large.in");
    ofstream cout("pancakes.out");
    int n;
    cin>>n;
    for(int y=1; y<=n; y++){
        int s;
        string eina;
        cin>>eina;
        s=int(eina.length());
        int jau_kiek=0;
        bool blynai[s];
        for(int i=0; i<s; i++){
            if(eina[i]=='+'){
                blynai[i]=true;
            } else{
                blynai[i]=false;
            }
            
        }
        bool win=false;
        while(!win){
            win=true;
            for(int t=0; t<s; t++){
                if(!blynai[t])
                    win=false;
            }
            if(win)
                break;
            int i=s-1, geri=0;
            while(blynai[i]){
                geri++;
                i--;
            }
            //cout<<"geri:"<<geri<<endl;
            int skaicius=0;
            i=0;
            if(blynai[0]){
                //cout<<"pirmas"<<endl;
                while(blynai[i]){
                    i++;
                    skaicius++;
                }
                for(int r=0; r<skaicius; r++){
                    blynai[r]=false;
                }
                jau_kiek++;
            } else{
                //cout<<"du"<<endl;
                bool keitinys[s-geri];
                for(int u=0; u<s-geri; u++){
                    keitinys[u] = blynai[s-geri-1-u];
                }
                for(int u=0; u<s-geri; u++){
                    blynai[u] = !keitinys[u];
                }
                jau_kiek++;
            }
        }
        cout<<"Case #"<<y<<": "<<jau_kiek<<endl;
        
    }
    return 0;
}
