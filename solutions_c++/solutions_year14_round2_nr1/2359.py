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
//	char ch;
//	ch=getchar();
	int n;
	char a[105],b[105];
	int cas=1,cnt=0,flag=0;
	while(t--) {
		cnt=0;
		flag=0;
		s(n);
		scanf("%s%s",a,b);
		int i=0,j=0;
		int cnt1=0,cnt2=0;
		while(a[i] && b[j]) {
			if(a[i]==b[j]) {
				cnt1++,cnt2++;
				while(a[i+1] && a[i]==a[i+1])cnt1++,i++;
				while(b[j+1] && b[j]==b[j+1])cnt2++,j++;
				cnt+=abs(cnt1-cnt2);
				cnt1=0,cnt2=0;
			} else {
				flag=1;
				break;
			}
			i++,j++;
		}
		if(a[i] || b[j])flag=1;
		if(flag) {
			printf("Case #%d: Fegla Won\n",cas);
		} else {
			printf("Case #%d: %d\n",cas,cnt);
		}
		cas++;
	}
	return 0;
}
