#include <bits/stdc++.h>
using namespace std;

#define fr(a, n) for(a = 0; a < n; a++)
#define fr1(a, n) for(a = 1; a <= n; a++)
#define frR(a, n) for (a = n; a >= 0; a--)
#define sc(a) scanf("%d", &a)
#define pr(a) printf("%d\n", a)
#define p(i, j) make_pair(i, j)
#define fi first
#define se second

typedef pair<int, int> ii;
typedef pair<double, double> dd;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long int ll;
typedef unsigned long long int ull;


int main(){
	int tab[255];
	int transl[10];
	int k, t, i;
	string s;
	string::iterator it;
	sc(t);
	fr1(k,t){
		
		cin>>s;
		memset(tab, 0, sizeof(tab));
		memset(transl, 0, sizeof(transl));
		
		for(it = s.begin(); it != s.end(); it++) tab[*it]++;
		
		if(tab['Z'] > 0){
			
			tab['E'] -= tab['Z'];
			tab['R'] -= tab['Z'];
			tab['O'] -= tab['Z'];
			transl[0] += tab['Z'];
			tab['Z'] = 0;
		}
		if(tab['W'] > 0){
			tab['T'] -= tab['W'];
			tab['O']  -= tab['W'];
			transl[2] += tab['W'];
			tab['W'] = 0;
		}
		if(tab['U'] > 0){
			tab['F'] -= tab['U'];
			tab['O'] -= tab['U'];
			tab['R'] -= tab['U'];
			transl[4] += tab['U'];
			tab['U'] = 0;
		}
		if(tab['G'] > 0){
			tab['E'] -= tab['G'];
			tab['I'] -= tab['G'];
			tab['H'] -= tab['G'];
			tab['T'] -= tab['G'];
			transl[8] += tab['G'];
			tab['G'] = 0;
		}
		if(tab['F'] > 0){
			tab['I'] -= tab['F'];
			tab['V'] -= tab['F'];
			tab['E'] -= tab['F'];
			transl[5] += tab['F'];
			tab['F'] = 0;
		}
		if(tab['V'] > 0){
			tab['S'] -= tab['V'];
			tab['E'] -= 2 * tab['V'];
			tab['N'] -= tab['V'];
			transl[7] += tab['V'];
			tab['V'] = 0;
		}
		if(tab['O'] > 0){
			tab['N'] -= tab['O'];
			tab['E'] -= tab['O'];
			transl[1] += tab['O'];
			tab['O'] = 0;
		}
		if(tab['N'] > 0){
			tab['I'] -= tab['N']/2;
			tab['E'] -= tab['N']/2;
			transl[9] += tab['N']/2;
			tab['N'] = 0;
		}
		if(tab['T'] > 0){
			tab['H'] -= tab['T'];
			tab['R'] -= tab['T'];
			tab['E'] -= 2* tab['T'];
			transl[3] += tab['T'];
			tab['T'] = 0;
		}
		if(tab['S'] > 0){
			tab['I'] -= tab['S'];
			tab['X'] -= tab['S'];
			transl[6] += tab['S'];
			tab['S'] = 0;
		}
		
		/*fr(i, 10){
			printf("transl%d", i);
		}*/
		printf("Case #%d: ", k);
		fr(i, 10){
			while(transl[i] > 0){
				printf("%d", i);
				transl[i]--;
			}
		}
		printf("\n");
	}
	
}

