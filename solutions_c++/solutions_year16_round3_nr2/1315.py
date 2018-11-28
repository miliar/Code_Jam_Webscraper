#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

ifstream infile("B-small-attempt0.in");
ofstream outfile("1sans.in");

void bin(int bl,int m,int p){
outfile<<"0";
if(m==p){
    bl--;
     while(bl--){
        outfile<<"1";
        }
    outfile<<endl;
    return;
    }
else{
p=p/2;
while(p>0){
    outfile<<m/p;
    m=m%p;
    p=p/2;
    }
outfile<<"0"<<endl;
}
}

int power(int a, int b)
{    if(b==0)
        return 1;
     int c=a;
     for (int n=b; n>1; n--) c*=a;
     return c;
}

void res(int a){
int i,j;
for(i=2;i<=a;i++){
    j=i;
    while(j--){
        outfile<<"0";
        }
    j=a-i;
    while(j--){
        outfile<<"1";
        }
    outfile<<endl;
    }
}

int main(){
int cas,bl,m,powe;

infile>> cas;
int cass=1;
while(cas--){
    infile>>bl;
    infile>>m;
    powe=power(2,bl-2);
    if (powe<m){
        outfile<<"Case #"<<cass<<": IMPOSSIBLE"<<endl;
        cass++;
        }
    else{
        outfile<<"Case #"<<cass<<": POSSIBLE"<<endl;
        bin(bl,m,powe);
        res(bl);
        cass++;
        }
    }

}
