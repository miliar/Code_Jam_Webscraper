#include <iostream>
#include <bits/stdc++.h>
#include <String>
#include <map>
using namespace std;

int main(){
    freopen("A-large.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OutputA.txt", "w", stdout);
    int T,temp,length;
    int cF,cG,cH,cI,cO,cU,cV,cW,cX,cZ;
    int counter[9];
    string S;
    cin>>T;
    for(int i=1;i<=T;i++){
        cin>>S;
        length = S.size();
        cF = 0; cG = 0; cH = 0; cI = 0; cO = 0; cU = 0; cV = 0; cW = 0; cX = 0; cZ = 0;
        for(int m=0;m<9;m++)
            counter[m] = 0;
        cout<<"Case #"<<i<<": ";
        //cout<<S<<endl;
        //cout<<length<<endl;
        for(int j=0;j<length;j++){
            if (S[j] == 'F'){
                cF++;
                continue;
            }
            else if(S[j] == 'G'){
                cG++;
                continue;
            }
            else if(S[j] == 'H'){
                cH++;
                continue;
            }
            else if(S[j] == 'I'){
                cI++;
                continue;
            }
            else if(S[j] == 'O'){
                cO++;
                continue;
            }
            else if(S[j] == 'U'){
                cU++;
                continue;
            }
            else if(S[j] == 'V'){
                cV++;
                continue;
            }
            else if(S[j] == 'W'){
                cW++;
                continue;
            }
            else if(S[j] == 'X'){
                cX++;
                continue;
            }
            else if(S[j] == 'Z'){
                cZ++;
                continue;
            }
        }
        //cout<<cZ<<cX<<cW<<cU<<cG<<cH<<cF<<cV<<cO<<cI<<endl;
        while(cZ--){
            cout<<0;
            cO--;
        }
        while(cX--){
            counter[5]++;   //5-1
            cI--;
        }
        while(cW--){
            counter[1]++;
            cO--;
        }
        while(cU--){
            counter[3]++;
            cF--;
            cO--;
        }
        while(cG--){
            counter[7]++;
            cI--;
            cH--;
        }
        while(cH--){
            counter[2]++;
        }
        while(cF--){
            counter[4]++;
            cI--;
            cV--;
        }
        while(cV--){
            counter[6]++;
        }
        while(cO--){
            cout<<1;
        }
        while(cI--){
            counter[8]++;
        }
        for(int k=1;k<9;k++)
            while(counter[k]--)
                cout<<k+1;
        cout<<endl;
    }
    return 0;
}
