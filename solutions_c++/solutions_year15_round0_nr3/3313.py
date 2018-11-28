	using namespace std;
#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i = (a), _b = (b); i <= _b; ++i)
#define FORD(i,a,b) for(int i = (a), _b = (b); i >= _b; --i)

int f[4][4] = {{1,2,3,4},{2,-1,4,-3},{3,-4,-1,2},{4,3,-2,-1}};

int conv(char c){
	if( c == 'i') return 2;
	if( c == 'j') return 3;
	return 4;
}

int multi(int x,int y){
	if(x < 0 && y < 0){
		return multi(-x,-y);
	}
	if(x < 0 && y > 0){
		return -multi(-x,y);
	}
	if(x >0 && y < 0){
		return -multi(x,-y);
	}

	return f[x - 1][y - 1];
}

int expo(int x,int m){
	if(x == -1) {
		if( m % 2 == 1) return -1;
		return 1;
	}
	if(x == 1) return 1;

	m = m % 4;
	if(m == 0) return 1;
	if(m == 1) return x;
	if(m == 2) return -1;
	return -x;
}

int ntest, l, fcal[11111],rfcal[11111];
int x;
string s;

int solve(int l,int x, string s){

	int cal = 1, rcal = 1;
	int c[5]; FOR(i,0,4) c[i] = 0;
	FOR(i,1,l){
		cal = multi(cal,conv(s[i-1]));
		fcal[i] = cal;
		rcal = multi(conv(s[l - i]),rcal);
		rfcal[l - i + 1] = rcal;
		c[conv(s[i-1])] = 1;
	}
	cal = expo(cal,x);

	if(cal != -1) return 0;
	FOR(i,1,4) c[0] += c[i];
	if(c[0] < 2) return 0;
	int findi = -1;
	FOR(i,1,l){
		int valnow = fcal[i];
		if( valnow == 2){
			if(findi == -1){
				findi = i;
			} else findi = min(findi,i);
		} else {
			FOR(j,1,4){
				if(multi( expo(fcal[l],j), valnow) == 2){
					int posnow = j * l + i;
					if(findi == -1) findi = posnow; else findi = min(findi,posnow);
					break;
				}
			}
		}
	}
	if(findi == -1) return 0;
	int findk = -1;
	FORD(i,l,1){
		int valnow = rfcal[i];
		if( valnow == 4){
			if(findk == -1){
				findk = l - i + 1;
			} else {
				findk = min(findk,l - i + 1);
			}
		} else {
			FOR(j,1,4){
				if(multi(valnow,expo(fcal[l],j)) == 4){
					int posnow = j * l + l - i + 1;
					if(findk == -1) findk = posnow; else findk = min(findi,posnow);
					break;
				}
			}
		}
	}
	if(findk == -1) return 0;
	return( (findi + findk) < (l * x));
}

int main(){
	
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	
	cin >> ntest;
	FOR(test,1,ntest){
		cin >> l >> x;
		cin >> s;
		int res = solve(l,x,s);
		printf("Case #%d: %s\n", test, res?"YES":"NO");
	}
	
	return 0;
}