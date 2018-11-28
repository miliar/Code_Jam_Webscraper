#include <iostream>
#include <fstream>
#include <gmp.h>
#include <cstring>
using namespace std;

void sqrt(const char *c, char *r) {
	static mpz_t n_in, n_out; static bool init=false;
	if (!init) { mpz_init(n_in); mpz_init(n_out); init=true; }
	mpz_set_str (n_in, c, 10);
	mpz_sqrt(n_out,n_in);
	mpz_get_str (r,10,n_out);
}

bool check_pow(const char *s, const char *p) {
	static mpz_t n_in, n_out; static bool init=false;
	if (!init) { mpz_init(n_in); mpz_init(n_out); init=true; }
	mpz_set_str (n_in, s, 10);
	mpz_mul(n_out,n_in,n_in);
	static char aux[1024];
	mpz_get_str (aux,10,n_out);
	return strcmp(aux,p)==0;
}

void pow(const char *c, char *r) {
	static mpz_t n_in, n_out; static bool init=false;
	if (!init) { mpz_init(n_in); mpz_init(n_out); init=true; }
	mpz_set_str (n_in, c, 10);
	mpz_mul(n_out,n_in,n_in);
	mpz_get_str (r,10,n_out);
}

void add_one(char *n, int &l) {
	if (l==0) { n[0]='1'; n[1]='\0'; l=1; return; }
	int i=l-1;
	while (n[i]=='9') {
		n[i]='0'; i--;
		if (i==-1) {
			n[0]='1'; n[l]='0'; l++; n[l]='\0';
			return;
		}
	}
	n[i]++;
}

bool less_or_equal(char *n1, int l1, char *n2, int l2) {
	if (l2==l1) {
		for(int i=0;i<l1;i++)
			if (n1[i]!=n2[i]) 
				return n1[i]<n2[i];
		return true;
	} else return l1<l2;
}

void get_next(char *n, int &l) {
	int l2=l/2; bool par=(l2*2==l);
	if (!par && n[l2]!='9') {
		n[l2]++;
		return;
	}
	static char aux[1024];
	for(int i=0;i<l2;i++) { aux[i]=n[i]; }
	int ol2=l2;
	add_one(aux,l2);
	if (par || ol2!=l2) {
		for(int i=0;i<l2;i++) 
			n[l2*2-i-1]=n[i]=aux[i];
		l=l2*2;
	} else {
		n[l2]=n[l/2];
		for(int i=0;i<l2;i++) 
			n[l2*2-i]=n[i]=aux[i];
		l=l2*2+1;
	}
	n[l]='\0';
}

void get_first(char *n, int &l) {
	int l2=l/2;
	static char aux[1024];
	for(int i=0;i<l2;i++) aux[l2-i-1]=n[i];
	bool problem=!less_or_equal(n+(l-l2),l2,aux,l2);
	for(int i=0;i<l2;i++) n[l-l2+i]=aux[i];
	if (problem) get_next(n,l);
}

bool test(char *n, int l) {
	static char aux[1024];
	n[l]='\0';
	pow(n,aux);
	int al=strlen(aux); int l2=al/2;
	for(int i=0;i<l2;i++)
		if (aux[i]!=aux[al-i-1]) return false;
	return true;
}

int main(int argc, char *argv[]) {
	
	ifstream fin("C-small-attempt1.in");
	ofstream fout("C-small-attempt1.out");
	int T;
	fin>>T;
	for(int I=0;I<T;I++) {
		char na[110],nb[110];
		fin>>na>>nb;
		char sa[110],sb[110];
		sqrt(na,sa); sqrt(nb,sb);
		int la=strlen(sa), lb=strlen(sb);
		if (!check_pow(sa,na)) add_one(sa,la);
		int r=0;
		get_first(sa,la);
		while (less_or_equal(sa,la,sb,lb)) {
			if (test(sa,la)) {
				r++;
			}
			get_next(sa,la);
		}
			
		fout<<"Case #"<<I+1<<": "<<r<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

