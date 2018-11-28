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

    int t,n,i,j,k,m,cnt,l;
    char s[1001],a[2002];

     scanf("%d",&t);
     m=1;
     while(t>=m)
     {
        cnt=0;
        scanf("%s",&s);

        l=strlen(s);
        j=1000;k=1000;
        for(i=0;i<l;++i)
        {
            if(i==0)
            {
                a[j]=s[0];
            }
            else
            {
                if(s[i]>=a[j])
                    a[--j]=s[i];
                else
                    a[++k]=s[i];
            }
        }

        printf("Case #%d: ",m);

        for(i=j;i<=k;++i)
        {
//            ans[l]=a[i];
            cout<<a[i];
        }
        cout<<endl;

        ++m;
     }

	return 0;

}
