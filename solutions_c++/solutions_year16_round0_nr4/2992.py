//#include<iostream>
//#include<math.h>
//#include <fstream>
//using namespace std;
//int main(){
//	ifstream cin("D-small-attempt0.in");
//	ofstream cout("output.out");
//	int i, t, k, c, s, o = 0, save;
//	long long int tile, base, z;
//	cin >> t;
//	while (t--){
//		cin >> k >> c >> s;
//		o++;
//		cout << "Case #" << o << ":";
//		if (c*s < k){
//			cout << " IMPOSSIBLE" << endl;
//		}
//		else{
//			z = pow((1 + k), (c - 1));
//			base = ((1 - k)*(z - 1)) / k;
//			for (i = 1; i <= k; i += c){
//				if (i + c - 1 > k){
//					save = c;
//					c = k - i + 1;
//					z = pow((1 + k), (c - 1));
//					base = ((1 - k)*(z - 1)) / k;
//					tile = base + i*z;
//					tile = (tile - 1)*pow(k, (save - c)) + 1;
//				}
//				else{
//					tile = base + i*z;
//				}
//				cout << " " << tile;
//			}
//			cout << endl;
//		}
//	}
//	return 0;
//}
#include<iostream>
#include<math.h>
#include <fstream>
using namespace std;
int main(){
	ifstream cin("D-small-attempt1.in");
	ofstream cout("output.out");
	int i, t, k, c, s, o = 0, save;
	long long int tile, base, z;
	cin >> t;
	while (t--){
		cin >> k >> c >> s;
		o++;
		cout << "Case #" << o << ":";
		for (i = 1; i <= s; i++){
			cout << " " << i;
		}
		cout << endl;
	}
	return 0;
}