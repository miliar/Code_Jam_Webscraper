#include <iostream>
using namespace std;

int T;

int K;
char str[1003];
int q[1003];

int test(char c, int flip){
	return ((c == '+') && ((flip & 1) == 0)) || ( (c == '-') && ((flip & 1) == 1));
}

int main(){
	int front, end;
	cin>>T;
	for(int cs = 1; cs <= T; ++cs){
		cin>>str>>K;
		front = end = 0;
		int res = 0;
		int i;
		for(i = 0; str[i + K - 1]; ++i){
			if (end - front > 0 && q[front] == i)
				++front;
			if (!test(str[i], end-front)){
				q[end++] = i + K;
				++res;
			}
		}
		for(; str[i]; ++i){
			if (end - front > 0 && q[front] == i)
				++front;
			if(!test(str[i], end - front)){
				break;
			}
		}

		if(str[i]){
			cout<<"Case #"<<cs<<": IMPOSSIBLE"<<endl;
		}else{
			cout<<"Case #"<<cs<<": "<<res<<endl;
		}
	}

	return 0;
}
