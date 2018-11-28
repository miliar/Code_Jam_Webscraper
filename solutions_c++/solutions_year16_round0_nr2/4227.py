#include<cstdlib>
#include<iostream>
#include<fstream>
using namespace std;

int flip(char data[], int n) {
    if(data[n] == '-') {
        return n+1;
    }
    else {
        if(n == 0) return 0;
        return flip(data, n-1);
    }
    return 0;
}

int main(int argc, char const *argv[]) {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int N,tc,i,j,min;
    char buf[120], dat[60];

    scanf("%d", &N);
    for(tc=1;tc<=N;tc++){
        min = 0;
        scanf("%s", buf);
        i = 1;
        j = 0;
        dat[0] = buf[0];
        while(buf[i]){
            while(buf[i] == dat[j]) i++;
            j++;
            dat[j] = buf[i];
        }
        if(j > 0) j--;
        dat[j+1] = '\0';
        min = flip(dat, j);

        printf("Case #%d: %d\n", tc, min);
    }
    return 0;
}