#include <stdio.h>
#include <string.h>
#include <vector>
#include <assert.h>

using namespace std;

#define MAX 10000001LL

vector<long long> sqfs;

bool isPalin(long long n){
    char str[20];
    sprintf(str, "%lld", n);
    int len = strlen(str);
    for (int i=0; i<len/2; i++)
        if (str[i] != str[len-1-i]) return false;
    return true;
}

void Init(){
    sqfs.push_back(0);
    long long sqr;
    for (long long i=1; i<MAX; i++){
        if (isPalin(i)){
            sqr = i*i;
            if (isPalin(sqr)) sqfs.push_back(sqr);
        }
    }
}

int Search(long long key){
    int start=0, mid, end = sqfs.size()-1;
    while (start < end-1){
        mid = start + (end-start)/2;
        if (sqfs[mid] == key) return mid;
        else if (sqfs[mid] < key) start=mid;
        else end=mid-1;
    }
    if (sqfs[end] <= key) return end;
    if (sqfs[start] <= key) return start;
    assert(false);
}

int main(){
    int T;
    long long A, B;
    Init();
    scanf("%d", &T);
    for (int t=1; t<=T; t++){
        scanf("%lld %lld", &A, &B);
        printf("Case #%d: %d\n", t, Search(B) - Search(A-1));
    }
    return 0;
}

