#include<bits/stdc++.h>
using namespace std;

int main()
{
    FILE *fr , *fw;
    fr=fopen("in.txt","a+");
    fw=fopen("out.txt","w+");
    int t,n;
    fscanf(fr,"%d",&t);
    for(int k=1;k<=t;k++)
    {
        char s[10005];
        int i,l;
        fscanf(fr,"%s",s);
        string ans="";
        ans+=s[0];
        for(i=1;s[i];i++)
        {
            l=ans.length();
            if(ans[0]<=s[i])
                ans=s[i]+ans;
            else
                ans+=s[i];
        }
        for(i=0;i<ans.length();i++)
            s[i]=ans[i];
        s[i]='\0';
        fprintf(fw,"Case #%d: %s\n",k,s);

    }
    fclose(fw);
    fclose(fr);
    return 0;
}
