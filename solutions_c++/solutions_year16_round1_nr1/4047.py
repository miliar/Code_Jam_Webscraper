#include <bits/stdc++.h>
using namespace std;

vector<string> s;
int main()
{
    int t=0;
    char ques[1005];
    FILE *f,*fp;
    f=fopen("A-large (1).in","r");
    fp=fopen("output.txt","w");
    int p=0;
    string temp;
    while(fscanf(f,"%s",ques)!=EOF)
    {
        temp="";
        for(int l=0;l<strlen(ques);l++)
        {
            temp+=ques[l];
        }
        s.push_back(temp);
    }
    for(int i=0;i<s[0].size();i++)
    {
        t*=10;
        t+=(s[0][i]-'0');
    }
    for(int i=1;i<=t;i++)
    {
        string p =s[i];
        string ans;
        ans+=p[0];
        for(int j=1;j<p.size();j++)
        {
            if(p[j]>=ans[0])
                ans=p[j]+ans;
            else
                ans+=p[j];
        }
        fprintf(fp,"Case #%d: ",i);
        for(int j=0;j<ans.size();j++)
            fprintf(fp,"%c",ans[j]);
        fprintf(fp,"\n");
    }
    return 0;
}
