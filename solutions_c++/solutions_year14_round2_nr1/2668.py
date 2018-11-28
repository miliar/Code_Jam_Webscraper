#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <iostream>
#include <string>
#include <sstream>
#include <iomanip>
#include <vector>

using namespace std;

typedef long long ll;

int main(){

    int T;
    cin >> T;
    //cout << T << endl;

    int N;
    string tempstr;
    vector<string> strs;
    int *pos, *charcount;
    int avg;
    ll moves;
    char current;

    for(int i=1;i<=T;i++){

        //cout << i << endl;
        cin >> N;
        //cout << N << endl;
        //strs = (string*)malloc(N*sizeof(string));
        for(int j=0;j<N;j++){
            cin >> tempstr;
            strs.push_back(tempstr);
            //cout << strs[j] << endl;
        }
        pos = (int*)malloc(N*sizeof(int));
        charcount = (int*)malloc(N*sizeof(int));
        for(int j=0;j<N;j++) pos[j]=0;
        moves = 0;
        while(pos[0]<strs[0].length()){
            current=strs[0].at(pos[0]);
            for(int j=0;j<N;j++){
                charcount[j]=0;
                while((pos[j]<strs[j].length())&&(strs[j].at(pos[j])==current)){
                    charcount[j]++;
                    pos[j]++;
                }
                if(charcount[j]==0) moves=-1;
            }
            if(moves==-1){
                pos[0]=strs[0].length();
            }else{
                avg=0;
                for(int j=0;j<N;j++) avg+= charcount[j];
                //cout << avg;
                avg=(int)round((avg+0.0)/N);
                //cout << " " << avg << endl;
                for(int j=0;j<N;j++) moves+=abs(charcount[j]-avg);
            }
        }
        if(moves>=0){
            for(int j=0;j<N;j++) if(pos[j]<strs[j].length()) moves=-1;
        }


        cout << "Case #" << i << ": ";

        if(moves>=0){
            cout << moves;
        }else{
            cout << "Fegla Won";
        }

        cout << endl;
        //free(strs);
        strs.clear();
        free(pos);
        free(charcount);
    }

    return 0;
}
