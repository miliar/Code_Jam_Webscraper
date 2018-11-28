#include "stdafx.h"
#include<stdio.h>
#include <iostream>
#include <map>

using namespace std;

FILE *stream;

bool arr[10] = {false, false, false, false, false, false, false, false, false, false};

bool seenAll() {
	for( int i = 0; i < 10; ++i ) {
		if( !arr[i] ) {
			return false;
		}
	}
	return true;
}

int countSheep(int N) {
  if( N == 0 ) {
	return 0;
  }

  for(int i = 1; i < 10000; ++i) {
	  int n = i * N;
	  do {
		int digit = n % 10;
		arr[digit] = true;
		n /= 10;
	  } while (n > 0);
	  if( seenAll() ) {
		  for( int i = 0; i < 10; ++i ) {
			arr[i] = false;
		  }
		  return i * N;
	  }
  }
  return 0;
};

int main() {
	freopen_s(&stream, "C:\\Users\\jnambiar\\Downloads\\A-small-attempt1.in", "r", stdin);
	freopen_s(&stream, "C:\\Users\\jnambiar\\Downloads\\A-small-attempt1.out", "w", stdout);

  int t;
  cin >> t;
  for(int i = 1; i <= t; ++i) {
    int a;
    cin >> a;
    int val = countSheep(a);

    cout << "Case #" << i << ": ";
	if( val == 0 ) {
      cout << "INSOMNIA" << endl;
	} else {
      cout << val << endl;
	}
  }
  cin >> t;
  return 0;
}
