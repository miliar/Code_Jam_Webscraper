#include<iostream>
#include<cstdio>
#include<set>
#include<cstring>
#define For(i,a,b) for(long i = a;i<=b;i++)
#define Fo(i,a,b) for(long i = a; i<b;i++)
#define mp make_pair
#define pb push_back
#define nd second
#define fs first
#define M 2000000002
#define ll long long
#define mp make_pair
using namespace std;
typedef pair<int,char> pic;
string s;
void nhap(){
	int k,n;
	string x;
	cin>>n>>k>>x;
	s = "";
	for(int i = 1;i<=k;i++)
	s += x;
}
pic chance(char x, char y){
	if(x =='1'){
		if(y == '1') return mp(1,'1');
		if(y == 'i') return mp(1,'i');
		if(y == 'j') return mp(1,'j');
		if(y == 'k') return mp(1,'k');
	}else if(x == 'i'){
		if(y == '1') return mp(1,'i');
		if(y == 'i') return mp(-1,'1');
		if(y == 'j') return mp(1,'k');
		if(y == 'k') return mp(-1,'j');
	}else if(x == 'j'){
		if(y == '1') return mp(1,'j');
		if(y == 'i') return mp(-1,'k');
		if(y == 'j') return mp(-1,'1');
		if(y == 'k') return mp(1,'i');
	}else if(x == 'k'){
		if(y == '1') return mp(1,'k');
		if(y == 'i') return mp(1,'j');
		if(y == 'j') return mp(-1,'i');
		if(y == 'k') return mp(-1,'1');
	}
}
bool proce(){
	int Fi[10001],Fk[10001];
	int dau = 1, n = s.length();
	char c = s[0];
	pic p;
	if(c == 'i') Fi[0] = 1;
	else Fi[0] = 0;
	for(int i = 1; i< n - 2 ;i++){
		p = chance(c,s[i]);
		dau *=p.first;
		c = p.second;
		if(dau==1&&c=='i') Fi[i] = 1;
		else Fi[i] = 0;
	}
	dau = 1; 
	c = s[n-1];
	if(c == 'k') Fk[n-1] = 1;
	else Fk[n-1] = 0;
	for(int i = n-2;i>1;i--){
		p = chance(s[i],c);
		dau *=p.first;
		c = p.second;
		if(dau==1&&c=='k') Fk[i] =1;
		else Fk[i] = 0;
	}
		
	for(int i = 0; i<=n-3;i++)
	if(Fi[i]){
		dau = 1;
		c = '1';		
		for(int j = i+1; j<n-1;j++){
			p = chance(c,s[j]);
			dau *= p.first;
			c = p.second;
			if(dau==1&&c=='j'&&Fk[j+1]) return 1;
		}				
	}
	return 0;
}
int main(){
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int t;
	cin>>t;
	for(int i = 1; i<= t;i++){
		nhap();
		cout<<"Case #"<<i<<": ";
		if(proce()) cout<<"YES\n";
		else cout<<"NO\n";
	}
	return 0;
}

