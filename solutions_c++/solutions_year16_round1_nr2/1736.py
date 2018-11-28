#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;
int main(){
ifstream infile("2l.in");
ofstream outfile("outl.in");
int lines,a[2501],cas,num,rep,i,k;
cas=1;
infile>>lines;
while(lines--){
    for(i=0;i<2501;i++)
        a[i]=0;
    infile>>num;
    rep=num*(2*num-1);

    while(rep--){
        infile>>k;
        a[k]=1-a[k];

        }
    if(cas!=1)
        outfile<<endl;
    outfile<<"Case #"<<cas<<":";
    for(i=1;i<2501;i++){
        if(a[i]==1){
            outfile<<" "<<i;
            num--;
            }
        if(num==0)
            break;
        }
    cas++;
    }
}


