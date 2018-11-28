/* Copyright 2015 Fyodor Dmitrievich Listvin */
#include <cassert>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <iostream>
#include <vector>
#include <cstring>
#include <string>
using namespace std;

#define fname "dijkstra"
//#define DBG
#define DB(a) #a " == " << (a) << ";	"
#define REP(n) for (int i = 0; i < (int)(n); ++i)
#define FOR(i,n) for (int i = 0; i < (int)(n); ++i)
typedef long long int lli;

#define p1 0
#define pi 1
#define pj 2
#define pk 3
#define m1 4
#define mi 5
#define mj 6
#define mk 7
#define FLAG 8
#define Q(name) (name == '1' ? 0 : name - 'h')
const int m[8][8] = {
	{	p1, 	pi, 	pj, 	pk, 	m1, 	mi, 	mj, 	mk	},
	{	pi, 	m1, 	pk, 	mj, 	mi, 	p1, 	mk, 	pj	},
	{	pj, 	mk, 	m1, 	pi, 	mj, 	pk, 	p1, 	mi	},
	{	pk, 	pj, 	mi, 	m1, 	mk, 	mj, 	pi, 	p1	},
	{	m1, 	mi, 	mj, 	mk, 	p1, 	pi, 	pj, 	pk	},
	{	mi, 	p1, 	mk, 	pj, 	pi, 	m1, 	pk, 	mj	},
	{	mj, 	pk, 	p1, 	mi, 	pj, 	mk, 	m1, 	pi	},
	{	mk, 	mj, 	pi, 	p1, 	pk, 	pj, 	mi, 	m1	}
};
inline string qname(int num){
	switch(num){
		case 0: return " 1";
		case 1: return " i";
		case 2: return " j";
		case 3: return " k";
		case 4: return "-1";
		case 5: return "-i";
		case 6: return "-j";
		case 7: return "-k";
		case FLAG: return "nan";
		default: assert(false); return 0;
	}
}

inline int binpow(int quat, lli pow){
	if (pow == 0)
		return p1;
	int half = binpow(quat, pow/2);
	if (pow&1)
		return m[m[half][half]][quat];
	else
		return m[half][half];		
}

bool check_split_clever(string s, int L, lli X){
	const int LMAX = (int)1e4+2;
	static int mem[4][LMAX];
	REP(LMAX) mem[0][i] = mem[1][i] = mem[2][i] = mem[3][i] = FLAG;

	#ifdef DBG
		static int ga, ga2 = (1<<30);
	#endif

	int c[3] = {pi, pk, m1}, r = p1;

	bool cycled = false, all3 = false;
	int result = FLAG;
	for(
			int i = 0, j = 0, pnt = 0;
			j < X && (!all3 || result == FLAG) && !cycled;
			i = (i == L-1 ? 0*(++j) : i+1)
	){
		//1. next value calculation
		r = m[r][Q(s[i])];

		//2. providing result
		if (j == 0 && i == L-1)
			result = r;
		
		//3. checking cycling
		if (mem[pnt][i] == FLAG)
			mem[pnt][i] = r;
		else
			if (mem[pnt][i] == r)
				cycled = true;
		
		//4. trying to split
		if (pnt < 3 && c[pnt] == r){
			++pnt;
			if (pnt == 3)
				all3 = true;
		}
		#ifdef DBG
			ga = j;
		#endif
		//~ cerr << DB(i) DB(j) DB(r) DB(pnt) DB(all3) DB(cycled) DB(qname(result)) << endl;
	}
	
	result = binpow(result, X);
	
	#ifdef DBG
		ga2 = min(ga2, (int)X-ga);
		cerr << DB(X-ga) DB(ga2) "	";
		if (ga2 < X - 10)
			cerr << endl << DB(s) DB(X) DB(ga) << endl;
	#endif
	
	return all3 && result == m1;	
}

bool check_split(string s, int L, lli X){
	string s2 = "";
	REP(X) s2 = s2 + s;
	s = s2;

	int c[3] = {Q('i'), Q('j'), Q('k')}, r = Q('1'), cr = Q('1'), j = 0;
	#ifdef DBG
		//~ int prvi = -1;
		//~ cerr << "	" << s << " -> ";
	#endif
	REP(s.size()){
		r = m[r][Q(s[i])], cr = m[cr][Q(s[i])];
		if (j != 2 && c[j] == r){
			#ifdef DBG
				//~ cerr << s.substr(prvi+1, i-prvi) << " ";
				//~ prvi = i;
			#endif
			++j;
			r = Q('1');
		}
	}
	
	#ifdef DBG
		//~ cerr << DB(qname(cr)) << endl;
	#endif
	return j == 2 && r == c[2];// && cr == Q('l');
}

int main(){
	#ifdef DBG
		cerr << "	DBG defined, output will appear here\n\n";
	#else
		{
			string fn;
			cout << "Waiting for file name with input (\"'filename' \")...\n";
			getline(cin, fn);
			if (fn != ""){
				fn = fn.substr(1,fn.size()-3);
				freopen(fn.c_str(),"r",stdin),
				freopen((fn+".out").c_str(),"w",stdout);
			}
			else{
				cerr << "	No argument, output will appear here\n\n";
				//~ freopen(fname".in", "r", stdin);
			}
		}
	#endif

	int T;
	cin >> T;
	REP(T){
		string s; int L; lli X;
		scanf("%d%lld", &L, &X), getchar();
		getline(cin, s);
		printf("Case #%d: %s\n", i+1, check_split_clever(s, L, X) ? "YES" : "NO");
	}
	
	//~ int t = clock();
	//~ cerr << DB(check_split_clever("jijijijijiji", 12, 1e16)) << endl;
	//~ cerr << (clock() - t)/(CLOCKS_PER_SEC/1000) << "ms\n";
	
	//~ string s;
	//~ int c = 0;
	//~ while (true){
		//~ s.resize(rand()%1000+1); lli X = rand()%1000+1;//rand()%1 + 1;
		//~ for (auto & it : s) it = 'i' + rand()%3;
		//~ 
		//~ bool slow = check_split(s, s.size(), X);
		//~ bool clever = check_split_clever(s, s.size(), X);
		//~ 
		//~ if (slow == clever){
			//~ if ((++c)%50 == 0)
				//~ cerr << "ok " << c << "\n";
		//~ }		
		//~ else {
			//~ cerr << DB(c) << endl;
			//~ cerr << "fuck : " << s << " " DB(X) << endl;
			//~ cerr << DB(clever) << DB(slow) << endl;
			//~ getchar();
		//~ }
	//~ }
	
	return 0;	
}
