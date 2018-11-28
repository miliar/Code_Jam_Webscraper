#include <iostream>
#include <fstream>
#define MAX_T 100
#define MAX_S 1000
using namespace std;

ifstream fin ("A-small-attempt0.in");
ofstream fout ("results.txt");
int T, shyness[MAX_S+1];

void read();
int solve(int s, int arr[MAX_S+1]);
void write(int caseNum, int ans);

int main(){
    read();
    return 0;
}

int solve(int s, int arr[MAX_S+1]){
    int soFar = arr[0], ans = 0;
    for(int i = 1; i < s; i++){
        if(arr[i] == 0) continue;
        if(i <= soFar){
            soFar += arr[i];
        }else{
            ans += i - soFar;
            soFar += ans + arr[i];
        }
    }
    return ans;
}

void read(){
    char c;
    int S;
    fin >> T;
    for(int i = 0; i < T; i++){
        fin >> S;
        for(int j = 0; j <= S; j++){
            fin >> c;
            shyness[j] = c - '0';
        }
        write(i, solve(S+1, shyness));
    }
    fin.close();
    fout.close();
}

void write(int caseNum, int ans){
    fout << "Case #" << caseNum+1 << ": " << ans << endl;
}
