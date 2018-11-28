#include<iostream>
#include<cstdio>
#include<cstring>
#define MAXN 1024
using namespace std;

int T, arr[MAXN], N, curr;
char bla[MAXN];

int main (){
    scanf ("%d",&T);

    for (int test=1; test <= T; test++){
        scanf ("%d",&N);
        N++;

        scanf ("%s",bla);

        for (int i=0; i<strlen(bla); i++)
            arr[i] = bla[i]-'0';

        curr = arr[0];
        int ans = 0;

        for (int i=1; i<N; i++){
            if (curr < i){
                ans+= (i-curr);
                curr = i;
            }
            curr+=arr[i];
        }

        printf ("Case #%d: %d\n",test, ans);
    }
    return 0;
}
