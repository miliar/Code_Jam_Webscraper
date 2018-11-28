#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <fstream>
using namespace std;
ifstream fin("data.in");
ofstream fout("data.out");
#define cin fin
#define cout fout
bool ispalin(int s){
    bool flag=true;
    char ch[5];
    sprintf(ch,"%d",s);
    int len=strlen(ch);
    for(int s1=0;s1<len/2;s1++){
        if(ch[s1]==ch[len-1-s1]) continue;
        else {
            flag=false;
            break;
        }
    }
    return flag;
}
bool issquare(int r){
    int sq=(int)sqrt(r);
    bool flag=true;
    if(sq*sq==r) {
        flag=ispalin(sq);
    }
    else flag=false;
    return flag;
}
int main()
{
    int i,n,a,b,cnt,k;
    //char ch[4];
    i=1;
    cin>>n;
    while(i<=n){
        cin>>a>>b;
        cnt=0;
        for(k=a;k<=b;k++){
            if(ispalin(k)&&issquare(k)) cnt++;
        }
        cout<<"Case #"<<i++<<": "<<cnt<<endl;
    }
    //sprintf(ch,"%d",n);
    //cout<<ch<<endl;
    //cout<<((int)sqrt(4)==2)<<endl;
    return 0;
}
