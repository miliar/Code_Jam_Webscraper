#define Federico using
#define Javier namespace
#define Pousa std;
#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <stack>
#include <queue>
#include <cstring>
#include <sstream>


Federico Javier Pousa

string Ps;


string peor(long long int act, long long cuantos, int cant){
	string res = "";
	if(cuantos){
		res.push_back('1');
		res += peor(act,(cuantos-1)>>1, cant);
	}
	return res;
}

string mejor(long long int act, long long cuantos,int cant){
	string res = "";
	if(cuantos){
		res.push_back('0');
		res += mejor(act,(cuantos-1)>>1, cant);
	}
	return res;
}

int main(){	
	int T, N;
	long long P;
	cin >> T;
	for(int caso=1;caso<=T;++caso){
		cin >> N >> P;
		P--;
		Ps = "";
		while(P){
			if(P&1)Ps.push_back('1');
			if(!(P&1))Ps.push_back('0');
			P>>=1;
		}
		while((int)Ps.size()<N)Ps.push_back('0');
		reverse(Ps.begin(),Ps.end());
		//~ cerr << "Ps es: " << Ps << endl;
		cout << "Case #"<< caso << ": ";
		
		long long int inf, med, sup;
		inf = 0;
		sup = (1LL<<N);
		while(inf+1!=sup){
			med = (inf+sup)>>1;
			
			string bla = peor(med, med, N);
			while((int)bla.size()<N)bla.push_back('0'); 
			//~ cerr << "info1 " << med << " " << bla << endl;
			if(bla<=Ps){
				inf = med;
			}else{
				sup = med;
			}
		}
		cout << inf << " ";
		
		inf = 0;
		sup = (1LL<<N);
		while(inf+1!=sup){
			med = (inf+sup)>>1;
			string bla = mejor(med, (1LL<<N)-1-med, N);
			while((int)bla.size()<N)bla.push_back('1'); 
			//~ cerr << "info1 " << med << " " << bla << endl;
			if(bla>Ps){
				sup = med;
			}else{
				inf = med;
			}
		}
		cout << inf << endl;
	}
	return 0;
}
