#include<bits/stdc++.h>
using namespace std;
#define P 0
#define R 1
#define S 2
string getAns(int &p,int &r,int &s,int n,int aim)
{
	if (n == 1){
		if (aim == P) {
			if (p == 0) return "0";
			p--;
			return "P";
		}
		else if (aim == R) {
			if (r == 0) return "0";
			r--;
			return "R";
		}
		else if (aim == S) {
			if (s == 0) return "0";
			s--;
			return "S";
		}
	}
	if (aim==P){
		int p1 = p,r1 = r,s1 = s;
		int p2 = p,r2 = r,s2 = s;
		string x1 = getAns(p1,r1,s1,n / 2,P);
		string x2 = getAns(p2,r2,s2,n / 2,R);
		if (x1 == "0" || x2 == "0") return "0"; 
		if (x1 < x2){//P + R
			p = p1;
			r = r1;
			s = s1;
			x2 = getAns(p,r,s,n / 2,R);
			if (x1 == "0" || x2 == "0") return "0"; 
			return x1 + x2;
		}
		else
		{//R + P
			p = p2;
			r = r2;
			s = s2;
			x1 = getAns(p,r,s,n / 2,P);
			if (x1 == "0" || x2 == "0") return "0"; 
			return x2 + x1;
		}
	}
	else if (aim == R)
	{
		int p1 = p,r1 = r,s1 = s;
		int p2 = p,r2 = r,s2 = s;
		string x1 = getAns(p1,r1,s1,n / 2,R);		
		string x2 = getAns(p2,r2,s2,n / 2,S);
		if (x1 == "0" || x2 == "0") return "0"; 
		if (x1 < x2){// R + S
			p = p1;
			r = r1;
			s = s1;
			x2 = getAns(p,r,s,n / 2,S);
			if (x1 == "0" || x2 == "0") return "0"; 
			return x1 + x2;
		}
		else
		{//S + R
			p = p2;
			r = r2;
			s = s2;
			x1 = getAns(p,r,s,n / 2,R);
			if (x1 == "0" || x2 == "0") return "0"; 
			return x2 + x1;
		}
	}
	else if (aim == S)
	{
		int p1 = p,r1 = r,s1 = s;
		int p2 = p,r2 = r,s2 = s;
		string x1 = getAns(p1,r1,s1,n / 2,S);	
		string x2 = getAns(p2,r2,s2,n / 2,P);
		if (x1 == "0" || x2 == "0") return "0"; 
		if (x1 < x2){// S + P
			p = p1;
			r = r1;
			s = s1;
			x2 = getAns(p,r,s,n / 2,P);
			if (x1 == "0" || x2 == "0") return "0"; 
			return x1 + x2;
		}
		else
		{//P + S
			p = p2;
			r = r2;
			s = s2;
			x1 = getAns(p,r,s,n / 2,S);
			if (x1 == "0" || x2 == "0") return "0"; 
			return x2 + x1;
		}
	}
}
int main()
{
	freopen("1.txt","r",stdin);
	freopen("1.out","w",stdout);
	int T,test = 0;
	cin>>T;
	while (T--)
	{
		int n,p,r,s,_p,_r,_s;
		cin>>n>>r>>p>>s;
		_p = p;_r = r;_s = s;
		string ans = "Z";
		string tmp = getAns(_p,_r,_s,1<<n,P);
		if (tmp!="0" && tmp < ans) ans = tmp;
		_p = p;_r = r;_s = s;
		string tmp1 = getAns(_p,_r,_s,1<<n,R);
		if (tmp1!="0" && tmp1 < ans) ans = tmp1;
		_p = p;_r = r;_s = s;
		string tmp2 = getAns(_p,_r,_s,1<<n,S);
		if (tmp2!="0" && tmp2 < ans) ans = tmp2;
		if (ans == "Z") ans = "IMPOSSIBLE";
		cout<<"Case #"<<++test<<": "<<ans<<endl;
	}
} 
