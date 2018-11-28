#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
#include<iomanip> 
#include<utility> 
#include<climits>
#include<climits>
#include<cmath>
#include<algorithm>


using namespace std;


#define LL long long int
#define sc1(x) scanf("%d", &x)
#define sc2(x, y) scanf("%d%d", &x, &y)
#define sc3(x, y, z) scanf("%d%d%d", &x, &y, &z)
#define pr1(x) printf("%d\n", x)
#define FOR(i, a, n) for(int i=a;i<n;i++)
#define pp pair<int, int>
#define pb push_back 

#define MAX 20003
#define MOD 1000000007LL


char str[MAX];
int cnt[26];

string v[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int mat[10][26];


void offline() {
	FOR(i, 0, 10) {
		FOR(j, 0, v[i].size())
			mat[i][v[i][j]-'A']++;
	}

}

bool check(int x) {

	FOR(i, 0, v[x].size()) {
		//cout<<v[x][i]<<endl;
		cnt[v[x][i]-'A']--;
	}

	return true;
}

string func() {
	string result;

	//0
	while(cnt['Z'-'A']) {
		check(0);
		result += char('0'+0);
	}

	//2
	while(cnt['W'-'A']) {
		check(2);
		result += char('0'+2);
	}

	//4
	while(cnt['U'-'A']) {
		check(4);
		result += char('0'+4);
	}

	//6
	while(cnt['X'-'A']) {
		check(6);
		result += char('0'+6);
	}

	//8
	while(cnt['G'-'A']) {
		check(8);
		result += char('0'+8);
	}


	//1
	while(cnt['O'-'A']) {
		check(1);
		result += char('0'+1);
	}

	//3
	while(cnt['H'-'A']) {
		check(3);
		result += char('0'+3);
	}

	//5
	while(cnt['F'-'A']) {
		check(5);
		result += char('0'+5);
	}

	//7
	while(cnt['S'-'A']) {
		check(7);
		result += char('0'+7);
	}

	//9
	while(cnt['N'-'A']) {
		check(9);
		result += char('0'+9);
	}


	//FOR(i, 0, 26) if(cnt[i]) printf("break;\n");

	sort(result.begin(), result.end());

	return result;
}

int main() {

	offline();

	int t;

	sc1(t);
	FOR(i, 1, t+1) {
		scanf("%s", str);

		FOR(j, 0, 26) cnt[j] = 0;
		for(int j=0;str[j];j++) {
			cnt[str[j]-'A']++;
		}

		cout<<"Case #"<<i<<": "<<func()<<endl;
	} 
	return 0;
}













