#include<bits/stdc++.h>
#define MAX 10005
using namespace std;
vector<string> sa,sb;
void funa(string a,int n,int k)
{
    if(k==n)
    {
        sa.push_back(a);
        //cout<<a<<"\n";
        return;
    }
    else
    {
        if(a[k]=='?')
        {
            for(int i=0;i<=9;i++)
            {
                a[k]='0'+i;
                funa(a,n,k+1);
            }
        }
        else
            funa(a,n,k+1);
    }
}
void funb(string a,int n,int k)
{
    if(k==n)
    {
        sb.push_back(a);
        //cout<<a<<"\n";
        return;
    }
    else
    {
        if(a[k]=='?')
        {
            for(int i=0;i<=9;i++)
            {
                a[k]='0'+i;
                funb(a,n,k+1);
            }
        }
        else
            funb(a,n,k+1);
    }
}

int change(string s)
{
    int i,l=s.length(),v=0;
    for(i=0;i<l;i++)
        v=v*10+(s[i]-'0');
    return v;
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
        char a[20];
        char b[20];
        fscanf(fr,"%s",a);
        fscanf(fr,"%s",b);
        int i,j;
        sa.clear();
        sb.clear();

        funa(a,strlen(a),0);
        funb(b,strlen(b),0);
        int d=INT_MAX,ii,ij;
        sort(sa.begin(),sa.end());
        sort(sb.begin(),sb.end());

        for(i=0;i<sa.size();i++)
        {
            int x=change(sa[i]);
            for(j=0;j<sb.size();j++)
            {
                int y=change(sb[j]);
                if(d>abs(x-y))
                    ii=i,ij=j,d=abs(x-y);
            }
        }
        for(i=0;i<sa[ii].length();i++)
            a[i]=sa[ii][i];
        a[i]='\0';
        for(i=0;i<sb[ij].length();i++)
            b[i]=sb[ij][i];
        b[i]='\0';

        fprintf(fw,"Case #%d: %s %s\n",k,a,b);

    }
    fclose(fw);
    fclose(fr);
    return 0;
}
