#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;

bool is_perfect_square(int n) {
    if (n < 0)
        return false;
    int root(round(sqrt(n)));
    return n == root * root;
}

bool is_palindrome(int n){
	int num, digit, rev = 0;
	num = n;
	do{
		digit = num%10;
    		rev = (rev*10)+digit;
    		num = num/10;
    }while(num!=0);
    if(n==rev)
    	return true;
    else 
    	return false;
}

int main() {
  int T; 
  scanf("%d", &T);
  int A,B, count;
  for (int Ti = 1; Ti <= T; ++Ti) {
    //fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    count = 0;
    scanf("%d %d", &A, &B);
    //Check palindrome
    int n, num, digit, rev=0;
    for(int Tj = A; Tj <= B; Tj++){
    	if(is_palindrome(Tj)){	//palindrome
    		if(is_perfect_square(Tj)){
    			if(is_palindrome(sqrt(Tj)))
    				count++;
    		}
    	}
    }
    printf("Case #%d: %d\n", Ti, count);
  }
  return 0;
}
