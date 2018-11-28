#include <iostream>
#include<map>
#include <fstream>
#include<algorithm>
#include <sstream>
#include <limits>
using namespace std;
int pancake(string st, map<string, int>& cache){
	if(st == ""){
		return 0;
	}
	int i = st.length() -1;
	while(i >=0 && st[i] == '+') --i;
	if(i < 0){
		cache[st] = 0;
		return cache[st];
	}
	if(cache.count(st) == 0){
		cache[st] = numeric_limits<int>::max() - 1; 
		for(int s = i; s >= 0; --s){
			string top(st.substr(0, s+1));
			for(int k =0; k < top.length(); ++k){
				if(top[k] == '-') top[k] = '+';
				else if(top[k] == '+') top[k] = '-';
			} 
			reverse(top.begin(), top.end());

			string rest(st.substr(s+1, i-s));
			if(top == st.substr(0, s+1) || (top+rest) == st){
				continue;
			}

			int f = pancake(top+rest, cache);
	//cout <<0 << "|" <<  s << "|" << i << endl;
	//cout << st << "|" << top << "|" << rest << "|" << f << "|" << cache[st] <<endl;
			cache[st] = min(f+1, cache[st]);
		}
	}
	return cache[st];
}
int main(int argc, char* argv[]){
  	ifstream myfile (argv[1]);
  	if (myfile.is_open()){
		string line;
		int i = 1;
		int T = -1;
    		while ( getline (myfile,line) ){
			if(T == -1){
				T = stoi(line);
			}else{
				stringstream answer;
				/////////////////
				map<string, int> cache;
				answer << pancake(line, cache);	
				////////////////
				cout << "Case #"<< i <<": " << answer.str() << endl;
				i++;
			}
    		}
	}
    	myfile.close();
}
