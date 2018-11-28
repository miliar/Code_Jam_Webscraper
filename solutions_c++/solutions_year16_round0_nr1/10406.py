#include<iostream>
using namespace std;
int in[10]={0,0,0,0,0,0,0,0,0,0};
int glsm=0;
void extDig(int);
int main() {
int t;
cin>>t;
for(int i=0;i<t;i++) {
glsm=0;
for(int j=0;j<10;j++) in[j]=0;
int n,ne,ml=1;
cin>>n;
if(n==0){cout<<"Case #"<<i+1<<": "<<"INSOMNIA\n";}
else{
while(1){
ne=n*ml;
extDig(ne);
if(glsm==45 && in[0]==1){cout<<"Case #"<<i+1<<": "<<ne<<"\n";break;}
ml++;
}
}
}
return 1;
}

void extDig(int ne){
int rm;
while(ne>0){
rm=ne%10;
if(in[rm]==0) {
in[rm]=1;
glsm+=rm;
}
ne=ne/10;
}
}
