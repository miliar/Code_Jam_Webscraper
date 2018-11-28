typedef long long ll;
#include <iostream>
#include <stdio.h>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <string.h>
#include <map>
#include <queue>
#include <stack>
#include <sstream>
#include <fstream>
#include <stdlib.h>
#include <utility>

using namespace std;
int main()
{
    ll t,k,c,s,i,w=1;
    scanf("%lld",&t);
    while(t--)
    {
        scanf("%lld %lld %lld",&k,&c,&s);
        printf("Case #%lld: ",w++);
        for(i=1;i<=k;i++)
        printf("%lld ",i);
        printf("\n");
    }
	return 0;
}