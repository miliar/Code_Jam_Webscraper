#include <cstdio>
#include <vector>
#include <iostream>
using namespace std;

bool complete(vector<string> inp) {
    for(size_t i=0; i<inp.size(); i++) {
        for(size_t j=0; j<inp[i].size(); j++) {
            if(inp[i][j] == '.') return false;
        }
    }
    return true;
}

bool checkWin(vector<string> inp, char p) {
    // check row
    for(int i=0; i<4; i++) {
        int j;
        for(j=0; j<4; j++) {
            if(inp[i][j] != p && inp[i][j] != 'T') break;
        }
        if(j == 4) return true;
    }
    // check col
    for(int i=0; i<4; i++) {
        int j;
        for(j=0; j<4; j++) {
            if(inp[j][i] != p && inp[j][i] != 'T') break;
        }
        if(j == 4) return true;
    }
    // check diag
    int i;
    for(i=0; i<4; i++) {
        if(inp[i][i] != p && inp[i][i] != 'T') break;
    }
    if(i == 4) return true;
    for(i=0; i<4; i++) {
        if(inp[i][3-i] != p && inp[i][3-i] != 'T') break;
    }
    if(i == 4) return true;
    return false;
}

void print(vector<string> inp) {
    int i,j;
    for(i=0; i<4; i++) {
        for(j=0; j<4; j++) {
            cout<<inp[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main() {
    int t;
    vector<string> inp;
    cin>>t;
    string row;
    int tp = 0;
    while(t--) {
        tp++;
        cout<<"Case #"<<tp<<": ";
        inp.clear();
        for(int temp=0;temp<4; temp++) {
            cin>>row;
            inp.push_back(row);
        }
        
        
        if(checkWin(inp,'X')) {
            cout<<"X won"<<endl;
        } else if(checkWin(inp, 'O')) {
            cout<<"O won"<<endl;
        } else if(complete(inp)) {
            cout<<"Draw"<<endl;
        } else {
            cout<<"Game has not completed"<<endl;
        }
    }
    return 0;
}
