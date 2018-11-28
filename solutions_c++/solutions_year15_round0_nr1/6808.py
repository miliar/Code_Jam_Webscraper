#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<map>
#define  gc getchar()
#define pc(c) putchar(c)
using namespace std;
using namespace std;
template<class po>inline po s(po &x) {
    register char c = gc;
     x = 0;
    bool neg = false;
    for (; ((c < 48 || c > 57) && c != '-'); c = gc);
    if (c == '-') {
    	neg = true;
    	c = gc;}
    for (; c > 47 && c < 58; c = gc) {
    	x = (x << 1) + (x << 3) + c - 48;
    }
    if (neg) {
    	x = -x;
    }
    return x;
}
template<class po>inline void w(po n) {
    if(n<0){n=-n;pc('-');}
	po N = n, rev, count = 0;
    rev = N;
    if (! N) {
    	pc('0');
    	pc('\n');
    	return;
    }
    while (! (rev % 10)) {
    	count++;
    	rev /= 10;
    }
    rev = 0;
    while (N) {
    	rev = (rev << 3) + (rev << 1) + N % 10;
    	N /= 10;
    }
    while (rev) {
    	pc(rev % 10 + '0');
    	rev /= 10;
    }
    while (count--) {
    	pc('0');
    }
    pc('\n');
}

int main()
{freopen("in","r",stdin);
freopen("out", "w", stdout);
    int t,sh,sum,ans;
s(t);
for(int t1=1;t1<=t;t1++)
{sum=ans=0;
    printf("Case #%d: ",t1);
    s(sh);
    for(int i=0;i<=sh;i++)
    {
      char c=gc;
      if(c>='0'&&c<='9')
      {
          if(sum<i)
          {
              ans+=i-sum;
              sum+=i-sum;
          }
          sum+=c-'0';
      }
    }
    w(ans);
}
    return 0;
}
