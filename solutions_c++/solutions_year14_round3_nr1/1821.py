#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstring>
#include<map>
#include<limits.h>

#define INF (din[42])

using namespace std;

bool ok;
long long din[50], res;
map<long long,bool> f;

void solve(long long P,long long Q ){
     
     if( P == 0 )
         return;
     if( f[P] ){
         ok = false;
         return;
         }
     
     f[P] = 1;
     int pos = -1;
     for(int i=1;i<=41;i++)
             if( din[i]*P >= Q ){
                 pos = i;
                 break;
                 }
     
     long long left = din[pos]*P - Q;
     solve( left, Q );
     res = pos;
}
     
     
int main(){
    ifstream fin ( "elf.in" );
    ofstream fout( "elf.out" );
    
    din[0] = 1;
    for(int i=1;i<=45;i++)
            din[i] = din[i-1] * 2;
    
    int T; fin>>T;
    for(int t=1;t<=T;t++){
            f.clear();
            ok = true;
            res = -1;
            
            char x;
            long long P,Q; fin>>P>>x>>Q;
            
            solve( P, Q );
            fout<<"Case #"<<t<<": ";
            
            if( !ok )
                fout<<"impossible\n";
            else 
                 fout<<res<<endl;
            }
    
    return 0;
}
