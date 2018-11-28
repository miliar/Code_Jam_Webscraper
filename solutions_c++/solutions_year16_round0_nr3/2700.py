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
        cout << "Case #" << t << ": "<<endl;
        int n,j;
        cin>>n>>j;
        num[0]=1;
        for(int i=1;i<n-1;i++){
            num[i]=0;
        }

        num[n-1]=1;
        int i=0;
        while(j!=i){
            tenbase=0;
            for(base=2;base<=10;base++){
                tenbase=0;
                for(long long bb=0;bb<n;bb++){
                    tenbase = tenbase*base+num[bb];//number to 10base transform
                }
                //prime check
                notprime=false;
                for(prime=2;prime<tenbase;prime++){
                    if(prime*prime>tenbase)//prime
                    {
                        notprime=false;
                        break;
                    }
                        
                    if(tenbase%prime==0){
                        notprime=true;
                    }
                    if(notprime==true){//no prime so break;
                        notprimenum[base]=prime;
                        break;
                    }
                }
                if(notprime==false){//prime number so end
                    break;
                }
            }
            if(base==11&&notprime){
                i++;
                cout<<tenbase<<" ";
                for(int pp=2;pp<=10;pp++){
                    cout<<notprimenum[pp]<<" ";
                }
                cout<<endl;
                //print
            }
            makenextnum(n-2);
        }
        
            //cout <<numofN<< endl;
    }
    exit(0);
    
}
