#include<iostream>
#include<math.h>
#include<string>
#include<vector>
#include<fstream>

using namespace std;

int main(){
    ifstream fin("A-small-attempt0.in");
    ofstream fout("A-small-attempt0.out");
    int t,ans1,ans2;
    fin >> t;
    //vector<string> s;
    int a1[4][4],a2[4][4];
   // int time2[4];//,time2[4];
    int countt=0,numb;
    for(int i=0;i<t;++i){
        fin >> ans1;
        for(int j=0;j<16;++j){
            fin >> a1[j/4][j&3];\
        }
        fin >> ans2;
        for(int j=0;j<16;++j){
            fin >> a2[j/4][j&3];
        }
        for(int h=0;h<4;++h){
            for(int g=0;g<4;++g){
                //cout << '+' << a1[ans1-1][g]<< '-' << a2[ans2-1][h];
                if(a1[ans1-1][g] == a2[ans2-1][h]){
                   // cout << '+' << a1[ans1-1][g];
                    countt++;
                    numb=a1[ans1-1][g];
                }
            }
        }
        //cout <<' ';
        //cout << countt << endl;
        if(countt == 1){
            fout << "Case #" << i+1<< ": "<<numb;
        }
         if(countt == 0){
                fout << "Case #" << i+1<<": Volunteer cheated!";
        }
        if (countt >1){
                fout << "Case #" <<i+1<<": Bad magician!";
        }
        fout << endl;
        countt=0;

    }
return 0;
}
