// Create your own template by modifying this file!
#include <iostream>
using namespace std;

#define INF 100000000
#define pb push_back
#define PII pair<int,int>
#define mp make_pair
#define MAXN 100005

bool num[10];

void decompose(int n){
	while(n){
		num[n%10] = true;
		n /= 10;
	}
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++){
		long long N;
		cin >> N;
		if(!N) cout << "Case #" << t << ": INSOMNIA" << endl;
		else{
			for(int i = 0; i < 10; i++)
				num[i] = false;
			decompose(N);
			long long n = N;
			bool flag = true;
			for(int i = 0; i < 10; i++)
				flag &= num[i];
			while(!flag){
				N+=n;
				decompose(N);
				flag = true;
				for(int i = 0; i < 10; i++)
					flag &= num[i];
			}
			cout << "Case #" << t << ": " << N << endl;
		} 
	}
}

