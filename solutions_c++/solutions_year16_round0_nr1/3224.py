#include <bits/stdc++.h>
#include <fstream>
using namespace std;

int simi[10];

int main(){
    fstream potato;
    ofstream optato;
    optato.open("Answer.txt");
    potato.open("A-large.in");
    int n=0, k=0, j=0, tiems=0;
    potato >> tiems;
    for(int m=0; m<tiems; m++){
    for(int i=0; i<10; i++){
        simi[i]=0;
    }
POTA:    potato >> n;
    if(n==0){
        optato << "Case #" <<  m+1 << ": INSOMNIA\n";
        m++;
        goto POTA;
    }
    k=n;
    while(true){
    j=k;
    while(true){
        simi[j%10]=1;
        j = j/10;
        if(j==0){
            break;
        }
    }
    if(simi[0]==1 && simi[1]==1 && simi[2]==1 && simi[3]==1 && simi[4]==1 && simi[5]==1 && simi[6]==1 && simi[7]==1 && simi[8]==1 && simi[9]==1){
        optato << "Case #"<< m+1 << ": " << k << "\n";
        break;
    }
    k+=n;
}}
optato.close();
}
