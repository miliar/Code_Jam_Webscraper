#define nPROFILE

#include <cstdio>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <cmath>
#include <cstdlib>
using namespace std;

#ifdef PROFILE
#include <windows.h>
unsigned long long t_check;
unsigned long long t_ntt;
#endif

/* Data structure :
 * 
 *   unsigned int digits[101]
 *   unsigned int len
 *
 * There are only a handful of palindromic numbers whose square can also
 * be palindromic.
 * They are split in 4 categories :
 * - trivial (1, 2, 3)
 * - 1 (x) (x)* 1    where x is made of 0's and at most three 1's
 *                   (even number of digits n only)
 *                   with n = N/2-1, there are C(n,3)+C(n,2)+C(n,1)+C(n,0)
 *                   ==> (N^3 - 6 N^2 + 32 N) / 48
 * - 1 (x) y (x)* 1  where y is 0, 1 or 2
 *                   if y is 0 or 1, x can contain at most three 1's
 *                   if y is 2     , x can contain at most one   1
 *                   (odd number of digits N only)
 *                   with n = (N-3)/2, there are 2*(C(n,3)+C(n,2)+C(n,1)+C(n,0))
 *                                               + (C(n,1)+C(n,0))
 *                   ==> (N^3 - 9 N^2 + 59 N - 51) / 24
 * - 2 (0*) x (0*) 2  where x can be absent, 0 or 1*
 *                   (one possibility if even number of digits
 *                    two             if odd  number of digits)
 *                   ==> 1 if N even
 *                       2 if N odd
 *
 * For each bound A and B, with number of digits NA and NB, we must calculate
 * how many of these possible roots are included for NA and NB, and add the
 * total number of possible roots for number of digits in [NA+1, NB-1].
 *
 */

typedef struct {
  unsigned int digits[101];
  unsigned int len        ;
} Big;


void bigint_from_string(string s, Big* n) {
  unsigned int len = s.length();
  memset(n, 0, sizeof(Big));
  n->len = len;
  if (s[0] == 0) cout << "WARNING number starting with 0" << endl;
  for (unsigned int i = 0; i < len; i++)
    n->digits[i] = (unsigned int)(s[len-1-i] - '0');
}

int compare(const Big* a, const Big* b) {
  unsigned int n1 = a->len;
  unsigned int n2 = b->len;
  if (n1 > n2) return  1;
  if (n1 < n2) return -1;
  for (int i = n1 - 1; i >= 0; i--) {
    if (a->digits[i] > b->digits[i]) return  1;
    if (a->digits[i] < b->digits[i]) return -1;
  }
  return 0;
}

// n = a b (with a becoming highest significance part)
void concat(Big *a, Big *b, Big *n) {
  unsigned int len = a->len + b->len;
  memset(n, 0, sizeof(Big));
  n->len = len;
  memcpy(n->digits         , b->digits, b->len * sizeof(unsigned int));
  memcpy(n->digits + b->len, a->digits, a->len * sizeof(unsigned int));
}

// b = a b (with a becoming highest significance part)
void concat2(Big *a, Big *b) {
  unsigned int len = a->len + b->len;
  memcpy(b->digits + b->len, a->digits, a->len * sizeof(unsigned int));
  b->len = len;
}

// extract 'num' highest digits
void extract_high(Big *a, unsigned int num, Big *n) {
  memset(n, 0, sizeof(Big));
  num = min(num, a->len);
  unsigned int offset = a->len - num;
  for (unsigned int i = 0; i < num; i++)
    n->digits[i] = a->digits[offset + i];
  n->len = num;
}

// extract 'num' digits starting from 'start' (counting from lowest significance)
void extract_mid(Big *a, unsigned int start, unsigned int num, Big *n) {
  memset(n, 0, sizeof(Big));
  start = min(start    , a->len);
  num   = min(num, a->len-start);
  for (unsigned int i = 0; i < num; i++)
    n->digits[i] = a->digits[start + i];
  n->len = num;
}

void invert(Big *a, Big *n) {
  memset(n, 0, sizeof(Big));
  unsigned int len = a->len;
  n->len = len;
  for (unsigned int i = 0; i < len; i++)
    n->digits[i] = a->digits[len-1-i];
}

// crude smaller than square root
void sqrt_down(Big *a, Big *n) {
  memset(n, 0, sizeof(Big));
  unsigned int len = a->len;
  n->len = (len+1) / 2;
  if (len & 1)
    n->digits[n->len - 1] = 1;
  else
    n->digits[n->len - 1] = 3;
}

// crude bigger than square root
void sqrt_up(Big *a, Big *n) {
  memset(n, 0, sizeof(Big));
  unsigned int len = a->len + 1;
  n->len = (len+1) / 2;
  if (len & 1)
    n->digits[n->len - 1] = 1;
  else
    n->digits[n->len - 1] = 3;
}

void shift(Big *a, int i) {
  if (i < 0) return;
  memmove(a->digits + i, a->digits, a->len * sizeof(unsigned int));
  memset (a->digits    , 0        , i      * sizeof(unsigned int)); 
  a->len += i;
}

void add(Big *a, Big *b, Big *n) {
  memset(n, 0, sizeof(Big));
  unsigned int len = max(a->len, b->len) + 1;

  unsigned int carry = 0;
  unsigned int cur   = 0;

  for (unsigned int i = 0; i < len; i++) {
    cur   = a->digits[i] + b->digits[i] + carry;
    carry = cur / 10;
    n->digits[i] = cur - 10*carry;
  }

  if (n->digits[len-1] == 0) len--;
  n->len = len;
}


void add2(Big *a, Big *b) {
  unsigned int len = max(a->len, b->len) + 1;

  unsigned int carry = 0;
  unsigned int cur   = 0;

  for (unsigned int i = 0; i < len; i++) {
    cur   = a->digits[i] + b->digits[i] + carry;
    carry = cur / 10;
    b->digits[i] = cur - 10*carry;
  }

  if (b->digits[len-1] == 0) len--;
  b->len = len;
}


void add_digit(Big *a, unsigned int digit) {
  unsigned int len = a->len + 1;

  unsigned int carry = 0;
  unsigned int cur   = 0;

  cur   = a->digits[0] + digit;
  carry = cur / 10;
  a->digits[0] = cur - 10*carry;

  for (unsigned int i = 1; i < len && carry != 0; i++) {
    cur   = a->digits[i] + carry;
    carry = cur / 10;
    a->digits[i] = cur - 10*carry;
  }

  if (a->digits[len-1] == 0) len--;
  a->len = len;
}

// multiply a big integer by a single digit
void mul(const Big *a, const unsigned int digit, Big *n) {
  memset(n, 0, sizeof(Big));
  unsigned int len = a->len + 1;

  unsigned int carry = 0;
  unsigned int cur   = 0;

  for (unsigned int i = 0; i < len; i++) {
    cur   = a->digits[i] * digit + carry;
    carry = cur / 10;
    n->digits[i] = cur - 10*carry;
  }

  if (n->digits[len-1] == 0) len--;
  n->len = len;
}

// naive squaring
void square(const Big *a, Big *n) {
  Big b;
  memset(n, 0, sizeof(Big));
  unsigned int len = a->len * 2;

  for (unsigned int i = 0; i < a->len; i++) {
    mul(a, a->digits[i], &b);
    shift(&b, i);
    add2(&b, n);
  }

  if (n->digits[len-1] == 0) len--;
  n->len = len;
}

int check_palindrome(Big* n) {
  int pal = 0;
  int i;
  unsigned int sym = (n->len - 1);
  unsigned int max = sym / 2  ;

  for (i=max; i >= 0; i--)
    if (n->digits[i] != n->digits[sym-i])
      goto not_pal;

  pal = 1;
not_pal:
  return pal;
}

void display(const Big *n) {
  for (int i = n->len - 1; i >= 0; i--)
    cout << n->digits[i];
  cout << endl;
}

int check_square(const Big *n, const Big *A, const Big *B) {
  Big s;
  square(n, &s);
  if (check_palindrome(&s) && compare(&s, A) >= 0 && compare(&s, B) <= 0) {
    //cout << "found root : "; display(n);
    //display(&s);
    return 1;
  } else {
    return 0;
  }
}

int main() {
  int T, num=1;

  string sa, sb;
  Big A, B;
  Big a, b;

  Big n;
  unsigned long long found;

#ifdef PROFILE
  LARGE_INTEGER start, end, freq;
  ::QueryPerformanceFrequency(&freq);
  ::QueryPerformanceCounter(&start);
#endif

  for (cin >> T; T--;) {
    cin >> sa >> sb;
    found = 0;

    bigint_from_string(sa, &A);
    bigint_from_string(sb, &B);

    sqrt_down(&A, &a);
    sqrt_up  (&B, &b);

    // check all trivial palindromic roots : 1, 2, 3 -> 1, 4, 9
    unsigned int triv[3] = {1, 4, 9};
    for (int i =0; i < 3; i++) {
      if (A.len == 1 &&
          A.digits[0] <= triv[i] &&
          (B.len >= 2 ||
           B.digits[0] >= triv[i]))
        found++;
    }

    // loop over all root of the form 1 x x* 1
    for (unsigned int num_digits = max(a.len,(unsigned int)2);
                      num_digits <= b.len                    ; num_digits++) {
      // number size = num_digits
      memset(&n, 0, sizeof(Big));
      n.len = num_digits;

      n.digits[0           ] = 1;
      n.digits[num_digits-1] = 1;
      int first, last;
      first = 1               ;
      last  = num_digits/2 - 1;

      if (num_digits & 1) goto odd;

      // only even number of digits

      // zero 1
      //cout << "possible root: "; display(&n);
      found += check_square(&n, &A, &B);

      // one 1
      for (int i = first; i <= last; i++) {
        n.digits[i             ] = 1;
        n.digits[num_digits-1-i] = 1;
        //cout << "possible root: "; display(&n);
        found += check_square(&n, &A, &B);
        n.digits[i             ] = 0;
        n.digits[num_digits-1-i] = 0;
      }

      // two 1's
      for (int i = first; i <= last; i++) {
        for (int j = i + 1; j <= last; j++) {
          n.digits[i             ] =
          n.digits[j             ] =
          n.digits[num_digits-1-i] =
          n.digits[num_digits-1-j] = 1;
          //cout << "possible root: "; display(&n);
          found += check_square(&n, &A, &B);
          n.digits[i             ] =
          n.digits[j             ] =
          n.digits[num_digits-1-i] =
          n.digits[num_digits-1-j] = 0;
        }
      }

      // three 1's
      for (int i = first; i <= last; i++) {
        for (int j = i + 1; j <= last; j++) {
          for (int k = j + 1; k <= last; k++) {
            n.digits[i             ] =
            n.digits[j             ] =
            n.digits[k             ] =
            n.digits[num_digits-1-i] =
            n.digits[num_digits-1-j] =
            n.digits[num_digits-1-k] = 1;
            //cout << "possible root: "; display(&n);
            found += check_square(&n, &A, &B);
            n.digits[i             ] =
            n.digits[j             ] =
            n.digits[k             ] =
            n.digits[num_digits-1-i] =
            n.digits[num_digits-1-j] =
            n.digits[num_digits-1-k] = 0;
          }
        }
      }

      // now with 2
      n.digits[0           ] = 2;
      n.digits[num_digits-1] = 2;
      //cout << "possible root: "; display(&n);
      found += check_square(&n, &A, &B);

      // end for even number of digits
      continue;

odd:

      for (int y = 0; y <= 1; y++) {
        n.digits[last+1] = y;

        // zero 1
        //cout << "possible root: "; display(&n);
        found += check_square(&n, &A, &B);

        // one 1
        for (int i = first; i <= last; i++) {
          n.digits[i             ] = 1;
          n.digits[num_digits-1-i] = 1;
          //cout << "possible root: "; display(&n);
          found += check_square(&n, &A, &B);
          n.digits[i             ] = 0;
          n.digits[num_digits-1-i] = 0;
        }

        // two 1's
        for (int i = first; i <= last; i++) {
          for (int j = i + 1; j <= last; j++) {
            n.digits[i             ] =
            n.digits[j             ] =
            n.digits[num_digits-1-i] =
            n.digits[num_digits-1-j] = 1;
            //cout << "possible root: "; display(&n);
            found += check_square(&n, &A, &B);
            n.digits[i             ] =
            n.digits[j             ] =
            n.digits[num_digits-1-i] =
            n.digits[num_digits-1-j] = 0;
          }
        }

        // three 1's
        for (int i = first; i <= last; i++) {
          for (int j = i + 1; j <= last; j++) {
            for (int k = j + 1; k <= last; k++) {
              n.digits[i             ] =
              n.digits[j             ] =
              n.digits[k             ] =
              n.digits[num_digits-1-i] =
              n.digits[num_digits-1-j] =
              n.digits[num_digits-1-k] = 1;
              //cout << "possible root: "; display(&n);
              found += check_square(&n, &A, &B);
              n.digits[i             ] =
              n.digits[j             ] =
              n.digits[k             ] =
              n.digits[num_digits-1-i] =
              n.digits[num_digits-1-j] =
              n.digits[num_digits-1-k] = 0;
            }
          }
        }

        n.digits[last+1] = 0;
      }


      for (int y = 2; y <= 2; y++) {
        n.digits[last+1] = y;

        // zero 1
        //cout << "possible root: "; display(&n);
        found += check_square(&n, &A, &B);

        // one 1
        for (int i = first; i <= last; i++) {
          n.digits[i             ] = 1;
          n.digits[num_digits-1-i] = 1;
          //cout << "possible root: "; display(&n);
          found += check_square(&n, &A, &B);
          n.digits[i             ] = 0;
          n.digits[num_digits-1-i] = 0;
        }

        n.digits[last+1] = 0;
      }

      // now with 2
      n.digits[0           ] = 2;
      n.digits[num_digits-1] = 2;
      //cout << "possible root: "; display(&n);
      found += check_square(&n, &A, &B);
      n.digits[last + 1    ] = 1;
      //cout << "possible root: "; display(&n);
      found += check_square(&n, &A, &B);

    }

    printf("Case #%d: %llu\n", num++, found);
  }

#ifdef PROFILE
  ::QueryPerformanceCounter(&end);
  cout << (end.QuadPart - start.QuadPart) / static_cast<float>(freq.QuadPart) << endl;
  cout << t_ntt / static_cast<float>(freq.QuadPart) << endl;
  cout << t_check / static_cast<float>(freq.QuadPart) << endl;
#endif

}
