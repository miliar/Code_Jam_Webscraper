#include <iostream>
#include <string>
using namespace std;

string r[]={"0","1","2","3","4","5","6","7","8","9"};
char D[]={'0','1','2','3','4','5','6','7','8','9'};

int getInt(char c){
	for(int i=0;i<10;i++){
		if(c==D[i]){
			return i;
		}
	}
}
int main(){

	int K;
	cin >> K;
	for(int k=0;k<K;k++){
		int N;string S;
		cin >> N >> S;
		int c = 0;
		int d = 0;
		for(int i=0;i<S.size();i++){
			//cout << "needs " << i <<" standing - " << c+d << "standing" <<endl;
			//cout << c << " "<< d <<" "<< S[i] << endl;
			if(c+d >= i){
				//cout << "n: "<< i << endl;
				c+=getInt(S[i]);
			}else{
				//cout << "i:" << i << endl;
				d++;
				c+=getInt(S[i]);
			}
		}
		
		cout << "Case #" << k+1 << ": " << d << "\n";
	}



	return 0;
}