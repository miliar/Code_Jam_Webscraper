#include <cstdio>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <cstring>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define s(a)		    scanf("%d",&a)
#define p(a)		    printf("%d",a)

#define nl              printf("\n");
#define sp              printf(" ");

/*inline void ifast(int &x)
{
    register int c = getchar_unlocked();
    x = 0;
    int neg = 0;
    for(; ((c<48 || c>57) && c != '-'); c = getchar_unlocked());
    if(c=='-') {
        neg = 1;
        c = getchar_unlocked();
    }
    for(; c>47 && c<58 ; c = getchar_unlocked()) {
        x = (x<<1) + (x<<3) + c - 48;
    }
    if(neg)
        x = -x;
}

void ofast(int n)
{
    if(n<0) {
        n=-n;
        putchar_unlocked('-');
    }
    int i=10;
    C output_buffer[10];
    do {
        output_buffer[--i]=(n%10)+'0';
        n/=10;
    } while(n);
    do {
        putchar_unlocked(output_buffer[i]);
    } while(++i<10);
}*/

int main()
{
	int t;
	s(t);
	int a,b,c;
	int cnt=0,cas=1;
	while(t--) {
		cnt=0;
		s(a);s(b);s(c);
		for(int i=0;i<a;i++) {
			for(int j=0;j<b;j++) {
				if((i&j) < c)cnt++;
			}
		}
		printf("Case #%d: %d\n",cas,cnt);
		cas++;
	}
	return 0;
}
