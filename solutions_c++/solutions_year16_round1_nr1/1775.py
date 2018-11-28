#include<iostream>>
#include<math.h>
#include<fstream>
using namespace std;
int main(){
ifstream infile("2.in");
ofstream outfile("out2.in");
string a,b;
int i,j,lines,cas;
infile>>lines;
cas=1;
while(lines--){
infile>>a;
i=a.length();
b=a[0];
for(j=1;j<i;j++){
    if (a[j]<b[0])
        b=b+a[j];
    else
        b=a[j]+b;
    }
if(cas!=1)
    outfile<<endl;
outfile<<"Case #"<<cas<<": "<<b;
cas++;
}
}
