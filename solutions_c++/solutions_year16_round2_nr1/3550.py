#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

int cont[255];
vi resp;

void add(int v) {
	if(v == 0) {
		cont['Z']++;
		cont['E']++;
		cont['R']++;
		cont['O']++;
	}
	if(v == 1) {
		cont['O']++;
		cont['N']++;
		cont['E']++;
	}
	if(v == 2) {
		cont['T']++;
		cont['W']++;
		cont['O']++;
	}
	if(v == 3) {
		cont['T']++;
		cont['H']++;
		cont['R']++;
		cont['E']++;
		cont['E']++;
	}
	if(v == 4) {
		cont['F']++;
		cont['O']++;
		cont['U']++;
		cont['R']++;
	}
	if(v == 5) {
		cont['F']++;
		cont['I']++;
		cont['V']++;
		cont['E']++;
	}
	if(v == 6) {
		cont['S']++;
		cont['I']++;
		cont['X']++;
	}
	if(v == 7) {
		cont['S']++;
		cont['E']++;
		cont['V']++;
		cont['E']++;
		cont['N']++;
	}
	if(v == 8) {
		cont['E']++;
		cont['I']++;
		cont['G']++;
		cont['H']++;
		cont['T']++;
	}
	if(v == 9) {
		cont['N']++;
		cont['I']++;
		cont['N']++;
		cont['E']++;
	}
}

void rem(int v) {
	if(v == 0) {
		cont['Z']--;
		cont['E']--;
		cont['R']--;
		cont['O']--;
	}
	if(v == 1) {
		cont['O']--;
		cont['N']--;
		cont['E']--;
	}
	if(v == 2) {
		cont['T']--;
		cont['W']--;
		cont['O']--;
	}
	if(v == 3) {
		cont['T']--;
		cont['H']--;
		cont['R']--;
		cont['E']--;
		cont['E']--;
	}
	if(v == 4) {
		cont['F']--;
		cont['O']--;
		cont['U']--;
		cont['R']--;
	}
	if(v == 5) {
		cont['F']--;
		cont['I']--;
		cont['V']--;
		cont['E']--;
	}
	if(v == 6) {
		cont['S']--;
		cont['I']--;
		cont['X']--;
	}
	if(v == 7) {
		cont['S']--;
		cont['E']--;
		cont['V']--;
		cont['E']--;
		cont['N']--;
	}
	if(v == 8) {
		cont['E']--;
		cont['I']--;
		cont['G']--;
		cont['H']--;
		cont['T']--;
	}
	if(v == 9) {
		cont['N']--;
		cont['I']--;
		cont['N']--;
		cont['E']--;
	}
}

bool check() {
	for(int i = 'A'; i <= 'Z'; i++)
		if(cont[i]<0) return false;
	return true;
}

bool end() {
	for(int i = 'A'; i <= 'Z'; i++)
		if(cont[i]) return false;
	return true;
}

bool rec(int v) {
	rem(v);
	if(end()) {
		resp.push_back(v);
		return true;
	}
	if(!check()) {
		add(v);
		return false;
	}
	for(int i = v; i < 10; i++) {
		if(rec(i)) {
			resp.push_back(v);
			return true;
		}
	}
	add(v);
	return false;
} 

int main () {
	char s[2010];
	int t;
	
	scanf("%d", &t);
	
	for(int caso = 1; caso <= t; caso++) {
		scanf(" %s", s);
		int n = strlen(s);
		
		memset(cont,0,sizeof(cont));
		resp.clear();
		
		for(int i = 0; i < n; i++)
			cont[s[i]]++;
			
		for(int i = 0; i < 10; i++) {
			if(rec(i)) {
				printf("Case #%d: ", caso);
				//reverse(resp.begin(), resp.end());
				for(int j = resp.size()-1; j >= 0; j--)
					printf("%d", resp[j]);
				printf("\n");
				break;
			}
		}
	}  
  return 0;    
}
