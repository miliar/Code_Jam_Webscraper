#include<sstream>
#include<fstream>
#include<string>
#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;

bool Col(int dic[10][10], int m, int n, int j){
    for(int i = 0; i < m; ++i){
        if(dic[i][j] != 1) return false;
    }
    return true;
}

bool Row(int dic[10][10], int n, int m, int j){
    for(int i = 0; i < m; ++i){
        if(dic[j][i] != 1) return false;
    }
    return true;
}

string result(int dic[10][10], int n, int m){
    for(int i = 0; i < n; ++i){
        for(int j = 0; j < m; ++j){
            if(dic[i][j] == 1){
                if(!Col(dic, n, m, j) && !Row(dic, n, m, i))
                    return "NO";
            }
        }
    }
    return "YES";
}

int main(){
int t, n, m;    
int ch;         
int dic[10][10];
int Casesno = 0;
ifstream fi("B-small-attempt1.in");
ofstream fo("x.out");     
fi>>t;

    while(t--){
        memset(dic, -1, sizeof(dic));
        fi>>n>>m;       
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < m; ++j){
                fi>>ch;
                dic[i][j] = ch;
            }
        }
        fo<<"Case #"<<++Casesno<<": "<<result(dic, n, m)<<endl;
    }

    return 0;
}
