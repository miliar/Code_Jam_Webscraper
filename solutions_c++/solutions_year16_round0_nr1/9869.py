#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <utility>
#include <sstream>
#include <iomanip>
#include <cmath>
#include <bitset>
#include <map>
#include <stdlib.h>
#include <ctype.h>
#include <string>
#include <string.h>
#include <set>
#include <stack>
#include <deque>
#include <queue>
    using namespace std;

int main ()
{
    //freopen("input.txt","r",stdin);
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int TC;
    cin>>TC;
    long long num;
    for(int test=1;test<=TC;test++){
        scanf("%I64d",&num);
        //printf("%I64d\n",num);
        if(num == 0){
            printf("Case #%d: INSOMNIA\n",test);
            continue;
        }
        set <int> check;
        long long u = num;
        while((int)check.size() != 10){
            long long t = num;
            while(t){
                int a = t%10;
                //printf("%d\n",&a);
                check.insert(a);
                t /= 10;
            }
            if(check.size() == 10)
                break;
            num += u;
        }
        printf("Case #%d: %I64d\n",test,num);
    }
    return 0;
}
