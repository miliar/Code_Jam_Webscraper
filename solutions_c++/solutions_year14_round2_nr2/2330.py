#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <algorithm>
#include <queue>
#include <iostream>
#include <map>
#include <string>

using namespace std;

int A,B,K;

int mask[32];
int power[32];

void preprocess() {
  mask[0] = 0;
  power[0] = 1;
  for (int i = 1;i < 32;i++) {
    power[i] = power[i-1] << 1;
    mask[i] = power[i]-1;
  }

//  for (int i = 0;i < 32;i++) {
//    printf("power = %10d, mask = %10d\n",power[i],mask[i]);
//  }

}


void readData() {
  cin >> A >> B >> K;
  if (A > B) swap(A,B);
}

int get_digit(int a,int b) {
  int i = 0;
  while(power[i] <= b) i++;

  return i-1;
}

int get_next(int a) {
  if (a == 0) return 0;
  int i = 0;
  while (a != 1) {
    a = a >> 1;
    i++;
  }
  return power[i];
}

map< pair<int,int>, int> cache;


int process(int a,int b,int k) {
  printf("calculating %d %d %d\n",a,b,k);
  if (a <= 1 && b <= 1) {
    return k+k+k+k/2;
  }
  int result = 0;
  if (a > b) swap(a,b);
  auto it = cache.find(make_pair(a,b));
  if (it != cache.end()) { return it->second; }

  int next = get_next(b);
  int value = process( (next >> 1) ,(next >> 1),k);
  result = value;
  if (a > next) {
    if (a > (next << 1)) result += value;
    else {
      result += process( (a &  (next-1)) ,next >> 1,k);
    }
  }
  if (b > next) {
    if (b > (next << 1)) result += value;
    else {
      result += process( next >> 1, (b &  (next-1)),k);
    }
  }

  cache[make_pair(a,b)] = result;
  return result;
}

int process_naive() {
  int result = 0;
  for (int i = 0;i < A;i++) {
    for (int j = 0;j < B;j++) {
      if ((i & j) < K) result++;
    }
  }
  return result;
}


int main() {
  //freopen("ex.1.in","r",stdin);
  freopen("B-small-attempt0.in","r",stdin);
  //freopen("B-large.in","r",stdin);
  int T;
  cin >> T;
  int case_id = 0;
  preprocess();

//  for (int i = 0;i <= 20;i++) {
//    printf("%d: %d (%d)\n",i,get_digit(0,i),get_next(i));
//
//  }
//  return 1;

  while (T--) {
    case_id++;
    readData();
    int result = process_naive();
    //int result2 = process(A,B,K);
    //if (result != result2) printf("FUCK\n");
    fprintf(stderr,"doing case %d A = %d B = %d K = %d\n",case_id,A,B,K);
    cout << "Case #" << case_id << ": " << result << endl; 
  }
}
