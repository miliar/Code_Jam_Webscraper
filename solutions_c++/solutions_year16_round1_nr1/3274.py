#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include<vector>
#include<math.h>
#include <string>



using namespace std;
bool isbreak;
unsigned long long num[33];
unsigned long long jset[501];
char inputs[1001];
unsigned long long notprimenum[10];
int numofN;
bool notprime=true;
unsigned long long tenbase;
unsigned long long base;
unsigned long long prime=2;
char outputs[1001];
void moveback(int in){
    for(int i=1001;i>0;i--){
        outputs[i]=outputs[i-1];
    }
    outputs[0]=in;
}
void makenextnum(int n){
    if(num[n]==0){//0 so add 1.
        num[n]=1;
        return;
    }else{
        if(n==0){
            return;
        }
        num[n]=0;//make 1 to 0 and carryup
        makenextnum(n-1);
    }
    return;
}
int main() {
    FILE *fin = freopen("/Users/kimmyongjoon/Desktop/problem/A-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("/Users/kimmyongjoon/Desktop/problem/A-large9.out", "w", stdout);
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++){
        cout << "Case #" << t << ": ";
        char first;
        char last;
        cin>>inputs;
        int len=strlen(inputs);
        //cout<<inputs[0];
        first=inputs[0];
        last=inputs[0];
        outputs[0]=inputs[0];
        for(int i=1;i<len;i++){
            if(first<=inputs[i]){
                moveback(inputs[i]);
                first=inputs[i];
            }else {
                outputs[i]=inputs[i];
            }
        }
        for(int i=0;i<len;i++){
            cout<<outputs[i];
        }
        cout<<endl;
        
        //cout <<numofN<< endl;
    }
    exit(0);
    
}
