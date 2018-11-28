#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

struct M {
	char m[50][50], w,h;
	static int mcount;
	M() {mcount++;}
	~M() {mcount--;}
	M(int _w, int _h) {
		mcount++;
		w=_w; h=_h;
		for(int i=0;i<w;i++) { for(int j=0;j<h;j++) { m[i][j]='*'; } }
		vacias=0;
	}
	vector<int> frente;
	void quitar_del_frente(int i) {
		int n=frente.size();
		swap(frente[i],frente[n-2]);
		swap(frente[i+1],frente[n-1]);
		frente.erase(frente.begin()+n-2,frente.begin()+n);
	}
	int vacias;
	void Vaciar(int i) {
		int x=frente[i];
		int y=frente[i+1];
		quitar_del_frente(i);
		Vaciar(x,y);
	}
	void Vaciar(int x, int y) {
		if (m[x][y]=='*') vacias++; m[x][y]=' ';
		for(int i=-1;i<2;i++) { 
			for(int j=-1;j<2;j++) { 
				if (x+i<0 || x+i>=w) continue;
				if (y+j<0 || y+j>=h) continue;
				if (m[x+i][y+j]=='*') { 
					vacias++; m[x+i][y+j]='.';
					frente.push_back(x+i);
					frente.push_back(y+j);
				}
			}
		}
	}
};
int M::mcount=0;
M resultado;

bool test (M m, int goal) {
	if (m.vacias==goal) { resultado=m; return true; }
	if (m.vacias>goal) { return false; }
	for(unsigned int i=0;i<m.frente.size();i+=2) { 
		if (m.m[m.frente[i]][m.frente[i+1]]!='.') {
			m.quitar_del_frente(i); i-=2;
		} else {
			M m2=m;
			m2.Vaciar(i);
			if (test(m2,goal)) return true;
		}
	}
	return false;
}

int main(int argc, char *argv[]) {
	ifstream fin("C-small-attempt1.in");
	ofstream fout("C-small-attempt1.out");
	int T;
	fin>>T;
	for(int I=0;I<T;I++) {
		int r,c,m;
		fin>>r>>c>>m;
		cout<<"Case #"<<I+1<<":"<<endl;
		fout<<"Case #"<<I+1<<":"<<endl;
		
		int goal=r*c-m;
		M t(r,c); 
		if (goal==1) { t.m[0][0]='c'; t.vacias++; } else {
			t.Vaciar(0,0);
		}
		if (test(t,goal)) {
			for(int i=0;i<r;i++) { 
				for(int j=0;j<c;j++) {  
					if (i==0&&j==0) { fout<<'c'; continue; }
					char c=resultado.m[i][j];
					if (c=='*') fout<<'*'; else fout<<'.';
				}
				fout<<endl;
			}
		} else {
			fout<<"Impossible"<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}

