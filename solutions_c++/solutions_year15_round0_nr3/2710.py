#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

struct ijk {
	char c;
	bool sig;
};

struct ijk compute(struct ijk v, struct ijk u) {
	struct ijk rr; rr.sig=((v.sig==u.sig)?false:true);
	char a=v.c, b=u.c;
	if(a==b) {
		rr.c='1';
		if(a!=1) rr.sig=!rr.sig;
	} else if(a=='1' || b=='1') {
		if(a!='1') rr.c=a;
		else rr.c=b;
	} else if(a=='i') {
		if(b=='j')
			rr.c='k';
		if(b=='k') {
			rr.c='j';
			rr.sig=!rr.sig;
		}
	} else if(a=='j') {
		if(b=='k')
			rr.c='i';
		if(b=='i') {
			rr.c='k';
			rr.sig=!rr.sig;
		}
	} else {
		if(b=='i')
			rr.c='j';
		if(b=='j') {
			rr.c='i';
			rr.sig=!rr.sig;
		}
	}
	return rr;
}

int main(void) {
	int t; scanf("%d\n", &t);
	for(int cc=1;cc<=t;cc++) {
		int l, x;
		cin>>l>>x;
		vector<ijk> v;
		for(int ii=0;ii<l;ii++) {
			char c; cin>>c;
			struct ijk tmp; tmp.c=c; tmp.sig=false;
			v.push_back(tmp);
		}
		for(int xx=1;xx<x;xx++) {
			for(int j=0;j<l;j++)
				v.push_back(v.at(j));
		}
		if(v.size()<3) {
			printf("Case #%d: NO\n", cc);
			continue;
		}
		struct ijk tr;
		bool a=false, b=false, c=false, mod=true;
		int ii;
		for(ii=0;ii<v.size();ii++) {
			if(!mod) {
				tr=compute(tr, v.at(ii));
			} else {
				tr=v.at(ii);
				mod=false;
			}
			if(!a && !tr.sig && tr.c=='i') {
				a=true;
				mod=true;
			} else if(a && !b && !tr.sig && tr.c=='j') {
				b=true;
				mod=true;
			} else if(a && b && !c && !tr.sig && tr.c=='k') {
				c=true;
				mod=true;
				break;
			}
		}
		cerr<<"   [debug] ii = "<<ii<<endl;
		if(++ii<v.size()-1) {
			tr=v.at(ii);
			for(int j=ii+1;j<v.size();j++) {
				tr=compute(tr, v.at(j));
			}
			if(tr.sig || tr.c!='1') a=false;
		}
		cout<<"Case #"<<cc<<": "<<((a&&b&&c)?"YES":"NO")<<endl;
	}
}