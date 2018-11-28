#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include<math.h>
#include <string>

#include "BigIntegerLibrary.hh"


using namespace std;
bool isbreak;
unsigned long long num[33];
unsigned long long jset[501];
unsigned long long notprimenum[10];
int numofN;
char input[101];
char tempa[101];
char tempb[101];
bool isproved;
bool notprime=true;
int NNNN=1;
int N;
unsigned long long tenbase;
unsigned long long base;
int nn[10];
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
        unsigned long long n;
        NNNN=1;
        cin>>n;
        for(int i=0;i<10;i++){
            nn[i]=0;
        }
        
        while(1){
            if(n==0){
                cout<<"Case #"<<t<<": "<<"INSOMNIA"<<endl;
                break;
            }
            long long te=NNNN*n;
            while(te>0){
                long long temppp=te%10;
                nn[temppp]=1;
                te=te/10;
            }
            isproved=true;
            for(int i=0;i<10;i++){
                if(nn[i]==0){
                    isproved=false;
                    break;
                }
            }
            if(isproved){
                cout<<"Case #"<<t<<": "<<NNNN*n<<endl;
                break;
            }
            NNNN++;
        }
        
    }
    exit(0);
    
}
