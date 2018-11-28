//Autor: Edwin Payrumani Mamani
//Fecha: April , 2014
//problem; Codejam 2014 D;
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
#define SORT(c) sort((c).begin(),(c).end())
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
	int t , n;
	double dato;
	vector<double> set1;
	vector<double> set2;
	
	cin >> t;
	while(t--){
		cases++;
		set1.clear();
		set2.clear();
		cin >> n;
		rep(i,n){
			cin >> dato;
			set1.push_back(dato);
		}
		rep(i,n){
			cin >> dato;
			set2.push_back(dato);
		}
		SORT(set1);
		SORT(set2);
		
		//cout<<set1[0]<<" "<<endl;

		int index = SZ(set2) - 1;
		int victorias = 0 , victorias_2 = 0;
		int N = SZ(set1);

		for(int i = N-1 ; i >=0 ;){
			if(set1[i] > set2[index]){
				victorias++;
				i--;
			}else{
				if(set1[i] < set2[index]){
					i--;
				    index = index - 1;
				}					
			}
		}

		int index_2 = 0;

		for(int i = 0; i < SZ(set2) && index_2 < SZ(set2);){
			if(set1[i] > set2[index_2]){
				victorias_2++;
				i++; index_2++;
			}else{
				if(set1[i] < set2[index_2]){
					i++;
				}
				
			}	
		}

		cout<<"Case #"<<cases<<": "<<victorias_2<<" "<<victorias<<endl;
	
	}

	return 0;
}


