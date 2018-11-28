#include <algorithm> // Author: Edward Grigoryan, Email: edogrigqv2@gmail.com
#include <cstdio> // iostream sucks
#include <vector> // Why vector ???
#include <cmath> // Abulik
#include <cstring> // string also sucks
#include <cstdlib> // Never mind
#include <set> // Elephant
#include <map> // Mammoth
#include <deque> // Slut (DP)
#include <unordered_set> // Hash rocks
#include <unordered_map> // Hash again rocks
#include <initializer_list> // I love this one
#include <string> // still sucks but sometimes usefull
#include <list> // Atomic station
using namespace std; void solve(); typedef long long int64; typedef long double real; typedef pair<int,int> pii;
int main(){
#ifdef _PLATINA
	//freopen("error.txt", "w", stderr); 
	freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);
#else
#endif 
	try{solve();}catch(int x){return x;}
}
///////////////////////BRACE YOURSELVES, IOI IS COMING//////////////////////////////////////////////////

int n;
char S[1010];

bool Check(int x)
{
	x += S[0] - '0';
	for(int i = 1; i <= n; i++){
		if(x < i){
			return false;
		}	
		x += S[i] - '0';
	}
	return true;
}

int SolveTest()
{
	scanf("%d %s", &n, S);
	for(int i = 0; i <= n; i++){
		if(Check(i) == true){
			return i;
		}
	}
	
}

void solve()
{
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		printf("Case #%d: %d\n", i, SolveTest());
	}
	throw 0;
}