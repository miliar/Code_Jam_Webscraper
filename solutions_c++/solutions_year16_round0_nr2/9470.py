#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>

using namespace std;

string st;
int ans=0;

bool happy( ){
     bool ok=true;
     for(int i=0; i<st.size( ); i++) if(st[i]!='+') ok=false;
     return ok;
}

bool unhappy( ){
     bool ok=true;
     for(int i=0; i<st.size( ); i++) if(st[i]!='-') ok=false;
     return ok;
}

void flip( ){
    if(!unhappy( )){
         for(int i=1; i<st.size( ); i++){
             if(st[i]!=st[i-1]){
                 ans++;
                 string esp=st.substr(0, i);
                 for(int k=0; k<i; k++){
                     st[k]=(esp[i-1-k]=='+' ? '-' : '+');
                 }
             }
         }
    }
    else{
        for(int i=0; i<st.size( ); i++) st[i]='+';
        ans++;
    }
}

int main( ){
    int t;
    scanf("%d", &t);
    for(int i=1; i<=t; i++){
        cin >> st;
        ans=0;
        if(st.size( )==1){
           ans=(st[0]=='+' ? 0 : 1);
        }else{
           while(!happy( )) flip( );
        }
        printf("Case #%d: %d\n", i, ans);
    }
    return 0;
}
