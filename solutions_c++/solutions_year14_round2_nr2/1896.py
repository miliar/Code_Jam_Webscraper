#define _CRT_SECURE_NO_DEPRECATE
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <map>
#include <list>
#include <sstream>
#include <algorithm>
#include <vector>
#include <bitset>
#include <iomanip>
#include <queue>
#include <set>	
#include <cstring>
using namespace std;
typedef long long		ll;
typedef pair<int, int>	ii;
typedef pair<ii, int>	iii;
typedef vector<ii>		vii;
typedef vector<iii>		viii;
typedef vector<int>		vi;
typedef vector<char>	vc;
typedef vector<vc>		vvc;
typedef vector<string>	vs;
typedef unsigned long long	ull;
typedef vector<ull>		vul;
typedef vector<bool>	vb;
typedef vector<vi>		vvi;
typedef vector<vii>		vvii;
typedef vector<double>	vd;
#define INF 1000000000
#define PI 3.14159265

int msb(int x)
{
	int i = -1;
	while (((1 << ++i) <= x));
	return i;
} 

int main(int argc, char *argv[]){
	freopen("C:\\Users\\Vincent\\Desktop\\B-small-attempt0.in","r",stdin);
	freopen("C:\\Users\\Vincent\\Desktop\\out.txt","w",stdout);

	int T, N;
	cin >> T;
	for (int t=1; t<=T; t++) {
		int A,B,K;
		cin >> A >> B >> K;
		
		int count = 0;
		for (int a=0; a<A; a++) {
			for (int b=0; b<B; b++) {
				if ((a&b) < K)
					count ++;
			}
		}
		cout << "Case #" << t <<": " << count << endl;
	}


	return EXIT_SUCCESS;
}