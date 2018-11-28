#include <iostream>
#include <fstream>
#include <sstream>
#include <string.h>
#define MAXN 1001
using namespace std;
bool esCapicua(int n){
	stringstream ss;
	ss << n;
	string c;
	ss >> c;
	int i;int j;
	for(i = 0,j = c.size()-1; i < j ;i++,j--)
		if(c[i]!=c[j])
			return false;
	return true;
}
int v[MAXN];
void generar(){
	memset(v, 0, sizeof v);
	for(int i = 1; i < MAXN && i*i < MAXN; i++)
		if(esCapicua(i) && esCapicua(i*i))
			v[i*i] = 1;
	for(int i = 2; i < MAXN; i++)
		v[i] += v[i-1];
}
int solve(int a, int b){
	return v[b]-v[a-1];
}
int main() {
	//ifstream cin ("input.txt");
	//ofstream cout ("output.txt");
	int t,a,b;
	cin  >> t;
	generar();
	for(int caso = 1; caso <= t; caso++){
		cin >> a >> b;
		cout << "Case #" << caso << ": " << solve(a,b) << endl;
	}
	return 0;
}
