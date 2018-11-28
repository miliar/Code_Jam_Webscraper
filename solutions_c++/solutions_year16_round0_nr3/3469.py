/*#include <iostream>
using namespace std;
int A[100111],B[100111];
int main(){
	int n,inc = 0,m = -1; cin >> n;
	for (int i = 1; i <= n; i++){
		cin >> A[i];
		if (A[i] >= A[i - 1]){
			inc++;
		}
		else{
			m = m < inc ? inc : m;
			inc = 1;
		}
	}
	m = m < inc ? inc : m;
	for (int i = 1; i <= n; i++){
		B[n - i + 1] = A[i];
	}
	inc = 0;
	for (int i = 1; i <= n; i++){
		if (B[i] >= B[i - 1]){
			inc++;
		}
		else{
			m = m < inc ? inc : m;
			inc = 1;
		}
	}
	m = m < inc ? inc : m;
	cout << m << endl;
	return 0;
}*/
/*#include <stdio.h>
#pragma warning(disable:4996)
#define D 1000000003
int s[1111][1111];
int main()
{
	int n, k;
	int i, j;

	scanf("%d %d", &n, &k);
	if (2 * k > n) printf("0");
	else
	{
		s[0][0] = s[1][0] = s[1][1] = 1;
		for (i = 2; i <= n; i++)
		{
			for (j = 0; j <= i / 2 + 3; j++)
			{
				if (j == 0)
					s[i][j] = 1;
				else
					s[i][j] = (s[i - 1][j] + s[i - 2][j - 1]) % D;
			}
		}
	}
	printf("%d", (s[n - 3][k - 1] + s[n - 1][k]) % D);
	return 0;
}*/
/*#include <iostream>
#include <algorithm>
using namespace std;
struct gujo{
	int x, y;
}dat[1011];
int sort1(gujo p1, gujo p2){
	if (p1.x >= p2.x) return 0;
	return 1;
}
int main(){
	int n; cin >> n;
	for (int i = 1; i <= n; i++){
		cin >> dat[i].x;
		dat[i].y = i;
	} sort(dat + 1, dat + n + 1, sort1);
	int s = 0, ans = 0;
	for (int i = 1; i <= n; i++){
		s = s + dat[i].x;
		ans = ans + s;
	}
	cout << ans << endl;
	return 0;
}*/
/*#include <stdio.h>
#include <deque>
#pragma warning(disable:4996)
using namespace std;
int pri[111];
deque<int> Q;
int main(){
	int tcase; scanf("%d", &tcase);
	while (tcase--){
		int	n, m; scanf("%d %d", &n, &m);
		Q.clear();
		for (int i = 1; i <= n; i++){
			scanf("%d", &pri[i]);
			Q.push_back(i);
		}
		int ans = 0;
		while (1){
			int x = Q.front();
			Q.pop_front();
			bool flag = true;
			deque<int>::iterator p;
			for (p = Q.begin(); p != Q.end(); ++p){
				if (pri[*p] > pri[x]){
					flag = false;
					Q.push_back(x);
					break;
				}
			}
			if (flag){
				ans++;
				if (m+1 == x){
					printf("%d\n", ans);
					break;
				}
			}
		}
	}
	return 0;
}*/
/*#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#pragma warning(disable:4996)
long long int dp[12][2048];
int n, m;
void dfs(int i, int Initial, int Target, int s){
	if (s == m){
		dp[i + 1][Target] += dp[i][Initial];
	}
	else if ((Target & (1 << s)) == 0){
		dfs(i, Initial, Target | (1 << s), s + 1);
		if (s < m - 1 && (Target & (1 << (s + 1))) == 0){
			dfs(i, Initial, Target, s + 2);
		}
	}
	else{
		dfs(i, Initial, Target & ~(1 << s), s + 1);
	}
}
int main(){
	int i, j;
	while (1){

		scanf("%d %d", &n, &m);
		if (n == 0 && m == 0) break;
		memset(dp, 0, sizeof(dp));
		dp[0][0] = 1;
		for (i = 0; i < n; i++)
		{
			for (j = 0; j < (1 << m); j++)
			{
				if (dp[i][j])
				{
					dfs(i, j, j, 0);
				}
			}
		}
		printf("%lld", dp[n][0]);
	}
	return 0;
}*/
/*#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
string word[20111];
int sort1(string x, string y){
	if (x.size() < y.size()) return 1;
	else if (x.size() == y.size() && x.compare(y) < 0) return 1;
	return 0; 
}
int main(){
	int n; cin >> n;
	for (int i = 1; i <= n; i++){
		cin >> word[i];
	}
	sort(word + 1, word + n + 1, sort1);
	for (int i = 1; i <= n; i++){
		if (word[i].compare(word[i-1]) != 0) cout << word[i] << endl;
	}
	return 0;
}*/
/*#include <stdio.h>
#include <vector>
#include <string.h>
#pragma warning(disable:4996)
using namespace std;
char paren[100111];
vector<int> S;
int main(){
	int cnt = 0, ans = 0, omg = 0;
	bool flag = false;
	scanf("%s", paren);
	int len = strlen(paren);
	for (int i = 0; i < len; i++){
		if (paren[i] == '(' && (flag == true || i == 0)){
			S.push_back(++cnt);
			flag = true;
		}
		else if (paren[i] == '(' && flag == false){
			S.push_back(++cnt);
			flag = true;
			ans = ans + omg;
		}
		else if (paren[i] == ')' && flag == true){
			flag = false;
			omg = 0;
			ans = ans + (S.back() - 1);
			cnt--;
			S.pop_back();
		}
		else if (paren[i] == ')' && flag == false){
			flag = false;
			cnt--;
			S.pop_back();
			omg++;
		}
	}
	ans = ans + omg;
	printf("%d\n", ans);
	return 0;
}*/
/*#include <iostream>
#include <stdlib.h>
using namespace std;
int n;
int hh[20][20], vh[20][20];

int a[21][21];

void input()
{
	

	int i, j;
	cin >> n;

	for (i = 0; i < n; i++) {
		cin >> hh[n - i - 1][0];

		for (j = 1; j <= hh[n - i - 1][0]; j++)
			cin >> hh[n - i - 1][j];
	}

	for (i = 0; i < n; i++) {
		cin >> vh[i][0];

		for (j = vh[i][0]; j >= 1; j--)
			cin >> vh[i][j];
	}

}

int hcheck(int i, int j)
{
	int k, t = 1, len = 0;

	a[i][j + 1] = 0;

	for (k = 0; k <= j + 1; k++) {
		if (a[i][k]) len++;

		if ((!a[i][k]) && (len != 0)) {
			if (len > hh[i][t]) return 0;
			if (len < hh[i][t])
			if ((k != j + 1) || (j == i)) return 0;

			t++;
			len = 0;
		}
	}

	if ((i == j) && (t - 1 != hh[i][0])) return 0;

	return 1;
}

int vcheck(int i, int j)
{
	int k, t = 1, len = 0;

	a[i + 1][j] = 0;

	for (k = j; k <= i + 1; k++) {
		if (a[k][j]) len++;

		if ((!a[k][j]) && (len != 0)) {
			if (len > vh[j][t]) return 0;
			if (len < vh[j][t])
			if ((k != i + 1) || (i == n - 1)) return 0;

			t++;
			len = 0;
		}
	}

	if ((i == n - 1) && (t - 1 != vh[j][0])) return 0;

	return 1;
}


void recur(int i, int j)
{
	if (i == n) {


		for (i = n - 1; i >= 0; i--) {
			for (j = 0; j <= i; j++)
				cout << a[i][j] << ' ';
			cout << endl;
		}


		exit(0);
	}

	a[i][j] = 0;
	if (hcheck(i, j) && vcheck(i, j)) {
		if (i == j) recur(i + 1, 0);
		else recur(i, j + 1);
	}

	a[i][j] = 1;
	if (hcheck(i, j) && vcheck(i, j)) {
		if (i == j) recur(i + 1, 0);
		else recur(i, j + 1);
	}
}

void process()
{
	recur(0, 0);



	cout << "No Answer" << endl;


}

void main()
{
	input();
	process();
}
*/
/*#include <iostream>
using namespace std;
int n;
char l[111][111] = { 0, };
void input(){
	cin >> n;
	int a, b;
	for (int i = 0; i < n; i++) {
		cin >> a >> b;
		if (a < b) l[a][b] = 1;
		else l[b][a] = 1;
	}
}
void process(){
	int table[111][111] = { 0, };
	int i, j, k, t;
	for (t = 1; t <= 99; t++){
		for (i = 1; i <= 100 - t; i++) {
			j = i + t;
			for (k = i; k <= j; k++){
				if (table[i][k - 1] + table[k + 1][j - 1] + l[k][j] > table[i][j])
					table[i][j] = table[i][k - 1] + table[k + 1][j - 1] + l[k][j];
			}
		}
	}
	cout << table[1][100];
}

int main(){
	input();
	process();
	return 0;
}

*/
/*#include <iostream>
#include <string.h>
using namespace std;
const int net[8][2][3] = { { { 1, 5, 0 }, { 1, 1, 0 } },  // start
{ { 1, 2, 0 }, { 1, 7, 0 } },  // 1
{ { 1, 3, 0 }, { 1, 7, 0 } },  // 2
{ { 1, 3, 0 }, { 1, 4, 0 } },  // 3
{ { 1, 5, 0 }, { 2, 1, 4 } },  // 4
{ { 1, 7, 0 }, { 1, 6, 0 } },  // 5
{ { 1, 5, 0 }, { 1, 1, 0 } },  // 6
{ { 1, 7, 0 }, { 1, 7, 0 } } }; // error

int check(char str[])
{
	int oldstatus[8], newstatus[8];
	int i, j;

	for (i = 0; i < 8; i++) {
		oldstatus[i] = 0;
		newstatus[i] = 0;
	}
	oldstatus[0] = 1;

	for (i = 0; i < strlen(str); i++) {
		for (j = 0; j < 8; j++)
		if (oldstatus[j] == 1)
		for (int k = 1; k <= net[j][str[i] - '0'][0]; k++)
			newstatus[net[j][str[i] - '0'][k]] = 1;

		for (j = 0; j < 8; j++) {
			oldstatus[j] = newstatus[j];
			newstatus[j] = 0;
		}
	}

	if ((oldstatus[4] == 1) || (oldstatus[6] == 1)) return 1;
	return 0;
}

void main()
{
	int n;
	char str[255];

	while (cin >> str){
		if (check(str)) cout << "SUBMARINE" << endl;
		else cout << "NOISE" << endl;
	}
	
}*/
/*#include <iostream>
#include <stdio.h>
#pragma warning(disable:4996)
using namespace std;
typedef struct {
	double x1, y1, x2, y2;
} Tbox;

Tbox a[1111];
int n;

void input()
{

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> a[i].x1 >> a[i].y1 >> a[i].x2 >> a[i].y2;
		a[i].x2 += a[i].x1;
		a[i].y2 += a[i].y1;
	}

}

int hit(double ax1, double ay1, double ax2, double ay2,
	double bx1, double by1, double bx2, double by2)
{
	if ((ax2 > bx1) && (ax1 < bx2) &&
		(ay2 > by1) && (ay1 < by2)) return 1;
	else return 0;
}

void swap(double *a, double *b)
{
	double t;

	t = *a;
	*a = *b;
	*b = t;
}

void process()
{
	double x[1111], y[1111];
	int i, j, k;

	for (i = 0; i < n; i++) {
		x[i * 2] = a[i].x1;
		x[i * 2 + 1] = a[i].x2;
		y[i * 2] = a[i].y1;
		y[i * 2 + 1] = a[i].y2;
	}

	for (i = 0; i < n * 2; i++)
	for (j = i + 1; j < n * 2; j++) {
		if (x[i] > x[j]) swap(&x[i], &x[j]);
		if (y[i] > y[j]) swap(&y[i], &y[j]);
	}

	double area = 0;
	int flag;

	for (i = 0; i < n * 2 - 1; i++)
	for (j = 0; j < n * 2 - 1; j++) {
		flag = 0;

		for (k = 0; k < n; k++)
		if (hit(x[i], y[j], x[i + 1], y[j + 1],
			a[k].x1, a[k].y1, a[k].x2, a[k].y2)) flag = 1;

		if (flag) area += (x[i + 1] - x[i]) * (y[j + 1] - y[j]);
	}


	char str[1111];
	sprintf(str, "%.2f", area);
	cout << str << endl;


}

int main()
{
	input();
	process();
}*/
/*#include <cstdio>
#include <cstring>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v[51];
int fdis[51];
int dis[51];
int main(){
	int n; scanf("%d", &n);
	while (true){
		int a, b; scanf("%d %d", &a, &b);
		if (a == -1 && b == -1)break;
		v[a].push_back(b);
		v[b].push_back(a);
	}
	for (int i = 1; i <= n; ++i){
		int score = 0;
		memset(dis, -1, sizeof(dis));
		//각 번호 시작으로 거리구하기
		int start = i;
		dis[start] = 0;
		queue<int> q;
		q.push(start);
		while (!q.empty()){
			int here = q.front(); q.pop();
			for (int j = 0; j < v[here].size(); ++j){
				int there = v[here][j];
				if (dis[there] == -1){
					dis[there] = dis[here] + 1;
					if (dis[there] > score)score = dis[there];
					q.push(there);
				}
			}
		}
		fdis[i] = score;
	}
	int  small = 87654321;
	vector<int> candi;
	for (int i = 1; i <= n; ++i){
		if (small > fdis[i]){
			candi.clear();
			candi.push_back(i);
			small = fdis[i];
		}
		else if (small >= fdis[i]){
			candi.push_back(i);
		}
	}
	printf("%d %d\n", small, candi.size());
	for (int i = 0; i < candi.size(); ++i)printf("%d ", candi[i]);
	printf("\n");
	return 0;
}*/
/*#include <stdio.h>
#define MAX_G 21
#define MAX_M 301
#pragma warning(disable:4996)
int n, m;
int give[MAX_G];
int a[MAX_G][MAX_M];
int use[MAX_G][MAX_M];
int d[MAX_G][MAX_M];

void process() {

	int i, j, k;

	for (i = 1; i <= m; i++) {
		for (j = 0; j <= n; j++) {
			for (k = 0; k <= j; k++) {
				if (d[i - 1][j - k] + a[i][k] > d[i][j]) {
					d[i][j] = d[i - 1][j - k] + a[i][k];
					use[i][j] = k;
				}
			}
		}
	}
}

int main() {

	int i, j;
	int money;
	scanf("%d %d", &n, &m);
	for (i = 1; i <= n; i++) {
		int x; scanf("%d", &x);
		for (j = 1; j <= m; j++){
			scanf("%d", &a[j][i]);
		}
	}

	process();

	j = n;
	for (i = m; i >= 1; i--) {
		give[i] = use[i][j];
		j -= give[i];
	}
	printf("%d\n", d[m][n]);
	for (i = 1; i <= m; i++)
		printf("%d ", give[i]);
	printf("\n");
	return 0;
}*/
/*#include <stdio.h>
#define MOD 10000003
#pragma warning(disable:4996)
int main(){
	int n; scanf("%d", &n);
	for (int i = 1; i <= n; i++){
		scanf("%d", &ar[i]);
		if (ar[i] == 1){
			ans = ans + ex[n];
		}
	}
	ex[0] = 1;
	for (int i = 1; i <= 100; i++){
		ex[i] = (ex[i - 1] * 2) % MOD;
	}
	for (int i = 1; i <= n; i++){
		for (int j = i + 1; j <= n; j++){
			bool flag = true;
			for (int k = 2; k <= sqrt(ar[i] < ar[j] ? ar[j] : ar[i]); k++){
				if (ar[i] % k == 0 && ar[j] % k == 0){
					flag = false;
					break;
				}
			}
			if (flag){
				ans = ans + ex[n - 1];
			}
		}
	}
	printf("%d\n", ans);
	return 0;
}
*/
/*#include <stdio.h>
#pragma warning(disable:4996)
bool chk[10];
int main(){
	int tcase;
	FILE *in = freopen("A-large.in", "r", stdin);
	FILE *out = freopen("output.txt", "w", stdout);
	scanf("%d", &tcase);
	for (int i1 = 1; i1 <= tcase; i1++){
		int N;
		scanf("%d", &N);
		if (N == 0){
			printf("Case #%d: INSOMNIA\n", i1);
			continue;
		}
		for (int i = 0; i <= 9; i++) chk[i] = false;
		int num = N;
		while (1){
			int x = num; 
			while (x != 0){
				chk[x % 10] = true;
				x /= 10;
			}
			bool flag = true;
			for (int i = 0; i <= 9; i++){
				if (!chk[i]){
					flag = false;
					break;
				}
			}
			if (flag){
				printf("Case #%d: %d\n",i1, num);
				break;
			}
			num = num + N;
		}
	}
	return 0;
}*/
#include <stdio.h>
#include <math.h>
#pragma warning(disable:4996)
int bA[17];
int ans[11];
int main(){
	int T, dap = 0; bool sw1;
	FILE *in = freopen("C-small-attempt0.in", "r", stdin);
	FILE *out = freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int i1 = 1; i1 <= T; i1++){
		sw1 = false; dap = 0;
		int N, J; scanf("%d %d", &N, &J);
		printf("Case #%d:\n",i1);
		for (int i = 0; i < 1 << (N - 2); i++){
			int su = i * 2 + 1 + (1 << (N - 1)); bool flag = false;
			for (int j = 2; j <= (int)sqrt((double)su); j++){
				if (su%j == 0){
					ans[2] = j;
					flag = true;
					break;
				}
			}
			if (flag){
				// 10 -> 2
				int x = su, cnt = 0;
				while (x != 0){
					bA[++cnt] = x % 2;
					x /= 2;
				}
				for (int j = 3; j <= 10; j++){
					long long int nsu = 0, bsu = 1;
					for (int k = 1; k <= cnt; k++){
						nsu = nsu + bsu * bA[k];
						bsu = bsu * j;
					}
					flag = false;
					for (int k = 2; k <= (int)sqrt((double)nsu); k++){
						if (nsu%k == 0){
							ans[j] = k;
							flag = true;
							break;
						}
					}
					if (!flag) break;
					if (j == 10){
						for (int k = 1; k <= cnt; k++){
							printf("%d", bA[cnt - k + 1]);
						}
						for (int k = 2; k <= 10; k++){
							printf(" %d", ans[k]);
						}
						dap++;
						printf("\n");
						if (dap == J){
							sw1 = true;
							break;
						}
					}
				}
			}
			if (sw1) break;
		}
	}
	return 0;
}