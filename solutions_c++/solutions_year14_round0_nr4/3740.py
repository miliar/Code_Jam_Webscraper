#include<iostream>
#include<fstream>
#include<sstream>
#include<vector>
#include<stdio.h>
#include<algorithm>
using namespace std;

int main(int argc, char* argv[]){
    char* filename = argv[1];
    //cout << filename << endl;
    fstream fp;
    int T;

    fp.open(filename, ios::in);
    if(!fp){
        cout <<"fail to open" << filename <<endl;
    }
    fp >> T ;

    int N;
    for(int t=0; t<T; t++){
        fp >> N;
        vector<double> Naomi(N);
        vector<double> Ken(N);
        for(int i=0;i<N;i++)
            fp >> Naomi[i];
        for(int i=0;i<N;i++)
            fp >> Ken[i];
        sort(Naomi.begin(),Naomi.end());
        sort(Ken.begin(),Ken.end());


        int score =0;
        int d_score =0;

        // war
        vector<int> flag(N);
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(flag[j] == 0 && Ken[j] > Naomi[i]){
                    flag[j] = 1;
                    score +=1;
                    break;
                }
            }
        }
        score = N - score;
        //deceived war
        vector<int> flag2(N);
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(flag2[j] == 0 && Ken[j] < Naomi[i]){
                    flag2[j] = 1;
                    d_score +=1;
                    break;
                }
            }
        }
        //d_score = N- d_score;

        printf("Case #%d: %d %d\n",t+1,d_score,score);
        /*
        for(int i=0;i<N;i++)
            cout <<  Naomi[i] <<" ";
        cout << endl;
        for(int i=0;i<N;i++)
            cout <<  Ken[i] <<" ";
        cout << endl;
        */
    }


    return 0;
}
