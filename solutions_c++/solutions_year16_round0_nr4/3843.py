#include<iostream>
#include<fstream>
#include<math.h>
using namespace std;

int main(){
ifstream infile("11.in");
ofstream outfile("22.txt");
int k,c,s,lines,x,i=1;
long int p,q;
infile>>lines;
while(lines--){
    outfile<<"Case #"<<i<<":";
    infile>>k;
    infile>>c;
    infile>>s;
    p=pow(k,c-1);
    for(x=1;x<=s;x++){

        outfile<<" "<<x;
    }
    outfile<<endl;
    i++;
    }
}
