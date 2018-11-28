#include <bits/stdc++.h>
#define gc getchar_unlocked
#define pc putchar

using namespace std;

inline int sn()
{
    char r;
	bool start=false,neg=false;
	int ret=0;
	while(true){
		r=getchar();
		if((r-'0'<0 || r-'0'>9) && r!='-' && !start){
			continue;
		}
		if((r-'0'<0 || r-'0'>9) && r!='-' && start){
			break;
		}
		if(start)ret*=10;
		start=true;
		if(r=='-')neg=true;
		else ret+=r-'0';
	}
	if(!neg)
		return ret;
	else
		return -ret;
}

inline void wi(int n)
{
    int N = n, rev;
    int count = 0;
    rev = N;
    if (N == 0) { pc('0');  return ;}
    while ((rev % 10) == 0) { count++; rev /= 10;}
    rev = 0;
    while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}
    while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
    while (count--) pc('0');
}

int main(){
    int t = sn(), n, k = 1, s, f;//1023
    while(t--){
        n = sn();
        if(!n){
            printf("Case #%d: INSOMNIA\n", k++);
            continue;
        }
        s = n;
        f = 0;
        while(true){
            int c = s;
            while(c){
                f |= 1 << (c % 10);
                c /= 10;
            }
            if(f == 1023){printf("Case #%d: %d\n", k++, s);break;}
            s += n;
        }
    }
    return 0;
}
















