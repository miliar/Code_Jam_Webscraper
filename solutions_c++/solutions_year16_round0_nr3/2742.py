#include<iostream>
#include<fstream>
#include<vector>

typedef unsigned long long llong;
using namespace std;


ifstream fin ("C-small-attempt0.in");
ofstream fout ("output.out");

llong N,J,T;

llong pow(llong i,llong j){
if(j==0)return 1;
else if(j%2==0){
    llong temp = pow(i,j/2);
    return temp*temp;
}
else { llong temp = pow(i,j/2);
       return temp*temp*i;
     }
}

llong base(int i,llong k){
llong temp=0,power=1;
//in base i
for(int j=0;j<N;j++){
    if((k>>j)&1){temp+=power;}
    power*=i;
}

if(temp%2==0)return 2;
for(llong j=3;j<temp;j+=2){
    if(j*j>temp)return -1;
    if(temp%j==0)return j;
}
}

void jam(){
llong k=pow(2,N-1)+1;
int coin=0;
while(coin<J){
    bool prime = false;
    vector<llong> factor;
    for(int i=2;i<=10;i++){
            llong temp = base(i,k);
            if(temp==-1){ prime=true;break;}
            else{ factor.push_back(temp);}
    }
    if(prime){k+=2;continue;}
    coin++;
    for(int i=N-1;i>=0;i--){
        if((k>>i)&1)fout << "1";
        else fout << "0";
    }
    for(int i=2;i<=10;i++){
        fout << " " << factor[i-2];
    }
    fout << endl;
    k+=2;
}
return;
}
int main(){

fin >> T;
fout << "Case #1:" << endl;
fin >> N >> J;
jam();
return 0;
}
