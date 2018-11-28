#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstring>
#include <string>
#include <sstream>

#define MAX_D 111

using namespace std;

string U, V;
int BigA[MAX_D], BigB[MAX_D];

void mul(int A[], int B[])
{
    int i, j, t, C[MAX_D];
    memset(C, 0, sizeof(C));
    for (i = 1; i <= A[0]; i++)
    {
        for (t=0, j=1; j <= B[0] || t; j++, t/=10)
            C[i+j-1]=(t+=C[i+j-1]+A[i]*B[j])%10;
        if (i + j - 2 > C[0]) C[0] = i + j - 2;
    }
    memcpy(A, C, sizeof(C));
}

void sub1(int A[])
{
  int B[2];
  B[0] = B[1] = 1;
  int i, t = 0;
  for (i = 1; i <= A[0]; i++) {
    A[i] -= ((i <= B[0]) ? B[i] : 0) + t;
    A[i] += (t = A[i] < 0) * 10;
  }
  for (; A[0] > 1 && !A[A[0]]; A[0]--);
}

int lessThan(int A[], int B[]) {
    if (A[0] != B[0])
        return A[0] < B[0];
    for (int i = A[0]; i >= 1; --i)
        if (A[i] < B[i])
            return 1;
        else if (A[i] > B[i])
            return 0;
    return 1;
}

void printBig(int A[]) {
  for (int i = A[0]; i >= 1; --i)
    printf("%d", A[i]);
  printf("\n");
}

inline int squareParseLess(int A[], int B[]) {
  if (2 * A[0] - 1 < B[0])
    return 1;
  
  int C[MAX_D];
  memset(C, 0, sizeof(C));
  C[0] = 2 * A[0] - 1;
  
  for (int i = 1; i <= A[0]; ++i)
    if (A[i])
      for (int j = 1; j <= A[0]; ++j)
        if (A[j])
          C[i + j - 1] += A[i] * A[j];
/*
  if (lessThan(C, B)) {
    printf("valid: ");
    printBig(A);
    printBig(C);
    printBig(B);
  }
*/
  return lessThan(C, B);
}

int cur_res;
int cur[MAX_D];

void rec(int len, int pos, int sum, int B[]) {
  cur[0] = len;
  
  if (len % 2 && pos == len / 2 + 1) {
    for (int i = 0; i <= 2; ++i)
      if (sum >= i * i) {
        cur[pos] = i;
        cur_res += squareParseLess(cur, B);
      }
    return;
  } else if (len % 2 == 0 && pos == len / 2) {
    for (int i = 0; i <= 2; ++i)
      if (sum >= 2 * i * i) {
        cur[pos] = cur[pos + 1] = i;
        cur_res += squareParseLess(cur, B);
      }
    return;
  }
  
  for (int i = pos > 1 ? 0 : 1; i < 2; ++i) {
    if (sum >= 2 * i) {
      cur[pos] = cur[len - pos + 1] = i;
      rec(len, pos + 1, sum - 2 * i, B);
    }
  }
  
  if (pos == 1) {
    cur[pos] = cur[len - pos + 1] = 2;
    rec(len, pos + 1, sum - 8, B);
  }
}

inline int ispali(long long X) {
  long long Y = 0;
  long long x = X;
  while (x) Y *= 10, Y += x % 10, x /= 10;
  return X == Y;
}

inline int isok(long long x, int X) {
//  if (x <= X && ispali(x*x))
//    printf("%d\n", x);

  return x <= X && ispali(x*x);
}

int paliLessThan(int X) {
  if (X == 1000000) return 0 + paliLessThan(X - 1);

//  printf("lessThan %d\n", X);

  int ret = 0;

  for (int i = 1; i <= 9; ++i)
    ret += isok(i, X);

  for (int x = 1; x < 1000; ++x) {
    int cp = x;
    int y = 0;
    int len = 1;
    while(cp) y *= 10, y += cp % 10, cp /= 10, len *= 10;
    
    ret += isok(x * len + y, X);
    for (int i = 0; i < 10; ++i)
      ret += isok(x * (len * 10) + i * len + y, X);
  }

  return ret;
}

int answer(long long X) {
  if (X == 0) return 0;
  int root = (int) sqrt(X);
  return paliLessThan(root);  
}

int bigAnswer(int A[]) {
  if (A[0] <= 6) {
    int small = 0;
    for (int i = A[0]; i >= 1; --i)
      small *= 10, small += A[i];
    return answer(small);
  }
  
  int res = 5;
  
  for (int i = 3; 2 * i - 1 <= A[0]; ++i) {
    cur_res = 0;
    rec(i, 1, 9, A);
      //printf("len %d: %d\n", i, cur_res);
    res += cur_res;
  }
  
  return res;
}

int main() {
  int T;
  long long A, B;

  //freopen("C.in", "r", stdin);
  //freopen("C.out", "w", stdout);

  scanf("%d", &T);

  for (int i = 1; i <= T; ++i) {
    cin >> U >> V;
    
    if (U.size() <= 6 && V.size() <= 6) {
      stringstream UU, VV;
      UU << U; VV << V;
      UU >> A; VV >> B;
      cout << "Case #" << i << ": " << answer(B) - answer(A-1) << endl;
    } else {
      BigA[0] = BigB[0] = 0;
      for (int j = U.size() - 1; j >= 0; --j)
        BigA[j+1] = U[BigA[0]] - '0', ++BigA[0];
      for (int j = V.size() - 1; j >= 0; --j)
        BigB[j+1] = V[BigB[0]] - '0', ++BigB[0];
      sub1(BigA);
        //printBig(BigA);
        //printBig(BigB);
      cout << "Case #" << i << ": " << bigAnswer(BigB) - bigAnswer(BigA) << endl;
    }
      
  }
/*
  long long res = 0;
  for (long long i = 1; i * i <= 100000000000000LL; ++i)
    if (ispali(i) && ispali(i*i))
      ++res;
  cout << "brute = " << res << endl;
*/
}
