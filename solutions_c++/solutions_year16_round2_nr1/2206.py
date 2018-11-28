#include <bits/stdc++.h>

using namespace std;
// Constants and macros
#define INF 		(int)1e9
#define EPS 		1e-9
#define bitcount 	__builtin_popcount
#define gcd 		__gcd
#define forall(i,a,b) 	for(int i=a;i<b;i++)
#define pb 		push_back
#define mp		make_pair
#define MAX(a,b)	( (a)>(b) ? (a):(b))
#define MIN(a,b)	( (a)<(b) ? (a):(b))
#define s(a)		scanf("%d", &a)
#define ss(a,b)		scanf("%d %d", &a,&b)
#define sss(a,b,c)	scanf("%d %d %d", &a,&b,&c)
#define sl(a)		scanf("%I64d", &a)

int cnt[300];
int ncnt[11];

string s;

int T;

int main(){
	s(T);
	forall(i,0,T){
		memset(cnt,0,sizeof cnt);
		memset(ncnt, 0, sizeof cnt);
		cin >> s;
		forall(k,0,(int)s.length()){
			cnt[(int)s[k]]++;
		}
		int tosub;
		if ((tosub = cnt['Z'])) {
			cnt['Z']-= tosub;
			cnt['E']-= tosub;
			cnt['R']-= tosub;
			cnt['O']-= tosub;
			ncnt[0]+=tosub;
		}
		if ((tosub = cnt['U'])) {
			cnt['F']-= tosub;
			cnt['O']-= tosub;
			cnt['U']-= tosub;
			cnt['R']-= tosub;
			ncnt[4]+=tosub;
		}
		if ((tosub = cnt['W'])) {
			cnt['T']-= tosub;
			cnt['W']-= tosub;
			cnt['O']-= tosub;
			ncnt[2]+= tosub;
		}
		if ((tosub = cnt['X'])) {
			cnt['S']-= tosub;
			cnt['I']-= tosub;
			cnt['X']-= tosub;
			ncnt[6]+=tosub;
		}
		if ((tosub = cnt['G'])) {
			cnt['E']-= tosub;
			cnt['I']-= tosub;
			cnt['G']-= tosub;
			cnt['H']-= tosub;
			cnt['T']-= tosub;
			ncnt[8]+=tosub;
		}
		if ((tosub = cnt['H'])) {
			cnt['T']-= tosub;
			cnt['H']-= tosub;
			cnt['R']-= tosub;
			cnt['E']-= tosub;
			cnt['E']-= tosub;
			ncnt[3]+=tosub;
		}
		if ((tosub = cnt['F'])) {
			cnt['F']-= tosub;
			cnt['I']-= tosub;
			cnt['V']-= tosub;
			cnt['E']-= tosub;
			ncnt[5]+=tosub;
		}
		if ((tosub = cnt['O'])) {
			cnt['O']-= tosub;
			cnt['N']-= tosub;
			cnt['E']-= tosub;
			ncnt[1]+=tosub;
		}
		if ((tosub = cnt['S'])) {
			cnt['S']-= tosub;
			cnt['E']-= tosub;
			cnt['V']-= tosub;
			cnt['E']-= tosub;
			cnt['N']-= tosub;
			ncnt[7]+=tosub;
		}
		if ((tosub = cnt['I'])) {
			cnt['N']-= tosub;
			cnt['I']-= tosub;
			cnt['N']-= tosub;
			cnt['E']-= tosub;
			ncnt[9]+=tosub;
		}
	//	forall(kk,'A','Z'+1) cout << cnt[kk] << endl;
		printf("Case #%d: ", i+1);
		forall(j,0,10){
			forall(k,0,ncnt[j]){
				printf("%d",j);
			}
		}
		printf("\n");
	}
}
