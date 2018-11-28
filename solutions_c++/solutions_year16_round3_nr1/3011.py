#include <stdio.h>
#include <string>
using namespace std;

bool max_check(int A, int B, int C) {
    if (A<0|| B<0|| C<0) {
        return false;
    }
    
    int maj = (A+B+C)/2;

    if (A > maj || B > maj || C > maj) {
        return false;
    }
    return true;
}

int main() {
	int T, i, j, n, min, ssize, A, B, C;
	scanf("%d", &T);
	for (i=0;i<T;i++) {
		printf("Case #%d: ", i+1);
		scanf("%d", &n);
		
		if (n==3) {
		    scanf("%d%d%d", &A, &B, &C);
		} else if (n==2) {
		    scanf("%d%d", &A, &B);
		    C = 0;
		}
		
	    bool tf = (A>0 || B>0 || C>0);
	    
	    while (tf) {
		    //2s
		    if (max_check(A,B,C-2)) {
		        C = C-2;
		        printf("CC");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        }else {
		            printf("\n");
		        }
		        continue;
		    }
		    
		    if (max_check(A,B-2,C)) {
		        B = B-2;
		        printf("BB");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        }else {
		            printf("\n");
		        }
		        continue;
		    }
		    
		    if (max_check(A-2,B,C)) {
		        A = A-2;
		        printf("AA");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        }else {
		            printf("\n");
		        }
		        continue;
		    }
		    
		    if (max_check(A,B-1,C-1)) {
		        C = C-1;
		        B = B-1;
		        printf("BC");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        } else {
		            printf("\n");
		        }
		        continue;
		    }
		    
		    if (max_check(A-1,B,C-1)) {
		        C = C-1;
		        A = A-1;
		        printf("AC");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        }else {
		            printf("\n");
		        }
		        continue;
		    }
		    
		    if (max_check(A-1,B-1,C)) {
		        B = B-1;
		        A = A-1;
		        printf("AB");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        }else {
		            printf("\n");
		        }
		        continue;
		    }
		    //1s
		    if (max_check(A,B,C-1)) {
		        C =C-1;
		        printf("C");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        }else {
		            printf("\n");
		        }
		        continue;
		    }
		    if (max_check(A,B-1,C)) {
		        B =B-1;
		        printf("B");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        }else {
		            printf("\n");
		        }
		        continue;
		    }
		    if (max_check(A-1,B,C)) {
		        A =A-1;
		        printf("A");
		        tf = (A>0 || B>0 || C>0);
		        if (tf) {
		            printf(" ");
		        }else {
		            printf("\n");
		        }
		        continue;
		    }
		}
	}
	return 0;
}