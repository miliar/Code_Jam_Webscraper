#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

typedef unsigned long long LL;


int T;
LL A, B;

LL pansq[1000] = {1, 4, 9};
int pq = 3;


LL makepn(LL num, LL d)
{
    LL tnum = num;
    
    if(d != -1) {
        tnum = num * 10 + d;
    }
    
    while(num)
    {
        tnum = tnum * 10 + (num % 10);
        num /= 10;
    }
    
    return tnum;
}


bool isPan(LL num)
{
    char numstr[20];
    int i=0;
    
    while(num) {
        numstr[i++] = (char)((num % 10) + '0');
        num /= 10;
    }
    
    numstr[i] = '\0';
    
    int j;
    for(i=0, j=strlen(numstr) - 1; i<=j; i++, j--) {
        if(numstr[i] != numstr[j]) {
            break;
        }
    }
    
    if(i > j) {
        return true;
    }
    
    return false;
}


bool checkPanSq(LL num)
{
    LL psq = makepn(num, -1);
    psq *= psq;
    
    if(isPan(psq)) {
        pansq[pq++] = psq;
    }
    
    
    for(LL i=0; i < 10; i++) {
        psq = makepn(num, i);
        psq *= psq;
        
        if(isPan(psq)) {
            pansq[pq++] = psq;
        }
    }
    
    return true;
}


void genPanSq()
{
    LL nd;
    for(nd = 1; nd < 4; nd++)
    {
        LL low = (LL)pow((double)10, (double)(nd - 1));
        
        LL high = (LL)pow((double)10, (double)nd);
        
//        cout << "low: " << low << " high: " << high << endl;
        
        for(LL num = low; num < high; num++) {
            checkPanSq(num);
        }
    }
    
    sort(pansq, pansq + pq);
}


int main()
{
    
    genPanSq();
//    
//    int i;
//    for(i=0; i<pq; i++) {
//        printf("%lld\n", pansq[i]);
//    }
    
    scanf("%d", &T);
    
    for(int t=1; t<=T; t++)
    {
        scanf("%lld %lld", &A, &B);
        
        int count = 0;
        
        for(int i = 0; i < pq; i++) {
            if(pansq[i] < A) continue;
            if(pansq[i] > B) break;
            
            count++;
        }
        
        printf("Case #%d: %d\n", t, count);
    }
    
    return 0;
}