#include<iostream>
#include<cmath>
#include<string.h>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<map>
using namespace std;


int n,t;

char s[21][10011];
vector<int>ch[21];
map<string,int>stoi;
int tail;

bool s1[1000001],s2[1000001];


int ans;


void gao(int x)
{
    int i,j;
    string ss;
    char *p,*q;
    char tmp[11];
    p=s[x];
    q=strchr(s[x],' ');
    
    while(q!=NULL)
    {
        *q=0;
        strcpy(tmp,p);
        
        ss=tmp;
        
        if(stoi.find(ss)==stoi.end())
        {
            stoi.insert(make_pair(ss,tail++));
            ch[x].push_back(tail-1);
        }
        else
        {
            ch[x].push_back(stoi[ss]);
        }
        
        
        *q=' ';
        p=q+1;
        q=strchr(p+1,' ');
    }
    
    strcpy(tmp,p);
    ss=tmp;
    
        if(stoi.find(ss)==stoi.end())
        {
            stoi.insert(make_pair(ss,tail++));
            ch[x].push_back(tail-1);
        }
        else
        {
            ch[x].push_back(stoi[ss]);
        }
    
    return ;
}


void calc(int fx)
{
    int i,j;
    int tmp=0;
    
    for(i=1;i<=tail-1;i++)
    {
        s1[i]=s2[i]=0;
    }
    
    for(i=1;i<=n;i++)
    {
        if((fx&(1<<(i-1)))==0)
        {
            for(j=0;j<ch[i].size();j++)
            {
                if(s2[ch[i][j]]==1)
                {
                    if(s1[ch[i][j]]==0)
                    {
                        s1[ch[i][j]]=1;
                        tmp++;
                    }
                    else
                    {
                        
                    }
                }
                else
                {
                    if(s1[ch[i][j]]==0)
                    {
                        s1[ch[i][j]]=1;
                    }
                    else
                    {
                        
                    }
                }
            }
        }
        else
        {
            for(j=0;j<ch[i].size();j++)
            {
                if(s1[ch[i][j]]==1)
                {
                    if(s2[ch[i][j]]==0)
                    {
                        s2[ch[i][j]]=1;
                        tmp++;
                    }
                    else
                    {
                        
                    }
                }
                else
                {
                    if(s2[ch[i][j]]==0)
                    {
                        s2[ch[i][j]]=1;
                    }
                    else
                    {
                        
                    }
                }
            }
        }
    }
    
    ans=min(ans,tmp);
    
    return ;
}


int main()
{
    int i,j,k,times;
    
    
    freopen("data.in","r",stdin);
    freopen("ans.out","w",stdout);
    
    cin>>t;
    
    
    
    for(times=1;times<=t;times++)
    {
        cin>>n;
        gets(s[0]);
        
        stoi.clear();
        tail=1;
    
        for(i=1;i<=n;i++)
        {
            gets(s[i]);
            ch[i].clear();
            gao(i);
            
        }
        ans=99999999;
        cout<<tail-1<<endl;
        for(i=2;i<=(1<<n)-1;i+=4)
        {
            calc(i);
        }
        cout<<"Case #"<<times<<": "<<ans<<endl;
        
    }
    
    
    
    
    
    return 0;
}
