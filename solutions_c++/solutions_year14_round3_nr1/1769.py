#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int i, j, k, l;
int count, n;
int gcd ( int a, int b )
{
  int c;
  while ( a != 0 ) {
     c = a; a = b%a;  b = c;
  }
  return b;
}


int main() {
	unsigned long long in1, in2;
	int ans, t, tmp;
	scanf("%d\n", &n);
//	getchar();
	for (i = 1; i <= n; i++) {
		t = 0;
		scanf("%d/%d", &in1, &in2);
		getchar();
		tmp = gcd(in1, in2);
		in1 = in1 / tmp;
		in2 = in2 / tmp;
		if (in1 < in2) {
			for (j = 0;;j++) {
				if (in1 >= in2) {
					if (t == 0) {
						t = j;
					}
					in1 -= in2;
				}
				if (in2 == 1) {
					break;
				}
				if (in2 % 2 != 0) {
					t = -1;
					break;
				}
				in2 = in2 / 2;
			
			}
		}
		else {
			t = -1;
		}
		if (t <= 0) {
			cout << "Case #"<<i<<": impossible"<<endl;
		}
		else {
			cout << "Case #"<<i<<": "<<t<<endl;
		}
		
	
	
	
	
	
	
	
	
	
	}




	return 0;

}