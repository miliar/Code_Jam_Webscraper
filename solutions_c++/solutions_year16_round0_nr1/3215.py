#include<iostream>
#include<fstream>
#include<climits>

using namespace std;

ifstream fin ("A-large.in");
ofstream fout ("output.out");

bool digit[10];

bool verifie(){
for(int i=0;i<10;i++)
    if(!digit[i])return false;
return true;
}

void update(long long k){
while(k>0){
    int i = k%10;
    digit[i]=true;
    k/=10;
}
}
void sheep(long n){
if(n==0){fout << "INSOMNIA" << endl;
         return;
        }
long long k=n;
while(k<=LLONG_MAX - n){
    update(k);
    if(verifie()){fout << k<<endl;
                  return;
                 }
    k+=n;
}
fout << "INSOMNIA" << endl;
}

int main(){
    long t,N;
fin >> t;
for(int i=1;i<=t;i++){
    for(int i=0;i<10;i++)
        digit[i]=false;
    fin >> N;
    fout << "Case #" << i << ": ";
    sheep(N);
    //cout << i << endl;
}
//cout << "finish!" << endl;
return 0;
}
