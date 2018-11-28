#include<bits/stdc++.h>
using namespace std;
int main(){
    ifstream iff("A-large.in");
ofstream off("code_jamA.txt");
int t,c=0;
iff>>t;
while(t--){
        c++;
    long long int n,i=0,m;
    int mk[10],count =0;
    for(int j=0;j<10;j++){
        mk[j] = 0;
    }
    iff>>n;

if(n!=0){
    while(count!=10){
        i++;
        m = n*i;
        while(m>0){
            if(mk[m%10]==0){
            mk[m%10] = 1;
            count++;
            }
            m=m/10;
        }

    }
    off<<"Case #" << c << ": "<<n*i<<"\n";
}else{
    off<<"Case #" << c << ": INSOMNIA\n";
}

}
return 0;
}

