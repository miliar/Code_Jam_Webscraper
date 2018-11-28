#include <bits/stdc++.h>
 
using namespace std;
 
#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))
 
#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second
typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;

string as1, as2;
void query(string s1,string s2){
	int pos=-1;
	stringstream ss1,ss2,ss3,ss4;

	for(int i=0;i<s1.length();i++){
		if(s1[i]=='?'){pos=i;break;}
	}
	if(pos!=-1){
		for(int i=0;i<10;i++){
			s1[pos]=i+'0';
			query(s1,s2);
		}
		return;
	}
	pos=-1;
	for(int i=0;i<s2.length();i++){
		if(s2[i]=='?'){pos=i;break;}
	}
	if(pos!=-1){
		for(int i=0;i<10;i++){
			s2[pos]=i+'0';
			query(s1,s2);
		}
		return;
	}
	ss1.str(s1);ss2.str(s2);
	int t1, t2;
	ss1>>t1;ss2>>t2;
	int tas1,tas2;
	ss3.str(as1);ss4.str(as2);
	ss3>>tas1; ss4>>tas2;
	if(abs(t1-t2)<abs(tas1-tas2)){
		as1=s1;as2=s2;
		return;
	}
	if(abs(t1-t2)==abs(tas1-tas2)){
		if((t1<tas1)||(t1==tas1&&t2<tas2))
			{as1=s1;as2=s2;}

	}
	return;

}
int main(){
	int ite;
	cin>>ite;
	int co=1;
	while(ite--){
		cout<<"Case #"<<co++<<": ";
		as1="9999";as2="0";
		string s1,s2;
		cin>>s1>>s2;
		query(s1,s2);

		cout<<as1<<' '<<as2<<endl;
	}
}
