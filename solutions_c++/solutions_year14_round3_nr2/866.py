#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
#include<cstring>

using namespace std;
typedef long long LL;
#define MOD 1000000007LL

//REMOVE FOR SUBMISSION
#define gx getchar
#define px putchar
#define ps putchar(' ');
#define pn putchar('\n');
/*
#define gx getchar_unlocked
#define px putchar_unlocked
#define ps putchar_unlocked(' ')
#define pn putchar_unlocked('\n')
*/
void scan(int &n){int sign=1;n=0;char c=gx();while(c<'0'||c>'9'){if(c=='-')sign=-1;c=gx();}while(c>='0'&&c<='9')n=(n<<3)+(n<<1)+c-'0',c=gx();n=n*sign;}
void lscan(LL &n){int sign=1;n=0;char c=gx();while(c<'0'||c>'9'){if(c=='-')sign=-1;c=gx();}while(c>='0'&&c<='9')n=(n<<3)+(n<<1)+c-'0',c=gx();n=n*(LL)(sign);}
int sscan(char a[]){char c=gx();while(c==' '||c=='\n')c=gx();int i=0;while(c!='\n')a[i++]=c,c=gx();a[i]=0;return i;}
int wscan(char a[]){char c=gx();while(c==' '||c=='\n')c=gx();int i=0;while(c!='\n'&&c!=' ')a[i++]=c,c=gx();a[i]=0;return i;}
void print(int n){if(n<0){n=-n;px('-');}int i=10;char o[10];do{o[--i]=(n%10)+'0';n/=10;}while(n);do{px(o[i]);}while(++i<10);}
void lprint(LL n){if(n<0LL){n=-n;px('-');}int i=21;char o[21];do{o[--i]=(n%10LL)+'0';n/=10LL;}while(n);do{px(o[i]);}while(++i<21);}
void sprint(const char*a){const char*p=a;while(*p)px(*p++);}

string cat( vector< string > v ) {
	string k;
	for( int i = 0; i < v.size(); ++i ) {
		k += v[i];
	}
	return k;
}

int check( string x ) {
	bool a[26];
	int i, j;
	for( i = 0; i < 26; ++i ) a[i] = 0;
	for( i = 0; i < x.size(); ++i ) {
		for( j = i+1; x[j] == x[i] && j < x.size(); ++j );
		if( j < x.size() && a[x[j]-97] == 1 ) return 0;
		a[x[i]-97] = 1;
		i = j-1;
	}
	return 1;
}

int main() {
	string s;
	vector<string> v;
	vector<LL> counts;
	int t, T, i, n, j;
	LL flag;
	scan(T);
	for( t = 1; t <= T; ++t ) {
		cin >> n;
		v.clear();
		s.clear();
		counts.clear();
		for( i = 0; i < n; ++i )  {
			cin >> s;
			v.push_back(s);
		}
		cout << "Case #" << t <<": ";
		flag = 0LL;
		sort( v.begin(), v.end() );
		for( i = 0; i < v.size() - 1; ++i ) {
			j = i+1;
			while( j < v.size() && v[j] == v[i] ) ++j;
			counts.push_back( (LL)(j-i) );
			i = j-1;
		}
		
		do {
			if( check( cat( v ) ) ) ++flag;
		} while( next_permutation( v.begin(), v.end() ) );
		
		for( i = 0; i < counts.size(); ++i ) {
			flag = ( flag * counts[i] ) % MOD;
		}
		cout << flag << endl;
	}
	return 0;
}

