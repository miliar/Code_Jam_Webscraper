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
bool notprime=true;
int N;
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
        N=0;
        cout << "Case #" << t << ": ";
        int i=0;
        cin>>input;
        for(int i=0;i<strlen(input);i++){
            tempa[i]=input[i];
            tempb[i]=input[i];
        }
        int len=strlen(input);
        while(1){
            for(i=len-1;i>=0;i--){
                if(tempa[i]=='-'){
                    break;
                }
            }
            if(i==-1){
                cout<<N<<endl;
                break;
            }
            while(1){
                if(tempa[0]=='+'){
                    if(tempa[i]=='-'){
                        i--;
                    }else{
                        break;
                    }
                }else{
                    break;
                }
            }
            for(int j=0;j<=i;j++){
                if(tempa[j]=='-'){
                    tempb[i-j]='+';
                }else{
                    tempb[i-j]='-';
                }
            }
            for(int i=0;i<strlen(input);i++){
                tempa[i]=tempb[i];
            }
            N++;
        }
        
        
    }
    exit(0);
    
}
