#include<stdio.h>
#include <iostream>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<set>
#include<string>
int m,n,mark[10],now,t,ans,cc;
using namespace std;
string ss[10];
set<string> s;
void create_trie()
{
        s.clear();
}
void insert_trie(string ss) 
{
        s.insert("");
        for(int i=1;i<=ss.length();i++)
        {
                s.insert(ss.substr(0,i));
        }
}
int count_trie()
{
        return s.size();
}
void re(int h)
{
        if(h!=m)
        {
                for(int i=0;i<n;i++)
                {
                        mark[h]=i;
                        re(h+1);
                }
        }
        else
        {
                now=0;
                for(int i=0;i<n;i++)
                {
                        create_trie();
                        for(int j=0;j<m;j++)
                        {
                                if(mark[j]==i)
                                {
                                        insert_trie(ss[j]);
                                        //cout << ss[j] << "\n";
                                }
                        }
                        //printf("%d\n",count_trie());
                        //system("pause");
                        now+=count_trie();
                }
                if(now>ans)
                {
                        ans=now;
                        cc=1;
                }
                else if(now==ans)
                {
                        cc++;
                }
                        //printf("%d\n",now);
        }
}
int main()
{
     freopen("d.in","r",stdin);
     freopen("d.out","w",stdout);
     scanf("%d",&t);
     for(int rr=1;rr<=t;rr++)
     {
                ans=0;
        scanf("%d %d",&m,&n);
        for(int i=0;i<m;i++)
        {
                cin >> ss[i];
                //cout << ss[i] << "\n";
        }
        re(0);  
     
          printf("Case #%d: %d %d\n",rr,ans,cc);
     }
     //system("pause");
}
