#include <iostream>
#include <fstream>
#include <stdlib.h>
using namespace std;

enum kvadr {e,i,j,k, ne, ni, nj, nk};

kvadr multiple[8][8] = {
	 { e, i, j, k,ne,ni,nj,nk},
	 { i,ne, k,nj,ni, e,nk, j},
	 { j,nk,ne, i,nj, k, e,ni},
	 { k, j,ni,ne,nk,nj, i, e},
	 {ne,ni,nj,nk, e, i, j, k},
	 {ni, e,nk, j, i,ne, k,nj},
	 {nj, k, e,ni, j,nk,ne, i},
	 {nk,nj, i, e, k, j,ni,ne}
};

// szam^9 = szam

kvadr tokvadr(char a) {
	if (a=='i') return i;
	if (a=='j') return j;
	if (a=='k') return k;
}
string fromkvadr(kvadr a) {
	if(a==e) return " e";
	if(a==i) return " i";
	if(a==j) return " j";
	if(a==k) return " k";
	if(a==ne) return "ne";
	if(a==ni) return "ni";
	if(a==nj) return "nj";
	if(a==nk) return "nk";
}

int main() {

    freopen("in.in","r",stdin);
    freopen("out.out","w",stdout);
	int cases;
	int l,x;
	char tmp;
	bool volti, voltk, voltne;

	cin>>cases;
	for(int d=1; d<=cases; d++)
	{
	cin>>l>>x;
	kvadr szorzat[l];
	cin>>tmp;
	volti=false;
	voltk=false;
	voltne=false;
	szorzat[0] = tokvadr(tmp);
	if(szorzat[0] == i) volti=true;
	for(int y=1; y<l; y++) {
		cin>>tmp;
		szorzat[y] = multiple[szorzat[y-1]][tokvadr(tmp)];
		if(volti==false && szorzat[y] == i) volti=true;
		if(volti==true && voltk==false && szorzat[y] == k) voltk=true;
	}
	kvadr ending = szorzat[l-1];
	int xmarad,count = 1;
	kvadr szamol = ending;
	while(szamol!=e) {
		szamol = multiple[szamol][ending];
		count++;
	}
	xmarad=x%count;
	kvadr vege;
	vege = e;
	for(int z=1; z<=xmarad; z++) {
		vege = multiple[vege][ending];
	}
	if(x>18) x=18;
	for(int z = 1; z<x; z++) {
		for(int y =0; y<l; y++) {
			szorzat[y] = multiple[ending][szorzat[y]];
			if(volti==false && szorzat[y] == i) volti=true;
			if(volti==true && voltk==false && szorzat[y] == k) voltk=true;
		}
	}

	if(volti==true && voltk==true && vege == ne ) voltne =true;
	if(voltne) cout<<"Case #"<<d<<": YES"<<endl;
	else cout<<"Case #"<<d<<": NO"<<endl;
	}
	return 0;
}
