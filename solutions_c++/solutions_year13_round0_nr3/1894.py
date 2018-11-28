// Author :Krishna Kumar Tiwari


#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>

int main()
{
long long int w,cnt,u,p,q,array[39]={ 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004 };

int test_cases,tc=1;

scanf("%d",&test_cases);

while (test_cases--){
cnt=0;
scanf("%lld %lld", &p,&q);
for (w=0;w<39;w++){

if (array[w]==p || array[w]==q || (array[w]>p && array[w]<q))
cnt++;

}

printf("Case #%d: %lld\n",tc,cnt);
tc++;
}
return 0;
}
