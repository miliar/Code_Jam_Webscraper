#include <iostream>
#include <string>

using namespace std;
// '0' = 48

int execute(int kmax,string pattern){
	int stand = (int)(pattern.at(0))-48;
	int required=0;
	for(int i = 1 ; i <= kmax && i < pattern.size() ; i++){
		char c=pattern.at(i);
		int num = (int)c - 48;
		int subReq=0;
		if(stand <i && num!=0){// not enough to trigger
			subReq=i-stand;
		}
		required += subReq;
		stand = stand + subReq + num;
	}
	return required;
}

int main(){
    int t;
	int kmax;
	string pattern;
	cin>>t;
	for(int i = 0 ; i < t;i++){
		cin>>kmax>>pattern;
		cout<<"Case #"<<i+1<<": "<<execute(kmax,pattern)<<endl;
	}
}
