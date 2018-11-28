#include<iostream>
#include<fstream>
using namespace std;
int main(){
int a,u,l,b[4],c[4],d=0,e=0,p,f;
ifstream fin;
ofstream fout;
fin.open("A-small-attempt0.in");
while(!fin.eof()){       //transversing 
fin>>f;
for(int i=0;i<f;i++){       //no. of cases
fin>>a;
u=a*4;l=((a-1)*4)+1;d=0;
for(int j=1;j<=16;j++){       //moving out useless elements and storing data
fin>>a;
if(j>=l&&j<=u){
b[d]=a; d++;}
}
fin>>a;
d=0;
u=a*4;l=((a-1)*4)+1;
for(int j=1;j<=16;j++){
fin>>a;
if(j>=l&&j<=u){
c[d]=a; d++;}
   }
for(int k=0;k<4;k++){
for(int l=0;l<4;l++){
   if(b[k]==c[l]){
   e++;p=b[k];    }
      }}
fout.open("testo.txt",std::ios_base::app);
if(e==0)fout<<"Case #"<<(i+1)<<": volunteer cheated!";
else if(e==1)fout<<"Case #"<<(i+1)<<": "<<p;
else
fout<<"Case #"<<(i+1)<<": Bad Magician!";
e=0;
fout<<endl;
fout.close();
}   
break;            //for
}                             //while
fin.close();
return 0;
}
