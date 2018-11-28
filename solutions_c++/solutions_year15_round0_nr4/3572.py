#include<stdio.h>
#include<iostream>
#include<fstream>
using namespace std;
int main(){
    ofstream outfile;
    ifstream infile;
    outfile.open("b5.txt");
    infile.open("D-small-attempt0.in");
int t,i;
infile>>t;
for(i=1;i<=t;i++){
        int a=1,b=2,c1=3,c2=2,d1=4,d2=3,d3=2,x,r,c,n=0;

    infile>>x;
    infile>>r;
    infile>>c;
    if(x!=4||r!=4||c!=4){
            if(x!=3||r!=3||c!=3){
        n=r*c;
        if(x==1)
        {
            if(n%a==0)
                outfile<<"Case #"<<i<<": GABRIEL"<<endl;
            else
                outfile<<"Case #"<<i<<": RICHARD"<<endl;
        }
        else if(x==2){
            if(n%b==0)
                 outfile<<"Case #"<<i<<": GABRIEL"<<endl;
            else
                outfile<<"Case #"<<i<<": RICHARD"<<endl;
        }
        else if(x==3){
                        if(n%c1==0&&n%c2==0)
                 outfile<<"Case #"<<i<<": GABRIEL"<<endl;
            else
                outfile<<"Case #"<<i<<": RICHARD"<<endl;
        }
        else if(x==4){
            if(n%d1==0&&n%d2==0&&n%d3==0)
                 outfile<<"Case #"<<i<<": GABRIEL"<<endl;
            else
                outfile<<"Case #"<<i<<": RICHARD"<<endl;
        }
    }
    else
    outfile<<"Case #"<<i<<": GABRIEL"<<endl;
    }else
    outfile<<"Case #"<<i<<": GABRIEL"<<endl;
}
return(0);
}
