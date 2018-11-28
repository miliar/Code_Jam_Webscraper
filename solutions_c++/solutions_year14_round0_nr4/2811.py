#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::sort;

int pointsNaomiWar (vector <double> N, vector <double> K);
void printVector (vector<double> v);
bool check (vector<double> N, vector <double> K);
int pointsNaomiDWar (vector <double> N, vector <double> K);

bool check (vector<double> N, vector <double> K){
	int i;
	for (i = 0; i<N.size(); ++i){
		if (N[i] < K[i]){
			return false;
		}
	}
	return true;
}
void printVector (vector<double> v){
	int i, len;
	len = v.size();
	for (i = 0; i<len; ++i){
		printf ("%.2lf ", v[i]);
	}
	printf ("\n");
}

int pointsNaomiWar (vector <double> N, vector <double> K){
	int i, j;
	bool found;
	for (i = 0; i<N.size(); ++i){
		for (j = 0; j<K.size(); ++j){
			if (K[j] > N[i]){
				N.erase(N.begin()+i);
				K.erase(K.begin()+j);
				i = 0; j = -1;
			}
		}
	}
	return N.size();
}

int pointsNaomiDWar (vector <double> N, vector <double> K){
	int p = 0;
	int i, j;
	bool ok = check (N, K);
	for (i = 0; i<N.size() && !ok; ++i){
		if (N[i] < K[i]){
			for (j = K.size()-1; j>=0 && !ok; --j){
				if (N[i] < K[j]){
					N.erase (N.begin () + i);
					K.erase (K.begin () + j);
					i = -1;
					break;
				}
			}
		}
		else{
			N.erase(N.begin()+i);
			K.erase(K.begin()+i);
			i = -1;
			p ++;
		}
		ok = check(N, K);
	}
	return p+N.size();
}

int main(){
	int t, i, x, j, pnw, pndw;
	FILE *in, *out;
	double aux;
	vector<double> n, k;

	in = fopen ("D-large.in", "r");
	out = fopen ("D-large.out", "w");

	fscanf (in,"%d",&t);
	for (i = 1; i<=t; ++i){
		fscanf (in, "%d", &x);
		for (j = 0; j<x; ++j){
			fscanf (in, "%lf", &aux);
			n.push_back (aux);
		}
		for (j = 0; j<x; ++j){
			fscanf (in, "%lf", &aux);
			k.push_back (aux);
		}
		sort(n.begin(), n.end());
		sort(k.begin(), k.end());
		pnw = pointsNaomiWar (n,k);
		pndw = pointsNaomiDWar (n, k);
		
		fprintf (out,"Case #%d: %d %d\n",i, pndw, pnw);

		n.clear();
		k.clear();
		
	}

	fclose (in);
	fclose (out);
	return 0;
}