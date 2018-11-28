/*
 * =============================================================
 *
 *       Filename:  pali.cpp
 *    Description:  
 *         Author:  Shitikanth Kashyap (), shitikanth1@gmail.com
 *   Organization:  University of Waterloo
 *
 * ==============================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>

using namespace std;

bool is_palindrome(long long n) {
    char buffer[30];
    sprintf(buffer,"%lld",n);
    int l = strlen(buffer);
    int i = 0, j = l - 1;
    bool flag = true;
    while(i<j) {
        if (buffer[i]!=buffer[j]){
            flag = false;
            break;
        }
        i++;
        j--;
    }
    return flag;
}

long long reverse(long long n) {
    long long rev = 0;
    while(n){
        rev = rev*10+n%10;
        n = n/10;
    }
    return rev;
}

int length(long long n) {
    int ans = 0;
    while(n) {
        n /= 10;
        ans++;
    }
    return ans;
}

int next_palindrome(int p){
    int l=length(p);
    int left=p, right=0, middle=-1, pre;
    int pow=1;
    for(int i=0; i<l/2; i++){
        pow*=10;
    }
    right=left%pow;
    left=left/pow;
    if(l%2){
        middle=left%10;
        pre=left/10;
        if(reverse(pre)<right){
            middle++;
            if(middle==10){
                middle=0;
                pre++;
            }
        }
    }
    else {
        pre=left;
        if(reverse(pre)<right)
            pre++;
    }
    right=reverse(pre);

    if(l%2){
        pre*=10;
        pre+=middle;
    }
    for(int i=0; i<l/2; i++){
        pre=pre*10;
    }

    return pre+right;
}

void use(int a, int b){;}

int main(){
    int T;
    vector<int> palis;
    long long A, B;
    long long p=1;
    while(p<=1000000005) {
        if(is_palindrome(p*p)){
            palis.push_back(p);
        }
        p++;
        p = next_palindrome(p);
    }
//    printf("%d\n",palis.size());
    scanf("%d",&T);
    for (int t = 1; t<=T; t++) {
        scanf("%lld %lld",&A,&B);
        int a=floor(sqrt(A)), b=floor(sqrt(B));
        while(a*a<A) a++;
        while(b*b>B) b--;
        int ans=distance(lower_bound(palis.begin(),palis.end(),a),
                         upper_bound(palis.begin(),palis.end(),b));
        printf("Case #%d: %d\n",t,ans);
    }
}
