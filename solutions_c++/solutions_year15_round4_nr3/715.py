# include <bits/stdc++.h>

# define ff first
# define ss second
# define mp(x,y) make_pair(x,y)
# define tr(i,c) for(__typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)

template<typename A, typename B> inline void amax(A &x, B y) {if(x < y) x = y;}
template<typename A, typename B> inline void amin(A &x, B y) {if(!(x < y)) x = y;}

typedef long long lld;

using namespace std;

map<string,int> cp, bosh;
int t, n;
string S[99];
int A[99][1000];
int uz[99];
int ak[100009], gara[100009];
int san;

ofstream fout("C.out");
ifstream fin("C.in");

void ayarla(){
	cp = bosh;
	
	san = 0;
	vector<string> ss;
	string asd;
	
	for(int i=0; i<n; i++){
		ss.resize(0);
		asd = "";
		
		for(int j=0; j<S[i].length(); j++){
			if(j == S[i].length() - 1){
				asd += S[i][j];
				ss.push_back(asd);
				break;
			}
			
			else if(S[i][j] == ' '){
				ss.push_back(asd);
				asd = "";
			}
			
			else
				asd += S[i][j];
		}
		
		uz[i] = ss.size();
		
		for(int j=0; j<uz[i]; j++){
			if(!cp[ss[j]])
				cp[ss[j]] = ++san;
			
			A[i][j] = cp[ss[j]];
		}
	}
}

int main(){
	fin >> t;
	
	for(int ti=1; ti<=t; ti++){
		fin >> n;
		
		getline(fin, S[0]);
		
		for(int i=0; i<n; i++)
			getline(fin, S[i]);
		
		ayarla();
		
		memset(ak, 0, sizeof ak);
		memset(gara, 0, sizeof gara);
		
		for(int i=0; i<uz[0]; i++)
			ak[A[0][i]]++;
		
		for(int i=0; i<uz[1]; i++)
			gara[A[1][i]]++;
		
		int shumat = 0;
		
		for(int i=1; i<=san; i++)
			if(ak[i]  &&  gara[i])
				shumat++;
			
		int nw = san;
		
		if(n == 2)
			nw = 0;
		
		n -= 2;
		
		if(n){
			for(int i=0; i<(1<<n); i++){
				int sd = 0;
				
				for(int j=0; j<n; j++){
					if(((1<<j) & i) == 0)
						for(int u=0; u<uz[j+2]; u++){
							if(gara[A[j+2][u]] != 0  &&  ak[A[j+2][u]] == 0)
								sd++;
							
							ak[A[j+2][u]]++;
						}
					
					else
						for(int u=0; u<uz[j+2]; u++){
							if(ak[A[j+2][u]] != 0  &&  gara[A[j+2][u]] == 0)
								sd++;
							
							gara[A[j+2][u]]++;
						}
				}
				
				amin(nw, sd);
				
				for(int j=0; j<n; j++){
					if(((1<<j) & i) == 0)
						for(int u=0; u<uz[j+2]; u++){
							ak[A[j+2][u]]--;
						}
					
					else
						for(int u=0; u<uz[j+2]; u++){
							gara[A[j+2][u]]--;
						}
				}
			}
		}
		
		fout << "Case #" << ti << ": " << shumat + nw << "\n";
		
		/*if(ti == 3){
			for(int i=0; i<n+2; i++){
				for(int j=0; j<uz[i]; j++)
					fout << A[i][j] << " ";
					//fout << "(" << S[i] << ")";
				fout << "\n";
			}
			
		}*/
	}
}

