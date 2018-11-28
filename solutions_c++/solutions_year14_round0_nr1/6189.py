#include <iostream>
#include <cstdio>
#define lli long long int
using namespace std;
lli m1[5][5];
lli m2[5][5];
lli t,r1,r2;
lli sol=0;
lli pos=-1;
void read(lli mat[5][5]){
    for(lli i=0;i<4;i++){
        for(lli j=0;j<4;j++){
            cin>>mat[i][j];
        }
    }
}
void solve(){
    sol=0;pos=-1;
    lli rep=0;
    for(lli i=0;i<4;i++){
        for(lli j=0;j<4;j++){
           // cout<<"elm  "<<m2[i][j]<<endl;
          // cout<<"****==== "<<m1[r1-1][i]<<"   ==  "<<m2[r2-1][j]<<endl;
            if(m1[r1-1][i]==m2[r2-1][j]){

                rep++;pos=m2[r2-1][j];
            }
        }
    }
    if(rep==0){
        sol=3;return;
    }
    if(rep==1){
        sol=1;return;
    }
    if(rep>1){
        sol=2;return;
    }
}
int main()
{
FILE *out;
    out=fopen("out.txt","r+");
    cin>>t;
    for(lli m=1;m<=t;m++){
        cin>>r1;
        read(m1);
        cin>>r2;
        read(m2);
        solve();
        switch(sol){
    case 1:fprintf(out,"Case #%lld: %lld\n",m,pos);    break;
    case 2:fprintf(out,"Case #%lld: Bad magician!\n",m);  break;
    default:fprintf(out,"Case #%lld: Volunteer cheated!\n",m);break;
        }
    }

    return 0;
}
