#include <bits/stdc++.h>

#define MOD 1000000009

using namespace std;

int readInt () {
	bool minus = false;
	int result = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch-'0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result*10 + (ch - '0');
	}
	if (minus)
		return -result;
	else
		return result;
}

int main()
{
    freopen("D:/codes/16/codejam/in.txt","r",stdin);
    freopen("D:/codes/16/codejam/out.txt","w",stdout);

    int t,n,i,j,k,m,cnt,ans,l;
    char s[101];

     scanf("%d",&t);
     m=1;
     while(t>=m)
     {
        cnt=0;
        scanf("%s",&s);
        l=strlen(s);

        bool f=false,g;
        i=0;
        if(s[0]=='-')
            ++cnt;
        while(i<l)
        {
            g=true;
            if(s[i]=='+')
                f=true;

            if(f)
            {
                while(s[i]=='-')
                {
                    ++i;
                    g=false;
                }
            }
            if(g)
                ++i;
            else
                cnt+=2;
        }

        printf("Case #%d: %d\n",m,cnt);

        ++m;

     }

	return 0;

}
