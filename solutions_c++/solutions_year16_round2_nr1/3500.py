#include <iostream>
#include <fstream>
#include <String>

using namespace std;

ifstream fin("digitsSmall.in");
ofstream fout("digitsSmall.out");

string arr[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int used[10];
int num[26];

bool check(){
    for(int i = 0; i < 26; i++){
        if(num[i] != 0){
            return false;
        }
    }
    return true;
}

void reset(){
    for(int i = 0 ; i < 26; i++){
        num[i] = 0;
    }
    for(int i = 0; i < 10; i++){
        used[i] = 0;
    }
}

int toInt(char c){
    return (int)c - 65;
}

bool canRem(int x){
    for(int i = 0; i < arr[x].size(); i++){
        if(num[toInt(arr[x][i])] <= 0){
            return false;
        }
    }
    return true;
}

void recurse(int cur){
    if(cur >= 10){
        return;
    }
    if(check()){
        for(int i = 0; i < 10; i++){
            for(int j = 0; j < used[i]; j++){
                fout<<i;
            }
        }
        fout<<"\n";
        return;
    }
    if(canRem(cur)){
        for(int i = 0; i < arr[cur].size(); i++){
            num[toInt(arr[cur][i])]--;
        }
        used[cur]++;
        recurse(cur);
        for(int i = 0; i < arr[cur].size(); i++){
            num[toInt(arr[cur][i])]++;
        }
        used[cur]--;

    }
    recurse(cur+1);
}

void calc(){
    string s;
    fin>>s;
    reset();
    for(int i = 0; i < s.size(); i++){
        num[toInt(s[i])]++;
    }
    recurse(0);
}

int main(){
    int T;
    fin>>T;
    for(int t = 1; t <= T; t++){
        fout<<"Case #"<<t<<": ";
        calc();
    }
}
