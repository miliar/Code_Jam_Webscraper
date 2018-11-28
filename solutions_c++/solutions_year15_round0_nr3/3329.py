#include<iostream>
#include<cstdio>
#include<algorithm>
#include<climits>
#include<map>

using namespace std;

typedef unsigned long long ULL;

map<char, map<char,char> > table;
map<char, map<char,bool> >negTable;

char calc(char a, char b, bool &neg){
	char c = table[a][b];
	neg = (negTable[a][b] ? !neg : neg);
	
	//cout<<a<<" "<<b<<" "<<c<<" "<<negTable[a][b]<<endl;
 	//cout<<"=========="<<endl;
	return c;
}


int main() {
	int T;
	ULL buflen = 10001;
	char *s = new char[buflen];
// 	char input[10000000000000001];
	
	table['1']['1'] = '1';
	table['1']['i'] = 'i';
	table['1']['j'] = 'j';
	table['1']['k'] = 'k';
	table['i']['1'] = 'i';
	table['i']['i'] = '1';
	table['i']['j'] = 'k';
	table['i']['k'] = 'j';
	table['j']['1'] = 'j';
	table['j']['i'] = 'k';
	table['j']['j'] = '1';
	table['j']['k'] = 'i';
	table['k']['1'] = 'k';
	table['k']['i'] = 'j';
	table['k']['j'] = 'i';
	table['k']['k'] = '1';
	
	negTable['1']['1'] = false;
	negTable['1']['i'] = false;
	negTable['1']['j'] = false;
	negTable['1']['k'] = false;
	negTable['i']['1'] = false;
	negTable['i']['i'] = true;
	negTable['i']['j'] = false;
	negTable['i']['k'] = true;
	negTable['j']['1'] = false;
	negTable['j']['i'] = true;
	negTable['j']['j'] = true;
	negTable['j']['k'] = false;
	negTable['k']['1'] = false;
	negTable['k']['i'] = false;
	negTable['k']['j'] = true;
	negTable['k']['k'] = true;
	
	cin>>T;
	for(int t = 1; t <= T ; t++) {
		
		ULL L,X;
		
		cin>>L>>X;
		
		ULL n=L;
		
		cin>>s;
 		//cout<<"L,X,s "<<L<<" "<<X<< " "<<s<<endl;
 		
 		if(L*X < 3) {
 			cout<<"Case #"<<t<<": NO"<<endl;
 			continue;
 		}
		
		X--;
		while(X-- > 0) {
			memcpy(s+n, s, L);
			n+=L;
		}
		*(s+n) = '\0';
		//cout<<"L,X,s "<<L<<" "<<X<< " "<<s<<endl;
		
		////////////
		char match = 'i';
		char current = '1';
		bool neg = false;
		
		int i = 0;
		for(i = 0; i < n; i++) {
			current = calc(current, s[i], neg);
			if(current == 'i' && !neg) {
				//cout<<"found i at "<<i<<endl;
				break;
			}
		}
		
		if(i == n) {
			cout<<"Case #"<<t<<": NO"<<endl;
			continue;
		}
		
	// j	
		current = '1';
		neg = false;
		
		for(i++; i < n; i++) {
			current = calc(current, s[i], neg);
			if(current == 'j' && !neg) {
				//cout<<"found j at "<<i<<endl;
				break;
			}
		}
		
		if(i == n) {
			cout<<"Case #"<<t<<": NO"<<endl;
			continue;
		}
		
	//k
		current = '1';
		neg = false;
		
		for(i++; i < n; i++) {
			//cout<<"i = "<<i<<"n" <<n<<endl;
			current = calc(current, s[i], neg);
		}
		
		if(current == 'k' && !neg) {
			cout<<"Case #"<<t<<": YES"<<endl;
		}
		
		else {
			cout<<"Case #"<<t<<": NO"<<endl;
		}
		
		
		//cout<<"-------------"<<endl;
	}
	
	delete []s;

}