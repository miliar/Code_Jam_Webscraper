//||||||||||||||||||||||||||||
//----IN THE NAME OF GOD----||
//||||||||||||||||||||||||||||

#include <bits/stdc++.h>
using namespace std;

#define f first
#define s second
#define mp make_pair
#define pb push_back

typedef long long int lld;
typedef long double ldb;

int main(){
	ifstream input;
	input.open("A-large.in");
	ofstream output;
	output.open("out.txt");
	int t;
	lld n;
	input >> t;
	int i=0;
	while(t--){
		i++;
		input >> n;
		output << "Case #" <<i<<": ";
		if(n==0){
			output<<"INSOMNIA"<<endl;
			continue;
		}
		lld cnt=1;
		set <int> s;
		lld k=n,z;
		while(1){
			z = n*cnt;
			cnt++;
			lld tmp = z;
			while(tmp){
				s.insert(tmp%10);
				tmp/=10;
			}
			if(s.size()==10) break;
		}
		output << z <<endl; 
	} 
}
