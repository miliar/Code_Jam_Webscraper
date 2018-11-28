#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <fstream>
using namespace std;





int main(){
int N,caseNo,a,b,i,A[17],B[17],t1[5],flag,num,j;
fstream myfile("A-small-practise.txt", std::ios_base::in);
myfile >> N;
freopen ("A-small-practise_sol.txt","w",stdout);
for(caseNo=1;caseNo<=N;++caseNo) {
flag=0;
myfile >> a;
for(i=1;i<=16;i++) myfile >> A[i];
myfile >> b;
for(i=1;i<=16;i++) myfile >> B[i];
for(i=1;i<=4;i++) t1[i] = A[(a-1)*4+i];
for(i=1;i<=4;i++){
for(j=1;j<=4;j++){
if(t1[i]==B[(b-1)*4+j]){
flag++;
num = t1[i];
}
}
}
if(flag==1) cout<<"Case #"<<caseNo<<":"<<" "<<num<<"\n";
if(flag>1)  cout<<"Case #"<<caseNo<<":"<<" "<<"Bad magician!"<<endl;
if(flag<1)  cout<<"Case #"<<caseNo<<":"<<" "<<"Volunteer cheated!"<<"\n";
}
return 0;
}


