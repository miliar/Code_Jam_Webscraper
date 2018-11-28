#include<bits/stdc++.h>
using namespace std;
bool check(char s[])
{
    int f=true;
    for(int i=0;s[i];i++)
        if(s[i]=='-')
            f=false;
    return f;
}


int main()
{
    FILE *fr , *fw;
    fr=fopen("in.txt","a+");
    fw=fopen("out.txt","w+");
    int t,n;
    fscanf(fr,"%d",&t);
    for(int k=1;k<=t;k++)
    {
        char s[105];
        fscanf(fr,"%s",s);
        int ans=0;
        while(!check(s))
        {
            int i=0,j=0;
            ans++;
            char a[105];
            for(i=0;s[i];i++)
                a[i]=s[i];
            a[i]='\0';
            i=1;
            while(a[i]==a[i-1])i++;
            if(i)i--;
            //cout<<i<<"\t"<<j<<"\n";
            for(j=0;j<=i;j++)
                if(a[j]=='+')
                    s[i-j]='-';
                else
                    s[i-j]='+';
            //cout<<s<<"\n";
        }
        fprintf(fw,"Case #%d: %d\n",k,ans);

    }
    fclose(fw);
    fclose(fr);
    return 0;
}
