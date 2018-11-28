#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <cstdlib>
using namespace std;

int main() {
	int nums1[4];
	int nums2[4];
	int T;
	int a1,a2;
	int aux;

	cin >> T;

	for (int i=1; i<=T; i++) {
		cin >> a1;
		for (int j=0; j<4; j++) {
			for (int k=0; k<4; k++) {
				cin >> aux;
				if(j==a1-1) {
					nums1[k] = aux;
				}
			}
		}

		cin >> a2; 
    int count = 0;
    int first = 500;
		for (int j=0; j<4; j++) {
			for (int k=0; k<4; k++) {
				cin >> aux;
				if(j==a2-1) {
					for (int l=0; l<4; l++) {
            if (nums1[l] == aux) {
              count++;
              if (first == 500) first = aux;
            }
          }
				}
			}
		}
		
		if (count == 0) 
		  printf("Case #%d: Volunteer cheated!\n", i);
		else if (count == 1)
		  printf("Case #%d: %d\n", i, first);
		else
		  printf("Case #%d: Bad magician!\n", i);
  }
  
  return 0;
}

