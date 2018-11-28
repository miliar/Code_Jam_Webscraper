// Author : Mohd. Imranul Hoque Limon
// INS : Daffodil Internation University
// ID : 102-15-1036

#include <stdlib.h>
#include <cmath>
#include <algorithm>
#include <stdio.h>
#include <string.h>
#include <string>
#include <cstring>
#include <vector>
#include <set>
#include <map>
#include <iostream>
#include <cctype>
#include <deque>
#include <queue>

#define black 0
#define white 1
#define tru -1
#define fals -2
#define siz 10000000
using namespace std;

int main(){

    //#ifdef localhost
    //freopen("input.in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    //#endif


    long long  A, B, Cases, Case = 0, f, sz, n;
    long long num, i, j;
    vector <long long> v;
    vector <long long> res ;

      res.push_back(1LL);
      res.push_back(4LL);
      res.push_back(9LL);
      res.push_back(121LL);
      res.push_back(484LL);
      res.push_back(10201LL);
      res.push_back(12321LL);
      res.push_back(14641LL);
      res.push_back(40804LL);
      res.push_back(44944LL);
      res.push_back(1002001LL);
      res.push_back(1234321LL);
      res.push_back(4008004LL);
      res.push_back(100020001LL);
      res.push_back(102030201LL);
      res.push_back(104060401LL);
      res.push_back(121242121LL);
      res.push_back(123454321LL);
      res.push_back(125686521LL);
      res.push_back(400080004LL);
      res.push_back(404090404LL);
      res.push_back(10000200001LL);
      res.push_back(10221412201LL);
      res.push_back(12102420121LL);
      res.push_back(12345654321LL);
      res.push_back(40000800004LL);
      res.push_back(1000002000001LL);
      res.push_back(1002003002001LL);
      res.push_back(1004006004001LL);
      res.push_back(1020304030201LL);
      res.push_back(1022325232201LL);
      res.push_back(1024348434201LL);
      res.push_back(1210024200121LL);
      res.push_back(1212225222121LL);
      res.push_back(1214428244121LL);
      res.push_back(1232346432321LL);
      res.push_back(1234567654321LL);
      res.push_back(4000008000004LL);
      res.push_back(4004009004004LL);



    scanf("%lld",&Cases);
    while(Cases--){

        scanf("%lld %lld",&A,&B);

        long long cnt = 0;

        for(i=0; i<=39; i++){
            if(res[i]>=A && res[i]<=B) cnt++;
        }

        printf("Case #%lld: %lld\n",++Case,cnt);
    }

    return 0;
}




