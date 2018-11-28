#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
#include<vector>
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

vector<char>a, b;
vector<int>x, y;
string s;

int main() {
	int t, T, n;
	scan(T);
	int i, j, k;
	char e, f;
	bool flag;
	for( t = 1; t <= T; ++t ) {
		cout << "Case #" << t << ": ";
		cin >> n;
		s. reserve(n);
		flag = 0;
		a.clear();
		b.clear();
		x.clear();
		y.clear();
		cin >> s;
		for( j = 0; j < s.size(); ++j ) {
			e = s[j];
			k = 1;
			while( j < s.size() && s[j] == e ) {++j; ++k;}
			--j;
			a.push_back(e);
			x.push_back(k);
		}
		s.clear();
		cin >> s;
		for( j = 0; j < s.size(); ++j ) {
			e = s[j];
			k = 1;
			while( j < s.size() && s[j] == e ) {++j; ++k;}
			--j;
			b.push_back(e);
			y.push_back(k);
		}
		if( a.size() != b.size() ) {
			flag = 1;
		}
		else {
			for( j = 0; j < a.size(); ++j ) {
				if( a[j] != b[j] ) {
					flag = 1; break;
				}
			}
			if( flag == 0 ) {
				LL sum = 0LL;
				for( i = 0; i < x.size(); ++i ) {
					sum += (abs)(x[i]-y[i]);
				}
				cout << sum << endl;
			}
		}
		if(flag) {
			cout << "Fegla Won\n";
			continue;
		}
	}
	return 0;
}

