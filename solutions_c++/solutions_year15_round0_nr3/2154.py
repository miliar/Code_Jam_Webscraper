#include <iostream>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;
typedef long long Long;
typedef pair<Long,Long> PII;

#define I 2
#define J 3
#define K 4

int m[][4] = {
	{1, I, J, K},
	{I,-1, K,-J},
	{J,-K,-1, I},
	{K, J,-I,-1},
};

int mul(int a, int b){
	int ida = max(a,-a)-1, sa = a > 0 ? 1 : -1;
	int idb = max(b,-b)-1, sb = b > 0 ? 1 : -1;
	return sa * sb * m[ida][idb];
}
int toInt(char c){
	if(c == 'i')return I;
	if(c == 'j')return J;
	if(c == 'k')return K;
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int TC;
	cin >> TC;
	for(int tc = 1 ; tc<=TC ; ++tc){
		Long L,X;
		cin >> L >> X;
//		X %= 32;
		string S;
		cin >> S;
		string T;
		for(int i = 0; i < X; ++i){
			T += S;
		}
		
		int res = 1, idF = -1, idS = -1;
		for(int i = 0; i < T.size(); ++i){
			res = mul(res, toInt(T[i]));
			if(idF == -1 && res == I){
				idF = i;
			}
			if(res == mul(I,J))
				idS = i;
			
		}
		cout << "Case #" << tc << ": ";
		if(idS != -1 && idF != -1 && res == -1 && idS > idF)
			cout << "YES" << endl;
		else
			cout << "NO" << endl;
	}
	
		
}




