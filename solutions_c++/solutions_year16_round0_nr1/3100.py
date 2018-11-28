#include <iostream>
#include <bits/stdc++.h>
using namespace std;
map<unsigned long long,int> ma;
bool calcul (unsigned long long t){
bool brahim=false;
unsigned long long v=t;
int l=0;
while(v){

unsigned long long h=v%10;
ma[h]++;

v/=10;
brahim=true;
}
return brahim;



}
int main()
{
    int jg;
    int cases=0;
    fstream cin("b");
    ofstream cout("br");
    cin>>jg;
    while(jg--){
    unsigned long long t;
    ma.clear();
    cin>>t;
    cases++;
    if(t==0) {
    cout<<"Case #"<<cases<<": INSOMNIA"<<endl;
    }
    else{
    unsigned long long var=0;
    for(int i=1;i<1e6 && ma.size()<10;i++){
    calcul(t*i);
    var=t*i;
    }
    cout<<"Case #"<<cases<<": "<<var<<endl;
 }
}
    return 0;
}
