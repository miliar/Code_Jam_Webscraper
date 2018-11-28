#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

int main( int argc, char** argv){


ofstream output;
ifstream input;
cout<< " start "<<endl;
input.open(argv[1]);
output.open("ans.txt");


if(input.fail()){
  cout<<" error opening file"<<endl;
  return -1;
}


int cases;
input >> cases;

string ans;
string in;

for(int i=0; i< cases ; i++){



in.clear();
ans.clear();

input >> in;
cout<<"case "<<i+1<<" "<<in<<endl;
ans.push_back(in[0]);

for(int i=1; i<in.size(); i++){

if(in[i]>=ans.front()){
	ans.insert( ans.begin() , in[i] );
}else{
	ans.push_back(in[i]);
}

}
output<<"Case #"<<i+1<<": "<<ans<<endl;  
cout<<"Case #"<<i+1<<": "<<ans<<endl;  
}
input.close();
output.close();
return 0;
}
