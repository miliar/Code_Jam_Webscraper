#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cmath>
using namespace std;
int main(){
ifstream inf("A-large.in");
if(!inf){
cout<<"Error open file";
return 0;
}
ofstream outf("Output.txt");
if(!outf){
cout<<"Error open file";
return 0;
}
int max=0;
int num=0;
string wd;
inf>>wd;
num=atoi(wd.c_str());
for(int i=1;i<=num;i++){
inf>>wd;
max=atoi(wd.c_str());
inf>>wd;
const char *list=wd.c_str();
int result=0;
int currentp=0;
for(int j=0;j<=max;j++){
if(list[j]!='0'&&currentp<j){
result+=j-currentp;
currentp+=j-currentp;
}
currentp+=list[j]-'0';
}
outf<<"Case #"<<i<<": "<<result<<endl;
}
}