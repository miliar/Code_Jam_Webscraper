#include <iostream>
using namespace std;

int n;

int run(){
    cin >> n;getchar();
    int ret = 0;
    int cnt = 0;
    for(int i = 0; i <= n; i++){
            char c = getchar();
            int t = c - '0';
            if (t > 0)
            if (cnt >= i){
            	
			}else{
				ret += i - cnt;
				cnt = i;
			}
			cnt += t;
    }
	return ret;
}
int main(){
    int ntest;
    cin >> ntest;
    for(int i = 1; i <= ntest; i++){
            cout << "Case #" << i << ": " << run() << endl;
            }
    return 0;
}
