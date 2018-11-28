#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;


int main()
{   freopen("D-small-attempt0.in", "r", stdin);
    freopen("result1.txt", "w", stdout);
    int i,T,X,R,C;
    char ans[50];
    scanf("%d",&T);
    for(i=1;i<T+1;i++)
    {
    scanf("%d %d %d",&X,&R,&C);
    if(R>C)
        swap(R,C);
    if(X==1)
        strcpy(ans,"GABRIEL");
    else if(X==2)
    {
        if((R*C)%2==0)
            strcpy(ans,"GABRIEL");
        else
            strcpy(ans,"RICHARD");
    }
    else if(X==3)
    {
        if((R*C)>3 && (R*C)%3 ==0)
            strcpy(ans,"GABRIEL");
        else
            strcpy(ans,"RICHARD");
    }
    else if(X==4)
    {
        if((R*C)>8 && (R*C)%4==0)
            strcpy(ans,"GABRIEL");
        else
            strcpy(ans,"RICHARD");
    }
    printf("Case #%d: %s\n",i,ans);
    }
}
