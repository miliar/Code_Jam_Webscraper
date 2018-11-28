#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
char s[30][100005],t[100005],tt[1005];
char fu[100005],fv[100005];
string st;
vector<int> zz[30];
map<string,int> pp;
int v1[100005],f1[100005],v2[255],f2[255];
int tot;
int nn[30];
main()
{
    freopen("C-small-attempt1 (1).in","r",stdin);
    freopen("C-small-attempt1 (1).out","w",stdout);
    int T,cas=0;scanf("%d",&T);
    while(T--)
    {
        int n;scanf("%d%*c",&n);
        gets(fu);
        gets(fv);
        int d=0;
        pp.clear();
        memset(zz,0,sizeof(zz));
        memset(v1,0,sizeof(v1));
        memset(f1,0,sizeof(f1));
        int len,num;
        tot=1;
        n-=2;
        for(int i=0;i<n;i++)
        {
            gets(s[i]);
            len=strlen(s[i]);num=0;
            for(int j=0;j<=len;j++)
            {
                if(s[i][j]==' '||s[i][j]=='\0')
                {
                    tt[num]='\0';
                    st=string(tt);
                    num=0;
                    if(!pp[st]) pp[st]=++tot;
                    zz[i].push_back(pp[st]);
                }
                else
                tt[num++]=s[i][j];
            }
        }

        len=strlen(fu);num=0;
        for(int i=0;i<=len;i++)
        {
            if(fu[i]==' '||fu[i]=='\0')
            {
                tt[num]='\0';
                st=string(tt);
                num=0;
                //cout<<st<<"++++"<<endl;
                if(!pp[st]) pp[st]=++tot;
                v1[pp[st]]|=1;
            }
            else
            tt[num++]=fu[i];
        }
        len=strlen(fv);num=0;
        for(int i=0;i<=len;i++)
        {
            if(fv[i]==' '||fv[i]=='\0')
            {
                tt[num]='\0';
                st=string(tt);
                num=0;
                //cout<<st<<"+++"<<endl;
                if(!pp[st]) pp[st]=++tot;
                v1[pp[st]]|=2;
                if(v1[pp[st]]==3&&!f1[pp[st]]) {d++;f1[pp[st]]=1;}
            }
            else
            tt[num++]=fv[i];
        }
//for(int q=0;q<20;q++)
//cout<<v1[q]<<" ";cout<<endl;
        int ret=1000000;
        for(int i=0;i<(1<<n);i++)
        {
            int ans=0;
            memset(v2,0,sizeof(v2));
            memset(f2,0,sizeof(f2));
            for(int j=0;j<n;j++)
            {
                for(int k=0;k<zz[j].size();k++)
                {

                    int u=zz[j][k];
                    //cout<<u<<" ";
                    if(i&(1<<j))
                    v2[u]|=2;
                    else
                    v2[u]|=1;
                    if((v1[u]|v2[u])==3)
                    {
                        if(!f1[u]&&!f2[u])
                        {
                            ans++;f2[u]=1;
                        }
                    }
                }
                //cout<<endl;
            }
            //for(int q=0;q<20;q++)
           // cout<<(v1[q]|v2[q])<<" ";
           // cout<<endl;
            ret=min(ret,ans+d);
        }

        printf("Case #%d: %d\n",++cas,ret);

    }
}
