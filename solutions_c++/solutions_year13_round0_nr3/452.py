#include<cstdio>
#include<string>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
typedef long long i64;

bool palindrome(i64 N)
{
	int val[20], vl=0;
	while(N){
		val[vl++] = N%10;
		N /= 10;
	}
	for(int i=0;i<vl/2;i++) if(val[i] != val[vl-1-i]) return false;
	return true;
}

vector<pair<int, string> > cand;
int tmp[100];

void add(string S)
{
	//cand.push_back(make_pair(S.size(), S));
	for(int i=0;i<100;i++) tmp[i] = 0;
	for(int i=0;i<S.size();i++)
		for(int j=0;j<S.size();j++) tmp[i+j] += (S[i]-'0') * (S[j]-'0');
	bool flg = false;
	string ret;
	for(int i=99;i>=0;i--) if(flg || tmp[i]!=0){ ret.push_back(tmp[i]+'0'); flg = true; }
	cand.push_back(make_pair(ret.size(), ret));
}

void makeA(int ev, int p, int q, int r, int s)
{
	string tmp;
	if(ev==0){
		tmp = "0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000";
		tmp[p] = ++tmp[99-p];
		if(q>=0) tmp[q] = ++tmp[99-q];
		if(r>=0) tmp[r] = ++tmp[99-r];
		if(s>=0) tmp[s] = ++tmp[99-s];

	}else{
		--ev;
		tmp = "00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000";
		tmp[50] = ev+'0';
		tmp[p] = ++tmp[100-p];
		if(q>=0) tmp[q] = ++tmp[100-q];
		if(r>=0) tmp[r] = ++tmp[100-r];
		if(s>=0) tmp[s] = ++tmp[100-s];
	}

	int tr = 0;
	for(;;tr++) if(tmp[tr]!='0') break;

	string ret;
	for(int i=tr;i<tmp.size()-tr;i++) ret.push_back(tmp[i]);

	add(ret);
}

void gen()
{
	add(string("3"));
	for(int i=0;i<50;i++){
		makeA(0, i, -1, -1, -1);
		makeA(1, i, -1, -1, -1);
		makeA(2, i, -1, -1, -1);
		for(int j=i+1;j<50;j++){
			makeA(0, i, j, -1, -1);
			makeA(1, i, j, -1, -1);
			makeA(2, i, j, -1, -1);
			for(int k=j+1;k<50;k++){
				makeA(0, i, j, k, -1);
				makeA(1, i, j, k, -1);
				makeA(2, i, j, k, -1);
				for(int l=k+1;l<50;l++){
					makeA(0, i, j, k, l);
					makeA(1, i, j, k, l);
					makeA(2, i, j, k, l);
				}
			}
		}
	}

	for(int i=0;i<50;i++){
		makeA(0, i, i, -1, -1);
		makeA(1, i, i, -1, -1);
		makeA(2, i, i, -1, -1);
		makeA(3, i, -1, -1, -1);
		for(int j=i+1;j<50;j++){
			makeA(3, i, j, -1, -1);
		}
	}
	sort(cand.begin(), cand.end());
	//printf("%d\n", cand.size());
	//for(int i=0;i<100;i++) printf("%s\n", cand[i].second.c_str());
}

int T;
char A[105], B[105];

int solve(string S)
{
	/*
	printf("%s\n", S.c_str());
	*/
	return upper_bound(cand.begin(), cand.end(), make_pair((int)S.size(), S)) - cand.begin();
}

int main()
{
	/*
	for(int i=1;i<=300000000;i++){
		if(palindrome(i) && palindrome((i64)i * i)){
			printf("%d * %d = %lld\n", i, i, (i64)i * i);
			fflush(stdout);
		}
	}
	return 0;
	*/

	//get good numbers
	gen();

	scanf("%d", &T);
	for(int t=0;t++<T;){
		scanf("%s%s", A, B);

		string S = A;
		for(int i=S.size()-1;i>=0;i--){
			if(S[i]!='0'){
				S[i]--;
				break;
			}else S[i] = '9';
		}

		if(S[0]=='0') S.erase(S.begin());

		int cnt = -solve(S);
		S = B; cnt += solve(S);

		printf("Case #%d: %d\n", t, cnt);
	}

	return 0;
}
