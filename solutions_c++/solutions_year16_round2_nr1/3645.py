#include <bits/stdc++.h>
using namespace std;

#define ff first
#define ss second
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> ii;

const int MAXS = 2123;
const int INF = 0x3f3f3f;

char str[MAXS], letter[MAXS];
vector<int> d;


int main()
{
	int T, tc = 1;
	scanf("%d", &T);
	while ( T-- ) {
		scanf(" %s", str);
		d.clear();
		int tam = strlen(str);
		for ( int i = 'A'; i <= 'Z'; i++ ) {
			letter[i] = 0;
		}
		for ( int i = 0; i < tam; i++ ) {
			letter[str[i]]++;
		}	

		//EIGHT
		for ( int i = 0; i < letter['G']; i++ ) {
			d.pb(8);
		}
		for ( int i = 0; i < letter['Z']; i++ ) {
			d.pb(0);
		}
		for ( int i = 0; i < letter['W']; i++ ) {
			d.pb(2);
		}
		letter['T'] -= letter['G'] + letter['W'];
		for ( int i = 0; i < letter['T']; i++ ) {
			d.pb(3);
		}
		for ( int i = 0; i < letter['X']; i++ ) {
			d.pb(6);
		}
		letter['S'] -= letter['X'];
		for ( int i = 0; i < letter['S']; i++ ) {
			d.pb(7);
		}
		for ( int i = 0; i < letter['U']; i++ ) {
			d.pb(4);
		}
		letter['F'] -= letter['U'];
		for ( int i = 0; i < letter['F']; i++ ) {
			d.pb(5);
		}
		letter['I'] -= letter['X'] + letter['G'] + letter['F'];
		for ( int i = 0; i < letter['I']; i++ ) {
			d.pb(9);
		}
		letter['N'] -= 2*letter['I'] + letter['S'];
		for ( int i = 0; i < letter['N']; i++ ) {
			d.pb(1);
		}
		sort(d.begin(),d.end());
		printf("Case #%d: ",tc++);
		for ( vector<int>::iterator it = d.begin(); it != d.end(); it++ )
			printf("%d", *it);
		printf("\n");
	}
}