#include <iostream>
#include <stdio.h>
#include <queue>
using namespace std;
#define lli long long int
lli readint() {
    lli n = 0;
    char c = getchar_unlocked();
    while ( !( '0' <= c && c <= '9' ) ) {
        c = getchar_unlocked();
    }
    while ( '0' <= c && c <= '9' ) {
        n = (n<<3) + (n<<1) + c - '0';
        c = getchar_unlocked();
    }
    return n;
}
int main() {
	lli z=readint();
	for(lli t=1; t<=z; ++t)
	{
		lli s=readint();
		
		lli extra=0, people=0, temp;
		char c;
		
		for(lli i=0; i<=s; ++i)
		{
			scanf("%c", &c);
			temp=c-'0';
			if(temp==0) continue;
			
			if(people>=i)
				people+=temp;
			else
			{
				extra+=i-people;
				people+=temp+i-people;
			}
		}
		
		cout<<"Case #"<<t<<": "<<extra<<'\n';
	}
	return 0;
}