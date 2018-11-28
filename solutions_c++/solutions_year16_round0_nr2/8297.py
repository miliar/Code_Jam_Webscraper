#include <fstream>;
#include <string>;

using namespace std;

unsigned count_transitions(string s){
	unsigned length = s.length();
	unsigned transitions(0);
	if(length == 1)return (s[0] == '+')?0:1;
	for(int i = 1; i < length; ++i){
		if(s[i-1] != s[i]){
			++transitions;
		}
	}

	return (s[length-1] == '+')? transitions : (transitions + 1);
}

int main(){
	ifstream in("B-large.in");
	ofstream out("out.txt");
	unsigned cases(0);
	string s;

	in >> cases;
	for(int c = 1; c <= cases; ++c){
		in >> s;
		out << "Case #" << c << ": " << count_transitions(s) << "\n";
	}
	out.flush();
	return 0;
}
