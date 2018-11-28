#include <iostream>
#include <string>
#include <cstdlib>
#include <math.h>
using namespace std;

int main(){
int t;
cin>>t;
for(int i=1;i<=t;i++)
{

long long int a,b;
string p;
cin>>p;
string x,y;
x=p.substr(0,p.find('/'));
y=p.substr(p.find('/')+1,p.length()-p.find('/'));

a=atoi(x.c_str());
b=atoi(y.c_str());

double input=double(a)/double(b);
bool check=true;
if(a==0) check=false;
else {
	double p=(double(a)/double(b))*pow(2,int(log2(b))+1);
	if(int(p)==p) check=true;
	else check=false;
}

if(check)
{
int ans=0;

while(input<1){
	ans++;
	input*=2;		
}
cout<<"Case #"<<i<<": "<<ans<<endl;
}
else cout<<"Case #"<<i<<": impossible"<<endl;
}}
