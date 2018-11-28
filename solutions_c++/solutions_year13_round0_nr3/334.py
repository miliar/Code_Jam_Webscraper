/*
ID: ksun482
LANG: C++
TASK: start
*/
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <assert.h>
#include <iostream>
#include <string.h>
#include <set>
#include <queue>
#include <complex>
#include <deque>
#include <map>
using namespace std;
#define LL int64_t

int DEBUG = 0;
int num[1000];
int answer = 0;
struct fs{
  int n;
  int sq[200];  
};
vector<fs> all;
void dfs(int k, int n, int *a, int *sq){
  if(k >= (n+1)/2){
    num[n]++;
    answer++;
    fs cur;
    cur.n = n*2-1;
    for(int i = 0; i < n*2-1; i++){
      cur.sq[i] = sq[i];
    }
    all.push_back(cur);
  } else {
    for(int m = 0; m <= 3; m++){
      if(m == 0 && k == 0) continue;
      int nsq[n*2-1];
      for(int i = 0; i < n*2-1; i++) nsq[i] = sq[i];
      a[k] = m;
      a[n-1-k] = m;
      if(0 && DEBUG){
	for(int i = 0; i < n; i++){
	  if(i <= k || i >= n-1-k){
	    cout << a[i];
	  } else {
	    cout << "?";
	  }
	}
	cout << " ";
      }
      for(int i = 0; i < n; i++){
	if(i != k && i != n-1-k) nsq[i+k] += 2*a[i]*a[k];
      }
      if(n-1-k != k){
	for(int i = 0; i < n; i++){
	  if(i != k && i != n-1-k) nsq[i+n-1-k] += 2*a[i]*a[n-1-k];
	}
      }
      nsq[n-1] += a[k]*a[n-1-k];
      if(n-1-k != k){
	nsq[n-1] += a[k]*a[n-1-k];
	nsq[2*k] += a[k]*a[k];
	nsq[2*n-2*k-2] += a[k]*a[k];
      }
      int yes = 1;
      for(int i = 0; i < n*2-1; i++) if(nsq[i] >= 10) yes = 0;
      if(0 && DEBUG){
	for(int i = 0; i < 2*n-1; i++){
	  cout << nsq[i];
	}
	cout << endl;
      }
      if(yes) dfs(k+1, n, a, nsq);
      a[k] = 0;
      a[n-1-k] = 0;
    }
  }
}

main(int argc, char **argv) {
  FILE *fin = (argc>=2) ? freopen(argv[1], "r", stdin) :
    freopen("3large.in", "r", stdin);
  assert( fin!=NULL );
  DEBUG = (argc>=3) ? atoi(argv[2]) : 0;
  if(!DEBUG) freopen("3large.out", "w", stdout);
  for(int i = 0; i < 1000; i++){
    num[i] = 0;
  }
  for(int i = 1; i <= 50; i++){
    int a[1000];
    int sq[1000];
    for(int j = 0; j < 1000; j++){
      a[j] = sq[j] = 0;
    }
    //answer = 0;
    dfs(0, i, a, sq);
    //cout << i << " " << num[i] << endl;
  }
  /*for(int i = 0; i < 41551; i++){
    cout << all[i].n << " ";
    for(int j = 0; j < all[i].n; j++){
      cout << all[i].sq[j];
    }
    cout << endl;
  }
  cout << answer << endl;*/
  int T;
  cin >> T;
  for(int ii = 0; ii < T; ii++){
    cout << "Case #" << ii + 1 << ": ";
    char a1[1000];
    char b1[1000];
    scanf("%s%s", a1, b1);
    int alen = strlen(a1);
    int blen = strlen(b1);
    int a[alen];
    int b[blen];
    for(int i = 0; i < alen; i++) a[i] = a1[i] - '0';
    for(int i = 0; i < blen; i++) b[i] = b1[i] - '0';    
    /*for(int i = 0; i < alen; i++){
      cout << a[i];
    }
    cout << " ";
    for(int i = 0; i < blen; i++){
      cout << b[i];
    }
    cout << " ";*/
    int sa = -1;
    int la = answer;

    while(la - sa > 1){
      int m = (la+sa)/2;
      int yes = 1;
      if(all[m].n > alen){
	yes = 1;
      } else if(all[m].n < alen){
	yes = 0;
      } else {
	for(int i = 0; i < alen; i++){
	  if(all[m].sq[i] > a[i]){
	    yes = 1;
	    break;
	  } else if(all[m].sq[i] < a[i]){
	    yes = 0;
	    break;
	  }
	}
      }
      if(yes){
	la = m;
      } else {
	sa = m;
      }
    }
    int sb = -1;
    int lb = answer;
    while(lb - sb > 1){
      int m = (lb+sb)/2;
      int yes = 0;
      if(all[m].n > blen){
	yes = 1;
      } else if(all[m].n < blen){
	yes = 0;
      } else {
	for(int i = 0; i < blen; i++){
	  if(all[m].sq[i] > b[i]){
	    yes = 1;
	    break;
	  } else if(all[m].sq[i] < b[i]){
	    yes = 0;
	    break;
	  }
	}
      }
      if(yes){
	lb = m;
      } else {
	sb = m;
      }
    }
    cout << sb-la+1 << endl;
  }
}

// g++ -g start.cpp; ./a.out start.in 1

// cat ../../start.cpp | sed 's/start/newtask/g' > tmp.cpp



