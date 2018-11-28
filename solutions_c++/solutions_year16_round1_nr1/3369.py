#include <cstdio>
#include <cstdlib>
#include <deque>

using namespace std;

int main(){
	int t;
	scanf("%d\n", &t);
	for(int n = 0; n < t; n++){
		printf("Case #%d: ", n+1);
		deque<int> out;
		for(int c = getchar(); c != '\n'; c = getchar()){
			if(out.empty()){
				out.push_front(c);
				continue;
			}
			int i;
			for(i = 0; i < out.size() && out[i] == c; i++);
			if(i == out.size() || out[i] > c) out.push_back(c);
			else out.push_front(c);
		}
		out.push_back('\n');
		for(int i = 0; i < out.size(); i++){
			printf("%c",out[i]);
		}
	}

	return 0;
}
