#include<stdio.h>

char inp[103];

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("txt.txt","w",stdout);
    int t,ti,cnt,state,i;
    scanf ("%d",&t);
    for (ti=0;ti<t;++ti)
    {
        cnt=0;
        scanf ("%s",inp);
        if (inp[0] == '-')state=1;
        else state=0;
        for (i=0;inp[i];++i)
        {
            if ((state==1 && inp[i]=='+')||(state==0 && inp[i]=='-'))
            {
                state = (state+1)%2;
                cnt++;
            }
        }
        if (state==1)cnt++;
        printf ("Case #%d: %d\n",ti+1,cnt);
    }
    return 0;
}
