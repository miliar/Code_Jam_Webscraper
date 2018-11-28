#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<vector>

#define f first
#define s second
#define pb push_back

using namespace std;

typedef pair<int,int> pr;
typedef long long ll;

//freopen("input.txt","r",stdin);
//freopen("output.txt","r",stdout);

int S[128],C[15];

int main() {
	int i,j,t;
	string str;
	freopen("input1.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(false);
	cin>>t;
	for(i = 1;i <= t;i++) {
		cin>>str;
		memset(C,0,sizeof(C));
		memset(S,0,sizeof(S));
		int sz = str.size();
		for(j = 0;j < sz;j++) {
			S[str[j]]++;
		} 	
		while(S['Z'] > 0) {
			S['Z']--;
			S['E']--;
			S['R']--;
			S['O']--;
			C[0]++;
		} 
		while(S['W'] > 0) {
			S['T']--;
			S['W']--;
			S['O']--;
			C[2]++;
		} 
		while(S['U'] > 0) {
			S['F']--;
			S['O']--;
			S['U']--;
			S['R']--;
			C[4]++;
		}while(S['F'] > 0) {
			S['F']--;
			S['I']--;
			S['V']--;
			S['E']--;
			C[5]++;
		} 
		while(S['X'] > 0) {
			S['S']--;
			S['I']--;
			S['X']--;
			C[6]++;
		} 
		while(S['S'] > 0) {
			S['S']--;
			S['E']--;
			S['V']--;
			S['E']--;
			S['N']--;
			C[7]++;
		}
		while(S['G'] > 0) {
			S['E']--;
			S['I']--;
			S['G']--;
			S['H']--;
			S['T']--;
			C[8]++;
		} 
		while(S['O'] > 0) {
			S['O']--;
			S['N']--;
			S['E']--;
			C[1]++;
		} 
		while(S['N'] > 0) {
			S['N']--;
			S['I']--;
			S['N']--;
			S['E']--;
			C[9]++;
		} 
		while(S['T'] > 0) {
			S['T']--;
			S['H']--;
			S['R']--;
			S['E']--;
			S['E']--;
			C[3]++;
		} 	
	
		
	
		cout<<"Case "<<"#"<<i<<":"<<" ";
		for(j = 0;j < 10;j++) {
			while(C[j]) {
				cout<<j;
				C[j]--;
			}
		}
		cout<<endl;		
	
	}
	
}
