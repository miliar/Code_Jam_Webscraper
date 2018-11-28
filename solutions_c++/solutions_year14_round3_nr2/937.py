//
//// main.c
//
//#include <algorithm>
//#include <cstdio>
//#include <cmath>
//#include <cstdlib>
//#include <ctime>
//#include <functional>
//#include <bitset>
//#include <deque>
//#include <list>
//#include <map>
//#include <set>
//#include <stack>
//#include <vector>
//#include <numeric>
//#include <complex>
//#include <sstream>
//#include <iostream>
//#include <iomanip>
//#include <utility>
//
//#define i64 long long
//#define ui64 unsigned long long
//
//using namespace std;
//
//#define CODEJAM_READ_IN_FILE 1
//
////#ifdef ONLINE_JUDGE
////	#define CODEJAM_READ_IN_FILE 0
////#endif
//
//#define CODEJAM_WRITE_OUT_FILE 1
//
//vector<int> vi;
//
//int P, Q;
//
//int solve()
//{
//	
//	for (int i = 0; i <= 40; i++) {
//		i64 t = (P * (i64) powf(2, i) - Q);
//		if (t < 0) continue;
//		if (!t) return i;
//		
//		for (int j = 0; j <= 40; j++) {
//			if ((i64) powf(t, j) == Q) {
//				return i;
//			}
//		}
//	}
//	
//	return -1;
//}
//
//int main()
//{
//	if (CODEJAM_READ_IN_FILE) freopen("in.in", "r", stdin);
//	if (CODEJAM_WRITE_OUT_FILE) freopen("out.out", "w", stdout);
//	
//	int T;
//	scanf("%d\n", &T);
//	if (!T) {
//		cerr << "Check input!" << endl;
//		exit(0);
//	}
//	
//	for (int t = 1; t <= T; t++) {
//		if (CODEJAM_WRITE_OUT_FILE) cerr << "Solving: #" << t << " / " << T << endl;
//		
//		scanf("%d/%d", &P, &Q);
//		
//		int result = solve();
//		
//		printf("Case #%d: ", t);
//		
//		if (result == -1) {
//			printf("impossible\n");
//		} else {
//			printf("%d\n", result);
//		}
//		//if (t != T) cout << endl;
//		
//		//		printf("Case #%d: %s + %s = %s\n", t, a.c_str(), b.c_str(), result.c_str());
//		
//	}
//	
//	if (CODEJAM_READ_IN_FILE) fclose(stdin);
//	if (CODEJAM_WRITE_OUT_FILE) fclose(stdout);
//	
//	return 0;
//}
//



// main.c

#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <bitset>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <numeric>
#include <complex>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <utility>

#define i64 long long
#define ui64 unsigned long long

using namespace std;

#define CODEJAM_READ_IN_FILE 1

//#ifdef ONLINE_JUDGE
//	#define CODEJAM_READ_IN_FILE 0
//#endif

#define CODEJAM_WRITE_OUT_FILE 1

vector<int> vi;
vector<string> si;

int N;
int n1;
int coms;
int init_i;
//vector<int> acced;

bool valid() {
	
	string all;
	
	for (int i = 0; i < N; i++) {
		all.append(si[vi[i]]);
	}
	
	int len = (int) all.length();
	
	char last_chr = all[0];
	bool last_chr_paired = 0;
	
	bool unpair[255];
	memset(unpair, 0, 255);
	
	for (int i = 1; i < len; i++) {
		char cchr = all[i];
		if (cchr == last_chr) {
			last_chr_paired = 1;
			continue;
		} else {
			last_chr_paired = 0;
			if (i == len - 1) {
				if (unpair[cchr])
					return false;
			}
			
			if (last_chr_paired) {
				last_chr = cchr;
				continue;
			} else {
				if (unpair[cchr])
					return false;
				
				unpair[last_chr] = 1;
			}
			last_chr = cchr;
		}
	}
	
	//cout << all << endl;
	return true;
}


void swap(int *a, int *b)
{
    int m;
    m = *a;
    *a = *b;
    *b = m;
}

void perm(int list[], int k, int m)
{
    int i;
    if(k == m)
    {
		vi.clear();
        for(i = 0; i < m; i++) {
            vi.push_back(list[i]);
		}
		
		coms += valid();
		
        n1++;
    }
    else
    {
        for(i = k; i < m; i++)
        {
            swap(&list[k], &list[i]);
            perm(list, k + 1, m);
            swap(&list[k], &list[i]);
        }
    }
}

int solve()
{
	coms = 0;
	init_i = 0;
	vi.clear();
	
	int *list = (int *)malloc(4 * N);
	for (int i = 0; i < N; i++) {
		list[i] = i;
	}
	
    perm(list, 0, N);

	return coms;
}

int main()
{
	if (CODEJAM_READ_IN_FILE) freopen("in.in", "r", stdin);
	if (CODEJAM_WRITE_OUT_FILE) freopen("out.out", "w", stdout);
	
	int T;
	scanf("%d\n", &T);
	if (!T) {
		cerr << "Check input!" << endl;
		exit(0);
	}
	
	for (int t = 1; t <= T; t++) {
		if (CODEJAM_WRITE_OUT_FILE) cerr << "Solving: #" << t << " / " << T << endl;
		
		si.clear();
		
		scanf("%d\n", &N);
		int n = N;
		while (n--) {
			string str;
			cin >> str;
			si.push_back(str);
		}
		
		int result = solve();
		
		printf("Case #%d: ", t);
		
		if (result == -1) {
			printf("impossible\n");
		} else {
			printf("%d\n", result);
		}
		//if (t != T) cout << endl;
		
		//		printf("Case #%d: %s + %s = %s\n", t, a.c_str(), b.c_str(), result.c_str());
		
	}
	
	if (CODEJAM_READ_IN_FILE) fclose(stdin);
	if (CODEJAM_WRITE_OUT_FILE) fclose(stdout);
	
	return 0;
}



