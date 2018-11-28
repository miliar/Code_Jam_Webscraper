#include <cmath>
#include <iostream>
#include <string>
#include <algorithm>
#include <queue>  
#include <vector>

using namespace std;

int caseNumber;



int main(){

//input the given number of test cases and values
 int t;
 string m;
vector<string> v;
 cin >> t;  // the number of test cases we are given

  for (int i = 1; i <= t; i++) {
    cin >> m ;  
	v.push_back(m);
	
//putting it somewhere
	
  }
for(int i=0; i<t;i++){
cout<<"Case #"<<i+1<<": ";
string n=v[i];
vector<char> listc;

listc.push_back(n[0]);
for(int j=1; j<n.length(); j++){

	string temp1=string(1,listc[0]);
	string temp2=string(1,n[j]);
	int t=temp1.compare(temp2);
if(t<=0){
listc.insert(listc.begin(), n[j]);

}
	else{
	listc.push_back(n[j]);

	}

}

for(int k=0; k<n.length(); k++){
		cout<<listc[k];
}

cout<<""<<endl;
//the real code
}

}


