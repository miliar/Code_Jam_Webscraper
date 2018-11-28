#include <iostream>
#include <cmath>
#include <cstring>
#include <cstdio>
using namespace std;

bool fair(int N){
	char a[50];
	sprintf(a,"%d",N);
	for (int i = 0,j=strlen(a)-1; i<j; i++,j--){
		if (a[i]!=a[j]) return false;
	}
	return true;
}
bool square(int N){
	return ((int)sqrt(N)*(int)sqrt(N))==N;
}

int main(){
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	int T,A,B,m;
	cin >> T;
	for (int t = 0; t < T; t++){
		m=0;
		cin >> A >> B;
		for (int i = A; i <= B; i++){
			if (fair(i)&&square(i)&&fair(sqrt(i)))m++;
		}
		cout << "Case #" << t+1 << ": " << m << endl;
	}
	return 0;
}
