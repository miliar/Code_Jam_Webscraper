#include <iostream>
#include <cstdio>
#include <algorithm>
#include <sstream>
#include <cstring>
#include <string>
#include <math.h>
#include<map>
#include <vector>
#include <queue>
#include <stack>
#include <set>
using namespace std;
int n,m,k,c,d,vol,t;
int a , b ;
int main(){
    scanf("%d",&t);
    int counter =1;
    while (t--) {
        long long res =0;
        scanf("%d %d %d",&a,&b,&k);
        for (int i =0; i<a; i++) {
            for (int j =00 ; j<b; j++) {
                if ((i&j)<k) {
                    res++;
                }
            }
        }
        printf("Case #%d: %lld\n",counter,res);
        counter++;
    }
    return 0;
}