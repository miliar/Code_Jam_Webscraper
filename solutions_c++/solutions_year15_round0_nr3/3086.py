using namespace std;
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<cassert>
#include<cstring>
#include<cmath>
#include<set>
#include<map>
#include<fstream>
#include<sstream>
typedef long double D; typedef long long LL; typedef pair<int,int> pii;
#define ALL(v) (v).begin(),(v).end()
#define REP(i, n) for (int i (0); i < (n); i ++)
#define FORIT(a,b, it) for(__typeof(b)it(a);it!=(b);++it)
#define FOREACH(v, it) FORIT((v).begin(),(v).end(),it)
#define len(v) ((int)(v).size())
#define append push_back
#define _ make_pair
#define fi first
#define se second
#define add insert
#define remove erase
#define TWO(x) (1<<(x))
#define UNIQUE(v) (v).erase(unique(ALL(v)),(v).end())
const int infInt (1010101010);
const LL  infLL  (4 * LL (infInt) * LL (infInt));

#define I 2
#define J 3
#define K 4
int mul(int a,int b){
	int multi=1;
	if(a<0)multi*=-1,a=-a;
	if(b<0)multi*=-1,b=-b;
	int ans;
	if(a==1)ans=b;else if(b==1)ans=a;else
	if(a==b)ans=-1;else
	if(((b-a)%3+3)%3==1)ans=I+J+K-a-b;else ans=-(I+J+K-a-b);
	return ans*multi;
}
int main(){
	int T; cin >> T;
	for(int it=1;it<=T;it++){
		int L,X; cin >> L >> X;
		string s;cin>>s;
		string S;REP(i,X)S+=s;
		map<char,int>M;M['i']=I,M['j']=J,M['k']=K;
		bool ok1=false,ok2=false;
		int v=1;FOREACH(S,it){v=mul(v,M[*it]);if(v==I)ok1=true;else if(v==mul(I,J)&&ok1)ok2=true;}
		//cout<<ok1<<" "<<ok2<<endl;
		printf("Case #%d: %s\n",it,(v==mul(I,mul(J,K))&&ok1&&ok2)?"YES":"NO");
	}
}
