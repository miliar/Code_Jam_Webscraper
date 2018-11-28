#include<cstdlib>
#include<cstdio>
#include<iostream>
#include<fstream>
using namespace std;

int main(){
FILE *ifp;

ifp =fopen("A-small-attempt0.in","r+");
ofstream fout("prob1.out");

int T,row1,row2,a[16],b[16],flag,it=0,val,j=0,i=0;
fscanf(ifp,"%d",&T);
while(it<T){
++it;
fscanf(ifp,"%d",&row1);
fscanf(ifp,"%d%d%d%d",a,a+1,a+2,a+3);
fscanf(ifp,"%d%d%d%d",a+4,a+5,a+6,a+7);
fscanf(ifp,"%d%d%d%d",a+8,a+9,a+10,a+11);
fscanf(ifp,"%d%d%d%d",a+12,a+13,a+14,a+15);

fscanf(ifp,"%d",&row2);
fscanf(ifp,"%d%d%d%d",b,b+1,b+2,b+3);
fscanf(ifp,"%d%d%d%d",b+4,b+5,b+6,b+7);
fscanf(ifp,"%d%d%d%d",b+8,b+9,b+10,b+11);
fscanf(ifp,"%d%d%d%d",b+12,b+13,b+14,b+15);
flag=0;
for(i=0;i<4;i++){
for(j=0;j<4;j++){
if(*(a+(4*(row1-1))+i)==*(b+(4*(row2-1))+j)){
++flag;
val= *(a+(4*(row1-1))+i);
}
if(flag>1) break;
}
if(flag>1) break;
}
if(flag==0)
fout<<"Case #"<<it<<": Volunteer cheated!"<<endl;
else if(flag>1) 
fout<<"Case #"<<it<<": Bad magician!"<<endl;
else if(flag==1)
fout<<"Case #"<<it<<": "<<val<<endl;
}
}
