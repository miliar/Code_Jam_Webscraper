#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#ifndef ONLINE_JUDGE
#define gc getchar
#define pc putchar
#else
#define gc getchar_unlocked
#define pc putchar_unlocked
#endif
//Shorthands
// typedefs
using namespace std;

//Generic fast output function
template <class T> inline void write(T x)
{
    int i = 20;
    char buf[21];
    // buf[10] = 0;
    buf[20] = '\n';

    do
    {
        buf[--i] = x % 10 + '0';
        x/= 10;
    }while(x);
    do
    {
        putchar(buf[i]);
    } while (buf[i++] != '\n');
}
//Generic fast inputs
template <class T>
inline T read()
{
    T n=0;
    bool sign=0;
    char p=gc();
    if(p=='-')
        sign=1;
    while((p<'0'||p>'9')&&p!=EOF&&p!='-')
        p=gc();
    if(p=='-')
        sign=1,p=gc();
    while(p>='0'&&p<='9') {
        n = (n<< 3) + (n<< 1) + (p - '0');
        p=gc();
    }
    if(sign)
        return -n;
    return n;
}

int main()
{
	freopen("F:\\google codejam\\code jam 2015\\input.in","r",stdin);
	freopen("F:\\google codejam\\code jam 2015\\output.in","w",stdout);
	int t,i,j,k,l,e,p,w;
	t=read<int>();
	char s[10000];
	w=1;
	while(w<=t)
	{
		scanf("%d",&l);
		scanf("%s",s);
		i=0;
		j=((int)s[i]-48);
		i=1;
		e=0;
		while(i<=l)
		{
			k=(int)(s[i]-48);
			p=k;
			//printf("%d %d\n",i,j);
			if(i>j&&p>0)
			{
				//printf("holla\n");
				e+=(i-j);
				//printf("e=%d\n",e);
				j+=e+1;
				p-=1;	
			}
			if(p>0)
			j+=p;			
			i++;
		}
		printf("Case #%d: %d\n",w,e);
		w++;
	}
	return 0;
}
