#include <iostream>
#include <fstream>
#define cir 100
using namespace std;

fstream file("A-small-attempt0.in");
fstream out("out.txt");

int arr[cir];

int calculate(int r,int t){
int n=1;
while(t>=n*((2*r)+(2*n)-1))
++n;

return n-1;
}


int main(){
int no,r,t,res;

file>>no;
for(int i=0;i<no;i++){
file>>r;
file>>t;
res=calculate(r,t);
out<<"Case #"<<i+1<<": "<<res<<endl;
}

	
return 0;
}