#include "def.h"

typedef pair<C,PII> PCI;
typedef vector<PCI> VU;
typedef vector<VU> VUU;

#define last(A) temp[SZ(A)-1]

I main() {
	I k, N;
	string str; C a;
	VU temp;
	VUU inp;
	VI A;

	S(k);
	//P(k);
	Fe(t,1,k) {
		RSZ(i,inp) {inp[i].clear();} inp.clear(); A.clear();
		S(N); a=getchar();
		//N++;
		W(N!=0) {
			temp.clear();
			//getline (cin,str);
			//P(N);
			//Pn(str);
			//for (it = begin(str); it!=end(str); ++it) {
			//R(i,SZ(str)) {
			W(1) {
				//a=str[i];
				a=getchar();
				//P(a);
				if (a=='\n') break;
				if (SZ(temp)==0) {temp.pb(mp(a,mp(1,0)));}
				else {
					if(a==last(temp).FF) {(last(temp).YY)++;}
					else {temp.pb(mp(a,mp(1,0)));}
				}
			}
			inp.pb(temp);
			N--;
		}
		//Pn(SZ(inp));
		//	RSZ(i,inp) {RSZ(j,inp[i]){P(inp[i][j].FF); Pn(inp[i][j].YY);}}
		I len = SZ(inp[0]);
		I f=0;
		RSZ(i,inp) {/*P(SZ(inp[i])); */if(len!=SZ(inp[i])){printf("Case #%d: Fegla Won\n", t); f=1; break;}}
		if (f==1) continue;
		R(j,len) {
			I avg=0;
			f=0;
			a=inp[0][j].XX;
			RSZ(i,inp) {
				if(a!=inp[i][j].XX){printf("Case #%d: Fegla Won\n", t); f=1; break;}
				avg+=inp[i][j].YY;
			}
			if(f==1) break;
			A.pb(avg/SZ(inp));
		}
		if (f==1) continue;
		I r=0;
		R(j,len) {
			I avg= A[j];
			RSZ(i,inp) {
				if (avg > inp[i][j].YY) {r+=(avg-inp[i][j].YY);}
				else {r+=(inp[i][j].YY-avg);}
			}
		}
		printf("Case #%d: %d\n", t,r);

		//foreach(it,inp) {foreach(jt,it){P(jt.FF); Pn(jt.SS);}}
		//foreach(it,inp) {it.clear();} inp.clear();
	}
}
