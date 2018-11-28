#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
int main()
{
    freopen ("D-small-attempt1.in", "r", stdin);
    freopen ("output1.out","w",stdout);
    int t,p=0,x,r,c;
    scanf("%d",&t);
    while(p<t)
    {
        p++;
        int flag = 0;
        scanf("%d%d%d",&x,&r,&c);
        switch(x)
        {
            case 4: if(r*c>=12) flag = 1; break;
            case 1: flag = 1;break;
            case 2: if((r*c%2)==0) flag = 1; break;
            case 3: if(r*c>3 && (r==3||c==3)) flag = 1; break;
        }
        if(flag==1)
            printf("Case #%d: GABRIEL\n",p);
        else
            printf("Case #%d: RICHARD\n",p);
    }
    fclose (stdout);
    fclose (stdin);
    return 0;
}
