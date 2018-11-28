#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include<math.h>
#include <string>



using namespace std;
bool isbreak;
unsigned long long num[33];
unsigned long long jset[501];
unsigned long long notprimenum[10];
int numofN;
bool notprime=true;
unsigned long long tenbase;
unsigned long long base;
unsigned long long prime=2;
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
        int k,c,s;
        cin>>k>>c>>s;
        for(int i=1;i<=k;i++){
            cout<<i<<" ";
        }
        cout<<endl;
        
        //cout <<numofN<< endl;
    }
    exit(0);
    
}
