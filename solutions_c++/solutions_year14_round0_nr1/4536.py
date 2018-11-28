//Autor: Edwin Payrumani Mamani
//Fecha: April , 2014
//problem; Codejam 2014 A;
//#include <bits/stdc++.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <string>
#include <bitset>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <stack>
#include <sstream>

using namespace std;

#define SZ(a) int((a).size())
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())n
#define pb push_back
#define mp make_pair

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  FOR(i,0,n)
#define foreach(c,it) for(__typeof((c).begin())it = (c).begin();it!=(c).end(); it++)
#define CLR(a,b) memset(a,b,sizeof a)

typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;


int main(){
	ios_base::sync_with_stdio(0);
	
	int cases = 0;
	int fila1;
	int fila2;
	int set1[4][4];
	int set2[4][4];
	int t;
	vector<int> aux;
	vector<int> aux2;
	cin >> t;
	int dato;
	while(t--){
		cases++;
		int c = 0;
		cin >> fila1;
		rep(i,4){
			rep(j,4){
				cin >>dato;
				if(i == fila1-1){
					aux.push_back(dato);
				} 
			}
		}
		cin >> fila2;
		rep(i,4){
			rep(j,4){
				cin >>dato;
				if(i == fila2-1){
					aux2.push_back(dato);
				} 
			}
		}

		
		rep(i,SZ(aux)){
			rep(j,SZ(aux2)){
				if(aux[i] == aux2[j]){
					c++;
					if(c == 1){
						dato = aux[i];
					}
				} 
			}
		}

		if(c == 1){
			cout<<"Case #"<<cases<<": "<<dato<<endl;
		}else{
			if(c > 1){
				cout<<"Case #"<<cases<<": "<<"Bad magician!"<<endl;
			}else{
				cout<<"Case #"<<cases<<": "<<"Volunteer cheated!"<<endl;
			}
		}
		aux.clear();
		aux2.clear();

	}

	return 0;
}


