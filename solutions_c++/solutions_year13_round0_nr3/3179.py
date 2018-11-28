
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <string>
#include <sstream>

using namespace std;

bool isPalin(int num){
	stringstream ss;
	ss<<num;
	string s;
	ss>>s;
	
	for(int i=0;i<s.length()/2;i++){
		if(s[i] != s[s.length() - i - 1])
			return false;
	}
	return true;

}


int main(){

	ifstream in;
	in.open("C.in");
	
	ofstream out;
	out.open("out.txt");
	
	int T;
	in>>T;
	
	vector<int> sq;
		
	for(int i=0;i*i<=1000;i++){
		int square = i*i;
		if(isPalin(i) && isPalin(square)){
			sq.push_back(square);
			cout<<square<<endl;
		}
	}
	
	for(int u=0;u<T;u++){
	
		int A,B;
		in>>A>>B;
		
		int count = 0;
		for(int i=0;i<sq.size();i++){
			if(sq[i] <= B && sq[i] >= A) count++;
		}
		
		out<<"Case #"<<(u+1)<<": "<<count<<endl;
		cout<<"Case #"<<(u+1)<<": "<<count<<endl;	
		
    }
	in.close();
	out.close();
	
    return 0;
}





