#include <iostream>
using namespace std;

int position(char c){
    if(c=='Z'){
        return 0;
    } else if(c=='O'){
        return 1;
    } else if(c=='W'){
        return 2;
    } else if(c=='T'){
        return 3;
    } else if(c=='F'){
        return 4;
    } else if(c=='V'){
        return 5;
    } else if(c=='X'){
        return 6;
    } else if(c=='S'){
        return 7;
    } else if(c=='G'){
        return 8;
    } else if(c=='I'){
        return 9;
    }
    return -1;
}

void phone(string S) {
    int C [10]= {0,0,0,0,0,0,0,0,0,0};

    for(int l=0;l<10;l++){
        C[l]=0;
    }

    int p=0;
    for(char& c : S) {
        p=position(c);
        if(p>=0){
            C[p]++;
        }
    }

    int r[10] = {0,0,0,0,0,0,0,0,0,0};

    r[0]=C[0];
    r[2]=C[2];
    r[6]=C[6];
    r[8]=C[8];
    r[7]=C[7]-r[6];
    r[5]=C[5]-r[7];
    r[4]=C[4]-r[5];
    r[3]=C[3]-r[2]-r[8];
    r[1]=C[1]-r[0]-r[2]-r[4];
    r[9]=C[9]-r[5]-r[6]-r[8];

    for(int l=0; l< 10;l++){
        for(int u=0; u<r[l]; u++){
            cout << l;
        }
    }
}

int main() {
  int t;
  string S;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cin >> S;
    cout << "Case #" << i << ": ";
    phone(S);
    cout << endl;
  }
}
