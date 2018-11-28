#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char s[200],p[200];
int main(void){
    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){
        int ans = 0;
    	scanf("%s", s);

    	int n = strlen(s);
    	while(1){
    		int i;
    		for (i = 0; i < n && s[i]=='+'; ++i);
    		if (i==n)
    		{
    			break;
    		}

    		int st,ed;
    		for (st = 0; st <n && s[st]=='-'; ++st) s[st]='+';
    		for (ed = n-1; ed >=0 && s[ed]=='+'; --ed) p[ed]='+';

    		if (st < ed){
	    		if (st == 0){ 
	    			ans++;
	    			for (st = 0; st <n && s[st]=='+'; ++st) s[st]='-';
	    		}
    			ans++;
    			for(int j=0;j<=ed;j++)
    				p[j] = (s[ed-j]=='+')?'-':'+';
    		} else {
    			ans++;
    		}
    		for (i = 0; i < n ; ++i) s[i]=p[i] ;

    	}

        printf("Case #%d: %d\n", tt, ans);
    }
    return 0;
}

