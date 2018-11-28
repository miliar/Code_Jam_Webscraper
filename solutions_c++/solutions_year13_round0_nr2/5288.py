#include <algorithm>
#include <iostream>
#include <vector>
#include <cmath>
#include <numeric>
#include <stdio.h>
using namespace std;

int program(int N, int M, int casee){
    int  data[N][M];
    bool pass[N][M];
    vector <int> notN;
    vector <int> notM;
    int largest = 0;
    for(int i = 0; i < N; i++){
        for(int j = 0; j < M; j++){
            cin >> data[i][j];
            if (data[i][j]> largest)
                largest = data[i][j];
            pass[i][j]= false;
        }
    }

    while(true){
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(data[i][j] == largest){
                    notN.push_back(i);
                    notM.push_back(j);
                    pass[i][j] = true;
                }
            }
        }
        sort(notN.begin(),notN.end());
        sort(notM.begin(),notM.end());
        notN.erase( unique( notN.begin(), notN.end() ), notN.end() );
        notM.erase( unique( notM.begin(), notM.end() ), notM.end() );
        largest--;

        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(pass[i][j] != true){
                   goto k;
                }
            }
        }
            cout << "Case #"<< casee+1 <<": YES" << endl;
            return 0;
        k:


        for(int i = 0; i < notN.size(); i++){
            for(int j = 0; j < notM.size(); j++){
                if(pass[notN[i]][notM[j]] != true){
                   cout << "Case #"<< casee+1 <<": NO" << endl;

                    return 0;
                }
            }
        }
    }
}

int main(){

        int T, N, M;

        cin >> T;

        for(int i = 0; i < T;i++){
            cin >> N;
            cin >> M;
            program(N,M,i);

        }




}
