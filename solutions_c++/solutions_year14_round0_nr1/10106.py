/*  Problem A. Magic Trick  */

#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);

    int t, i, j, k, no;
    int col1, col2;
    int c = 0;
    int a1[4][4];
    int a2[4][4];
    cin>>t;

    for(i = 0; i<t; i++){
        cin>>col1;      //answer to first question
        for(j = 0; j<4; j++){
            for(k = 0; k<4; k++){
                cin>>a1[j][k];
            }
        }
        cin>>col2;      //answer to second question
        for(j = 0; j<4; j++){
            for(k = 0; k<4; k++){
                cin>>a2[j][k];
            }
        }
        for(j = 0, c = 0; j<4; j++){
            for(k = 0; k<4; k++){
                if(a1[col1 - 1][j] == a2[col2 -1][k]){
                    no = a1[col1 - 1][j];
                    c++;
                    break;
                }
            }
        }
        if(c == 1){
            cout<<"Case #"<<i+1<<": "<<no<<endl;
        }else if(c > 1){
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }else{
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        }
    }
    return 0;
}
