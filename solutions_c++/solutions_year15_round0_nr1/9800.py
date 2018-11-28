#include<stdio.h>
#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;
int main(){
    ofstream outfile;
    ifstream infile;
    outfile.open("b2.out");
    infile.open("A-small-attempt0.in");
int t,i,smax,j,count=0,count1=0,s=0,k;
infile>>t;
for(i=1;i<=t;i++){

        s=0;
        count1=0;

    infile>>smax;
    char a[smax+1];
    int b[smax+1];

    infile >> a;

    for(j=0;j<=smax;j++){
            b[j]=a[j]-48;
    }
        for(k=0;k<=smax;k++){
            if(k<=s)
                s=s+b[k];
            else{
                if(b[k]!=0){
                  count1=count1+(k-s);
                  s=s+b[k]+count1;
                }
            }
        }


outfile<<"Case #"<<i<<": "<<count1<<endl;
}
return(0);
}
