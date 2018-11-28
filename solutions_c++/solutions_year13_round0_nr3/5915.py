#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

fstream file("C-small-attempt0.in");
fstream out("out.txt");
bool isfair(int val){
int sep[4];		//to change
bool res=true;
int i=0;
while(val!=0){
	sep[i++]=val%10;
	val/=10;
}
for(int j=0;j<i/2;j++)
if(sep[j]!=sep[i-j-1]){
	res=false;
	break;	
	}

return res;
}

int sf(int a,int b){
int count=0,p;
p=sqrt(a);
if(p*p<a)p++;
while(p*p<=b){
	if(isfair(p*p))
		if(isfair(p))count++;
	p++;
}

return count;
}
int main(){
int no,a,b,count;

file>>no;
for(int i=0;i<no;i++){
file>>a>>b;
count=sf(a,b);
out<<"Case #"<<i+1<<": "<<count<<endl;
}
return 0;
}