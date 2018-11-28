#include<iostream>
#include<fstream>
using namespace std;

int main(){
	int t;
	
	ofstream myfile;
	ifstream input;
	
	input.open("A-large.in");
	myfile.open("output.txt");
	
	int counter = 1;
	input>>t;
	
	while(t--){
		int smax;
		input>>smax;
		
		string s;
		input>>s;
		
		int count[s.length()];
		
		for(int i=0;i<s.length();i++){
			count[i] = s[i] - '0';
		}
		
		long long mem = 0;
		long long frns = 0;
		for(int i=0;i<s.length();i++){
			if(i <= mem){
				mem += count[i];
			}else if(count[i] > 0){
				frns += (i-mem);
				mem = i + count[i];
			}
		}
		
		myfile<<"Case #"<<counter<<": "<<frns<<endl;
		counter++;
	}
	
	myfile.close();
}

