#include <iostream>
#include <sstream>
#include <utility>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <functional>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <set>
#include <stdio.h>
#include <string.h>
using namespace std;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("salida3.out","w",stdout);
    int t,A,B,con;
    int vec[5]={1,4,9,121,484};
    cin>>t;
    for(int a=0;a<t;a++)
    {
        con=0;
        cin>>A>>B;
        for(int b=0;b<5;b++)
        {if(vec[b]>=A && vec[b]<=B)con++;}
        printf("Case #%d: %d\n",a+1,con);
    }
}
