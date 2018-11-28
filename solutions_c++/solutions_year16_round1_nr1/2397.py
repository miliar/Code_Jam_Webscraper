#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
char s[2000], p[1100];

char dfs(int a){
	if (a == 0)
	{
		p[0] = s[0];
		return s[0];
	}
	char x = dfs(a-1);
	if( x > s[a] ) {
		p[a] = s[a];
		return x;
	}
	for (int i = a; i > 0; --i)
	{
		p[i] = p[i-1];	
	}
	p[0] = s[a];
	return s[a];
}

int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
    	scanf("%s", s);
    	n = strlen(s);
    	dfs(n-1);

        printf("Case #%d: ", tt);
        for (int i = 0; i < n; ++i)
        {
        	printf("%c", p[i]);
        }
        puts("");
    }
    return 0;
}

