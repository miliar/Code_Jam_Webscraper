#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("G:\\input.in","r",stdin);
    freopen("G:\\output.in","w",stdout);
    int tc,w,Smax,i,tot,naud;
    char ch;
    scanf("%d\n",&tc);
    w=1;
    while(w<=tc)
    {   tot=0;
    naud=0;
        scanf("\n%d ",&Smax);
        ch=getchar();
        tot=tot+(int)(ch-'0');
        for(i=1;i<=Smax;i++)
        {
            ch=getchar();

            if(i>0)
            {
                if(tot<i)
                    {naud=naud+i-tot;
                    tot=tot+(int)(ch-'0')+i-tot;
                    }
                else
                    {  tot=tot+(int)(ch-'0');
                        continue;
                    }
            }

        }
        printf("Case #%d: %d\n",w,naud);
        w++;
    }
return 0;
}
