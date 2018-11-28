
// aymos (Somya Mehdiratta , IIIT Hyderabad)

#include <bits/stdc++.h>  
using namespace std;

#define MP make_pair
#define PB push_back
#define FOR(i,s,n) for(int i=(s),_n=(n);i<_n;i++)
#define CLEAR(a) memset((a),0,sizeof(a)) 
#define ALL(c) (c).begin(), (c).end()

typedef long long LL;
typedef vector<int> VI;
typedef pair<int,int> PI;

int main(int argc, char *argv[]){
	int t,x;
	scanf("%d",&t);
	FOR(j,1,t+1){
		int c = 0;
		int a = 0;
		cin>>x;
		string s;
		cin>>s;
		x = s.size();
		if(s[0] == 0){
			s[0]=1;
			++a;
		}

		FOR(i,0,x){
			if(c<i){
				a += i - c;
				c += i-c;
			}
			c+=s[i]-'0';
		}

					
		printf("Case #%d: %d\n",j,a);
	}
	return 0;
}
