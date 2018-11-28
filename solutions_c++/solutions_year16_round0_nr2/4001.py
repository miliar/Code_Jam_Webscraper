#include <iostream> 
#include <stdio.h>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <regex>
using namespace std;


int main(){

int t;
cin>>t;
int c =1;
string n;

while(t--){

cin>>n;

char curr_sign = n[0];
int changes =0;

for(int i=1;i <n.size();i++){
if(n[i] == curr_sign) continue;
curr_sign = n[i];
changes++;

}
if(curr_sign == '-') changes++;


cout<<"Case #"<<c<<": "<<changes<<endl;


c++;

}


return 0;
}

 
