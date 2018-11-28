#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;


int main( int argc, char** argv){


ofstream output;
ifstream input;
//cout<< " start "<<endl;
input.open(argv[1]);
output.open("ans.txt");


if(input.fail()){
  cout<<" error opening file"<<endl;
  return -1;
}


int cases;
int X;
int R;
int C;
input >> cases;

int failure;
for(int i=0; i< cases ; i++){

failure=0;
cout<<"case " << i+1 <<endl;
input >>X;
input >>R;
input >>C;



if( (R*C)%X )
  failure = 1;

if( X>=(R*2+1) )
  failure = 1;

if( X>=(C*2+1) )
  failure = 1;

if( (X>R) && (X>C))
  failure = 1;

if( (C%2) && ((X-R)>=((C/2)+1)) && (X>2)  ) 
  failure = 1;

if( !(C%2) && ((X-R)>=(C/2)) && (X>2)) 
  failure = 1;

if( (R%2) && ((X-C)>=((R/2)+1)) && (X>2) ) 
  failure = 1;

if( !(R%2) && ((X-C)>=(R/2)) && (X>2) ) 
  failure = 1;

cout<<" failure "<<failure<<endl;
if(failure)
  output<<"Case #"<<i+1<<": "<<"RICHARD"<<endl;  
else
  output<<"Case #"<<i+1<<": "<<"GABRIEL"<<endl;  
}

input.close();
output.close();
return 0;
}
