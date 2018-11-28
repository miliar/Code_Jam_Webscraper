#include<iostream>
#include<math.h>
using namespace std;

string mmax(string a){
	string b="";
	for(int i = 0; i< a.length(); i++){
		if(a[i]=='?')b+="9";
		else b+=a[i];
	}
	return b;
}

string mmin(string a){
	string b="";
	for(int i = 0; i< a.length(); i++){
		if(a[i]=='?')b+="0";
		else b+=a[i];
	}
	return b;
}

int toNum(string a){
	int result=0;
	for(int i = 0; i< a.length(); i++){
		result*=10;
		result+=(int)(a[i]-'0');
	}
	return result;
}

int process(string p, string q, string& a, string& b){
	if(p.length()==0){
		a=p;
		b=q;
		return 0;
	}
	else if(p.length()==1){
		if(p[0]=='?'&&q[0]=='?'){
			a="0";
			b="0";
			return 0;
		}
		else if(p[0]=='?'){
			b=q;
			a=q;
			return 0;
		}
		else if(q[0]=='?'){
			b=p;
			a=p;
			return 0;
		}
		else{
			b=q;
			a=p;
			return abs((int)(a[0]-b[0]));
		}
	}
	else{		
		if(p[0]=='?'&&q[0]=='?'){
			string r,s;
			string pp,qq;
			r=p.substr(1,p.length()-1);
			s=q.substr(1,q.length()-1);
			int min=process(r,s,pp,qq);
			pp="0"+pp;
			qq="0"+qq;
			r="0"+r;
			s="1"+s;
			int dist1=toNum(mmin(s))-toNum(mmax(r));
			if(dist1<min){
				min=dist1;
				pp=mmax(r);
				qq=mmin(s);
			}
			r[0]='1';
			s[0]='0';
			int dist2=toNum(mmin(r))-toNum(mmax(s));
			if(dist2<min){
				min=dist2;
				pp=mmin(r);
				qq=mmax(s);
			}
			a=pp;
			b=qq;
			return min;
		}
		else if(p[0]=='?'){
			string r,s;
			string pp,qq;
			r=p.substr(1,p.length()-1);
			s=q.substr(1,q.length()-1);
			int min=process(r,s,pp,qq);
			pp=q[0]+pp;
			qq=q[0]+qq;
			if(q[0]!='0'){
				r=(char)((int)q[0]-1)+r;
				s=q[0]+s;
				int dist1=toNum(mmin(s))-toNum(mmax(r));
				if(dist1<=min){
					min=dist1;
					pp=mmax(r);
					qq=mmin(s);
				}
				r=r.substr(1,r.length()-1);
				s=s.substr(1,s.length()-1);
			}
			if(q[0]!='9'){
				r=(char)((int)q[0]+1)+r;
				s=q[0]+s;
				int dist2=toNum(mmin(r))-toNum(mmax(s));
				if(dist2<min){
					min=dist2;
					pp=mmin(r);
					qq=mmax(s);
				}
				r=r.substr(1,r.length()-1);
				s=s.substr(1,s.length()-1);
			}
			a=pp;
			b=qq;
			return min;
		}
		else if(q[0]=='?'){
			string r,s;
			string pp,qq;
			r=p.substr(1,p.length()-1);
			s=q.substr(1,q.length()-1);
			int min=process(r,s,pp,qq);
			pp=p[0]+pp;
			qq=p[0]+qq;
			if(p[0]!='0'){
				r=p[0]+r;
				s=(char)((int)p[0]-1)+s;
				int dist1=toNum(mmin(r))-toNum(mmax(s));
				if(dist1<=min){
					min=dist1;
					pp=mmin(r);
					qq=mmax(s);
				}
				r=r.substr(1,r.length()-1);
				s=s.substr(1,s.length()-1);
			}
			if(p[0]!='9'){
				r=p[0]+r;
				s=(char)((int)p[0]+1)+s;
				//cout << r <<endl;
				//cout << s <<endl;
				int dist2=toNum(mmin(s))-toNum(mmax(r));
				if(dist2<min){
					min=dist2;
					pp=mmax(r);
					qq=mmin(s);
				}
				r=r.substr(1,r.length()-1);
				s=s.substr(1,s.length()-1);
			}
			a=pp;
			b=qq;
			return min;
		}
		else{
			string r,s;
			string pp,qq;
			r=p.substr(1,p.length()-1);
			s=q.substr(1,q.length()-1);
			if(p[0]==q[0]){				
				int min=process(r,s,pp,qq);
				pp=p[0]+pp;
				qq=p[0]+qq;
				a=pp;
				b=qq;
				return min;
			}
			else if(p[0]>q[0]){
				r=p[0]+r;
				s=q[0]+s;
				int min=toNum(mmin(r))-toNum(mmax(s));
					a=mmin(r);
					b=mmax(s);
					return min;
			}
			else{
				r=p[0]+r;
				s=q[0]+s;
				int min=toNum(mmin(s))-toNum(mmax(r));
					a=mmax(r);
					b=mmin(s);
					return min;
			}
		}
	}
}


int main(){
	//cout << toNum("3124124");
	int t;
	cin >> t;
	
	for(int iter = 0; iter < t; iter++){
		string p,q;
		cin >> p >> q;
		string a,b;
		process(p,q,a,b);
		
		
		cout << "Case #" << iter + 1 << ": " << a << " " << b << endl;
	}

	
	return 0;
}
