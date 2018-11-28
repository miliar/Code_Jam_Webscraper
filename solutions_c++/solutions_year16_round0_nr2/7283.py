#include<bits/stdc++.h>

using namespace std;

main()
{
    long int T,i,j,tst=1,n;
    char s[105],cp[105];
    FILE *in,*out;
    in=fopen("inputblarge.txt","r");
    out=fopen("outputblarge.txt","w");
    fscanf(in,"%ld",&T);
    while(T--)
    {
        fscanf(in,"%s",s);
        n=strlen(s);
        long int ans=0;
        strcpy(cp,s);
        for(i=0;i<n;i++)
        {
            if(cp[i]=='-')
            {
                ans++;
                for(j=i+1;j<n;j++)
                {
                    if(cp[j]=='+')
                        break;
                }

            }
            if(cp[i]=='+')
            {
                for(j=i+1;j<n;j++)
                {
                    if(cp[j]=='-')
                    {
                        ans++;
                        break;
                    }
                }
            }
            i=j-1;
        }
        fprintf(out,"Case #%ld: %ld\n",tst++,ans);
    }
    fclose(in);
    fclose(out);
    return 0;
}
