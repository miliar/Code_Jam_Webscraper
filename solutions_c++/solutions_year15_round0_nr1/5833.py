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
input >> cases;

int maxs;
string s;
const char * ss;
long long ifriend;
long long cursum;
int current;

for(int i=0; i< cases ; i++){
//cout<<"case " << i <<endl;
ifriend=0;
cursum=0;
current=0;
input >> maxs;
input >> s;
ss = s.c_str();

for( int j=0; j <= maxs ; j++){
  current = ss[j]-48;
  if( cursum < j ){
    ifriend+=(j-cursum);
    cursum+=(j-cursum);
  }
  cursum+=current;
//  cout<<"current "<<current<<" cursum "<<cursum<<" invite "<<ifriend<<endl; 
}

//cout<<" invite "<<ifriend<<endl;
output<<"Case #"<<i+1<<": "<<ifriend<<endl;  

}

input.close();
output.close();
return 0;
}

