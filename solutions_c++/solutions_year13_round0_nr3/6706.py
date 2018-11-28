#include <stdio.h>
#include <string>
#include <stdlib.h>

using namespace std;

char * itoa(int n){
    char* ret = NULL;
    int numChars = 0;
    bool isNegative = false;
    if (n < 0) {
        n = -n;
        isNegative = true;
        numChars++;
    }
    int temp = n;
    do {
        numChars++;
        temp /= 10;
    } while ( temp );
    ret = new char[ numChars + 1 ];
    ret[numChars] = 0;
    if (isNegative) ret[0] = '-';
    int i = numChars - 1;
    do {
        ret[i--] = n%10 + '0';
        n /= 10;
    } while (n);
    return ret;
}

int snton(int a, int b, int c){
    return (a * 100) + (b * 10) + c;
}

int snton(int a, int b){
    return (a * 10) + b;
}

int palindrome(int n){
    char *a;
    a = itoa(n);
    int size = strlen(a), count = 0;
    for(int i = 0, j = size-1; i < size && j >= 0 && a[i] == a[j]; i++, j--)
        count++;
    if(count == size)
        return 1;
    return 0;
}

int main(){
    /*for(int i = 0; i < 10; i++){
        int n = i*i;
        if(palindrome(n))
            printf("%d - %d\n", i,n);
    }
    for(int i = 1; i < 10; i++){
        int n = snton(i,i);
        n *= n;
        if(palindrome(n))
            printf("%d%d - %d\n", i,i,n);
    }
    for(int i = 1; i < 10; i++){
        for(int j = 0; j < 10; j++){
            int n = snton(i, j, i);
            n *= n;
            if(palindrome(n))
                printf("%d%d%d - %d\n", i,j,i, n);
        }
    }*/
        FILE *f = fopen("out.txt", "w");
    int arr[10] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944};
    int k = 0, l = 0, cases = 0, c= 0;
    scanf("%d", &cases);
    while(c++ < cases){
        int count=0;
        scanf("%d %d", &k, &l);
        for(int i = 0; i < 10  && arr[i] <= l; i++){
            if(arr[i]>=k && arr[i] <= l){
                count++;
            }
        }
        
        printf("Case #%d: %d\n", c, count);
        fprintf(f,"Case #%d: %d\n", c, count);
    }
}