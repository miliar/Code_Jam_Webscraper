#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
using namespace std;
typedef long long LL;

int digit[11];

void reset()
{
    for(int i=0;i<11;i++) digit[i] = 0;
}

int checkdigit(LL n)
{
    int c;
    c = 0;
    for(int i=0;i<11;i++)
        c += digit[i];
    return c;
}

void setdigitvalue(LL N){
    int v;
    while(N>0){
        v = N%10;
        digit[v] = 1;
        N /= 10;
    }
}

int main() {
	int T, c, i;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	cin >> T;
	for(int t = 1; t <= T; t++){
		LL N, M;
		cin >> N;
		reset();
		if(N==0){
            cout << "Case #" << t << ": INSOMNIA"<<endl;
            continue;
		}
		i = 1;
        while(true){
            M = N*i;
            setdigitvalue(M);
            c = checkdigit(M);
            if(c==10){
                cout << "Case #" << t << ": "<<M<<endl;
                break;
            }
            i++;
		};
	}
	return 0;
}
