#include <iostream>
#include <string>
using namespace std;

int a[1000];
string ans,tmp;
string p1,r1,s1;
string tp,tr,ts;
int main(int argc, char *argv[]) {
	freopen("A.in","r",stdin);
	freopen("A.txt","w",stdout);
	int t,n,r,p,s,rr,pp,ss,rp,ps,sr;
	cin >> t;
	for(int aa=0;aa<t;aa++) {
		cin >> n >> r >> p >> s;
		int check = 0;
		
		rr =r; pp=p;ss=s;
		
		for(int i=n;i>=1;i--) {
			rp = (p+r-s);
			ps = (p+s-r);
			sr = (s+r-p);
			if(rp & 1 || rp < 0 || ps & 1 || ps < 0 || sr & 1 || sr < 0) check = 1;
			
			ss = ps / 2; pp = rp / 2; rr = sr / 2;
			s = ss; p = pp; r= rr;

		}
		
//		if(pp ==1) ans = "P";
//		else if( rr ==1) ans = "R";
//		else if(ss == 1) ans = "S";
		//cout << pp << " " << rr << " " << ss << endl;
//		for(int i=1;i<=n;i++) {
//			int kk = ans.size();
//			tmp.clear();
//			//cout << "A    " << ans << endl;
//			for(int j = 0;j<kk;j++) {
//				if(ans.at(j) == 'R') tmp += "RS";
//				else if(ans.at(j) == 'P') tmp += "PR";
//				else tmp += "PS";
//			}
//			ans = tmp;
//		}
		
		p1 = "P";
		r1 = "R";
		s1 = "S";
		
		for(int i=1;i<=n;i++) {
			if(p1 < r1) tp = p1 + r1;
			else tp = r1 + p1;
			
			if(r1 < s1) tr = r1 + s1;
			else tr = s1 + r1;
			
			if(s1 < p1) ts = s1 + p1;
			else ts = p1 + s1;
			
			p1 = tp; r1 = tr; s1 = ts;
		}
		
		if(pp ==1) ans = p1;
		else if( rr ==1) ans = r1;
		else if(ss == 1) ans = s1;

		
		
		if(check == 0) cout << "Case #" << aa+1 << ": " << ans << endl;
		else cout << "Case #" << aa + 1 << ": IMPOSSIBLE" << endl;
	}
}