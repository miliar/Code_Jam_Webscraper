#include <iostream>
#include <cstdio>
using namespace std;

void test(int t){
	cout << "Case #" << t << ": ";
	int K,C,S; cin >> K >> C >> S;
	for (int i=0;i<K;i++){
		cout << i+1;
		if (i != K-1) cout << " "; else cout << endl;
	}
}
int main(){
	freopen("D.in","r",stdin);
	freopen("D.txt","w",stdout);
	int n; cin >> n;
	for (int i=1;i<=n;i++) test(i);
}
