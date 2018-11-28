/*
 * =====================================================================================
 *
 *       Filename:  b.cc
 *        Version:  1.0
 *        Created:  04/02/2015 07:22:06 PM
 *       Revision:  none
 *       Compiler:  GNU C++
 *
 *                     I  don't  want  to  be  alone.
 *
 * =====================================================================================
 */
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <cmath>
#include <string>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

#define PB              push_back
#define SIZE(x)         (int)x.size()
#define clr(x,y)        memset(x,y,sizeof(x))
#define MP(x,y)         make_pair(x,y)
#define RS(n)           scanf ("%s", n)
#define ALL(t)          (t).begin(),(t).end()
#define FOR(i,n,m)      for (int i = n; i <= m; i ++)
#define ROF(i,n,m)      for (int i = n; i >= m; i --)
#define IT              iterator
#define FF              first
#define SS              second

typedef long long               ll;
typedef unsigned int            uint;
typedef unsigned long long      ull;
typedef vector<int>             vint;
typedef vector<string>          vstring;
typedef pair<int, int>          PII;

void RI (int& x){
	x = 0;
	char c = getchar ();
	while (!(c>='0' && c<='9' || c=='-'))     c = getchar ();
	bool flag = 1;
	if (c == '-'){
		flag = 0;
		c = getchar ();
	}
	while (c >= '0' && c <= '9'){
		x = x * 10 + c - '0';
		c = getchar ();
	}
	if (!flag)      x = -x;
}
void RII (int& x, int& y){RI (x), RI (y);}
void RIII (int& x, int& y, int& z){RI (x), RI (y), RI (z);}
void RC (char& c){
	c = getchar ();
	while (c == ' '||c == '\n')     c = getchar ();
}
char RC (){
	char c = getchar ();
	while (c == ' '||c == '\n')     c = getchar ();
	return c;
}

/**************************************END define***************************************/

const ll mod = 1e9+7;
const ll LINF = 1e18;
const int INF = 1e9;
const double EPS = 1e-8;

class Solution {
public:
	double findMedianSortedArrays(int A[], int m, int B[], int n) {
		if ((m+n)&1){
			return (double)findKth (A, m, B, n, (m+n+1)/2);
		}else{
			return (findKth (A, m, B, n, (m+n)/2)+
					findKth (A, m, B, n, (m+n)/2+1))/2.0;
		}
	}
private:
	int findKth (int a[], int m, int b[], int n, int k){
		if (m == 0)	return b[k-1];
		if (n == 0)	return a[k-1];
		if (k == 1)	return min (a[0], b[0]);
		if (k == m+n)	return max (a[m-1], b[n-1]);
		int i = k/2, j = k-1-i;
		if ((i==0 || a[i-1]<=b[j]) && a[i]>=b[j])	return b[j];
		if ((j==0 || b[j-1]<=a[i]) && b[j]>=a[i])	return a[i];
		if (a[i]<=b[j])	return findKth (a+i+1, m-i-1, b, j, k-i-1);
		else	return findKth (a, i, b+j+1, n-j-1, k-j-1);
	}
};
int Volume(int * height,int n){
	int* a = height;
	int head = 0, tail = n-1;
	int maxl = a[0], maxr = a[n-1];
	int ans = 0;
	while (head < tail){
		//cout << head << " " << tail << endl;
		if (maxl <= maxr){
			for (int i = head+1; i <= tail; i ++){
				if (a[i] < maxl){
					ans += maxl - a[i];
				}else{
					maxl = a[i];
					head = i;
					break;
				}
			}
		}else{
			for (int i = tail-1; i >= head; i --){
				if (a[i] < maxr){
					ans += maxr - a[i];
				}else{
					maxr = a[i];
					tail = i;
					break;
				}
			}
		}
	}
	return ans;
}

int main (){
	/*int a[] = {
		1,0,2,1,0,1,3,2,1,2,1
	};
	cout << Volume (a, 11) << endl;
	int b[] = {
		1, 0, 0, 2
	};
	cout << Volume (b, 4) << endl;
*/
	/*int a[] = {
		1, 2, 3, 4, 5
	};
	int b[] = {
		1, 2, 3, 4, 5, 5
	};
	Solution x;
	cout << x.findMedianSortedArrays(a, 5, b, 6);
	*/
	
}
