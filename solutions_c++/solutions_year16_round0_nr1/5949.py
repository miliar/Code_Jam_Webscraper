#include<iostream>
#include<fstream>
using namespace std;

long int calc(int a[],long int b,int pro){
    int k=0,j=0;
    long int r;
    r=b*pro;
    while(r>0){
    a[r%10]=1;
    r=r/10;
    }
    for(k=0;k<10;k++){
        if(a[k]==1)
            j=1;
        else{
            j=0;
            break;
        }
    }
    r=b*pro;
    if (j==1) return r;

    pro=pro+1;
    return calc(a,b,pro);
}

ifstream infile("lar.in");
ofstream outfile("larans.in");
int main(){
int lines,i,no;
long int input,out;
no=1;
int a[10];
infile>>lines;
while(lines--){
    infile>>input;
    for(i=0;i<10;i++){
        a[i]=0;
        }
        if(input==0){
            outfile<<"Case #"<<no<<": INSOMNIA"<<endl;
        }
        else{
            out=calc(a,input,1);
            outfile<<"Case #"<<no<<": "<<out<<endl;
        }
    no++;
}
}

