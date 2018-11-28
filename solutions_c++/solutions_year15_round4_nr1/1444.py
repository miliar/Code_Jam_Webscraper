#include<iostream>
#include<stdio.h>
#include<assert.h>
using namespace std;




int R,C;
bool Check(string s[1005])
{
    for(int i=0;i<R;i++)
        for(int j=0;j<C;j++)
        {
            if(s[i][j]!='.')
            {
                int flag=0;
                for(int k=0;k<C;k++)
                    if(k!=j && s[i][k]!='.') {flag++;break;}
                for(int k=0;k<R;k++)
                    if(k!=i && s[k][j]!='.') {flag++;break;}
                if(flag==0) return true;
            }
        }
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;
    string s[1005];
    cin>>T;
    for(int cas=0;cas<T;cas++)
    {
        
        cin>>R>>C;
        for(int i=0;i<R;i++)
            cin>>s[i];
        int ans=0;

        int i,j;
        for(i=0;i<R;i++)
            for(j=0;j<C;j++)
            {
                if(s[i][j]!='.')
                {
                    int flag[4]={0,0,0,0};
                    for(int k=0;k<j;k++)
                        if(s[i][k]!='.') {flag[0]=1;break;}
                    for(int k=j+1;k<C;k++)
                        if(s[i][k]!='.') {flag[1]=1;break;}
                    for(int k=0;k<i;k++)
                        if(s[k][j]!='.') {flag[2]=1;break;}
                    for(int k=i+1;k<R;k++)
                        if(s[k][j]!='.') {flag[3]=1;break;}
                    if(flag[0]==0 && s[i][j]=='<') ans++;
                    else if(flag[1]==0 && s[i][j]=='>') ans++;
                    else if(flag[2]==0 && s[i][j]=='^') ans++;
                    else if(flag[3]==0 && s[i][j]=='v') ans++;
                }
            }
            
        if(Check(s)==true)
            printf("Case #%d: IMPOSSIBLE\n",cas+1);
        else
            printf("Case #%d: %d\n",cas+1,ans);
    }
    return 0;
}
