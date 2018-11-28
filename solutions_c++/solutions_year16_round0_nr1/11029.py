#include<iostream>
//#include<conio.h>
using namespace std;
int seen[10];
int been[10];
void display(int x[]){
for(int i=0; i<10; i++){
 cout<<x[i]<<"\t";
 }cout<<endl;
 }





 int decompose(long int x){
long int residue=0,n=10;
int dc=0,ct=0;

 for(int i=0; i<=9; i++){
  if((x%n)<=x && ct==0){
  residue=(x%n);
  seen[i]=residue/(n/10);
  dc+=1;
  if(x%n==x)
   ct=-1;

   //cout<<seen[i]<<"\t";

  n=n*10;

  }

 }
 //cout<<endl;

   return dc;
}

void solver(int n){

 for(int a=0; a<n; a++){
  for(int b=0; b<10; b++){
   if(been[b]==-1){
    been[b]=seen[a];
    break;
    }
   if(been[b]==seen[a])
    break;
   }
  }

// display(been);

}

int sumcalc(){
int sum=0;
   for(int i=0; i<10; i++)
     sum=sum+been[i];
   return sum;
     }

void chief(int test,int v){

//clrscr();
for(int h=0; h<10; h++)
 been[h]=-1;
//cout<<"Enter a number";
//cin>>test;

int sum=sumcalc(), n=1;

while(sum!=45){

int digits=decompose(test*n);
solver(digits);
sum=sumcalc();
if(sum==45)
 cout<<"Case #"<<v+1<<":"<<test*n<<endl;

else
 n=n+1;


}



}


int main(){
int ntc;

cin>>ntc;
int tc[100];
for(int v=0; v<ntc; v++)
 cin>>tc[v];
for(int v=0; v<ntc; v++){
 if(tc[v]==0)
  cout<<"Case #"<<v+1<<":"<<"INSOMNIA\n";
 else
  chief(tc[v],v);
    }
//getch();
return 0;
}
