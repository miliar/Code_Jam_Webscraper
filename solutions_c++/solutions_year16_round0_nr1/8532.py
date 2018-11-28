#include <bits/stdc++.h>

using namespace std;
int flag[10];
int bts=0;
void sum(){
    bts = 0;
    for(int j = 0; j < 10; j++)
        bts += flag[j];
}
void found(string str){
                if(str.find("0") != string::npos)
                    flag[0] = 1;
                if(str.find("1") != string::npos)
                    flag[1] = 1;
                if(str.find("2") != string::npos)
                    flag[2] = 1;
                if(str.find("3") != string::npos)
                    flag[3] = 1;
                if(str.find("4") != string::npos)
                    flag[4] = 1;
                if(str.find("5") != string::npos)
                    flag[5] = 1;
                if(str.find("6") != string::npos)
                    flag[6] = 1;
                if(str.find("7") != string::npos)
                    flag[7] = 1;
                if(str.find("8") != string::npos)
                    flag[8] = 1;
                if(str.find("9") != string::npos)
                    flag[9] = 1;
}
void cero(){
    for(int j = 0; j < 10; j++)
        flag[j]=  0;
}
main(){
    int T, N, n;
    cin >> T;

    for(int k = 1; k<=T; k++){
        cin >> N;
        n = N;
        if(N == 0){
            cout <<"Case #"<< k <<": INSOMNIA" << endl;
        }else{
            for(int i=1; i <= 1000000; i++){
                stringstream ss;
                ss << n;
                string abc = ss.str();
                found(abc);
                sum();

                if(bts == 10){
                    cout <<"Case #"<< k <<": "<< n << endl;
                    cero();
                    break;
                }
                n = N*i;
            }
        }
    }
}


