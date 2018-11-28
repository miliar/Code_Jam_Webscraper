#include <iostream>
#include <unordered_map>
using namespace std;

// void intToStr(int a,std::vector<char> &v){
// 	int sz = log10(a)+1;
// 	v.resize(sz);
// 	// ptr = (char *)malloc(sz);
// 	for(int i=0;i<sz;++i){
// 	// while(a){
// 		v[sz-i-1] = '0' + a % 10;
// 		a = a / 10;
// 	}
// }

// bool verifyAll(string &s){
// 	for(char &ch:s){
// 		if(ch == '-')
// 			return false;
// 	}
// 	return true;
// }

// void printVector(std::vector<char> &v){
// 	for(auto ch:v)
// 		cout<<ch;
// 	cout<<"\n";
// }

// void flip(string &s,int end){
// 	assert(s.size() > end);

// 	for (int i = 0; i < (end+1)/2 ; ++i){
// 		char temp = s.at(i);				
// 		s.at(i) = '-'+'+'-s.at(end-i);
// 		s.at(end-i) = '-'+'+'-temp;
// 	}
// 	// for the middle value
// 	if(!(end % 2))
// 		s.at(end/2) = '-'+'+'-s.at(end/2) ;
// }

std::unordered_map<string,int> m1 = {{"-",1},{"+",0},
							{"--",1},{"++",0},
								{"-+",1},{"+-",2}};

int findVal(string s){
	auto it = m1.find(s);
	if(it != m1.end())
		return it->second;
	
	char lc1 = s.back();
	string origStr = s;
	s.pop_back();
	int result = findVal(s);
	char lc2 = s.back();

	if (lc1 == '-' && lc2 == '+'){
		result += 2;
	}

	m1[origStr] = result;
	return result;
}

int main(){
	int T;
	cin >> T;

	for(int i=0;i<T;++i){
		string input;
		cin >> input;

		cout<<"Case #"<<i+1<<": "<<findVal(input)<<endl;
	}
}