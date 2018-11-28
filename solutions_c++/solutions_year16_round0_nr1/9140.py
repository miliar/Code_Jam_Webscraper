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
    freopen("D:/out.txt","w",stdout);

    int t,n,i,j,k,m,cnt,ans,l;
    bool a[10]={true},flag;

     scanf("%d",&t);
     m=1;
     while(t>=m)
     {
        fill(a,a+10,true);
        scanf("%d",&n);
        l=n;

        if(n>0)
        {
            flag=false;
            while(1)
            {
                j=n;
                while(j)
                {
                    k=j%10;
                    j/=10;
                    a[k]=false;

                }
                flag=true;
                for(i=0;i<10;++i)
                {
                    if(a[i])
                    {
                        flag=false;
                        break;
                    }
                }

                if(flag)
                {
                    printf("Case #%d: %d\n",m,n);
                    break;
                }
                n+=l;
            }
        }
        else
           printf("Case #%d: INSOMNIA\n",m);

        ++m;

     }

	return 0;

}
