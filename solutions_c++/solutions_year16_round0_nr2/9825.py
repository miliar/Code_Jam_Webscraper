#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>

using namespace std;  // since cin and cout are both in namespace std, this saves some text

#define CASE "Case #"
#define COLON ": "
#define SPACE " "
#define HAPPY '+'

void solution(std::string& pancake_stack, const size_t N, size_t& flips, bool prev_happy){
	if(N==0){ return; }
	for(size_t i=N-1;;--i){
		if(i != 0){
			if(pancake_stack[i] == HAPPY ^ prev_happy) ++flips;
			solution(pancake_stack, i, flips, pancake_stack[i] == HAPPY);
			break;
		}else if(pancake_stack[i] == HAPPY ^ prev_happy && i == 0){
			++flips;
		}
		if(i==0) break;//because i is unsigned, i am doing the check here ... to avoid overflows 0UL-1 = ULONG_MAX
	}
}

int main() {
    int line_count;
    cin >> line_count; 
    for (int line_no = 1; line_no <= line_count; ++line_no) {
				string line;
        cin >> line;
				size_t flips = 0;
				solution(line,line.size(),flips,true);
        cout << CASE << line_no << COLON << flips <<endl;
    }
}
