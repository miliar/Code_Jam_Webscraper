#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
using namespace std;
#define MAX 26

int cnt;

struct Node{

   int isstr;
   int num;
   Node *next[MAX];
   Node(){
      memset(next,0,sizeof(next));
      isstr=0;
      num=0;
   }
};

Node *root;

void Insert(char *s)
{
    Node *p=root ,*q;
    while(*s)
    {
        if(p->next[*s-'A']==NULL)
        {
            q=new Node;
            p ->next[*s-'A'] = q;
            cnt++;
        }
         p->next[*s-'A']->num++;
         p=p->next[*s-'A'];
         s++;
     }
     p->isstr=1;
}

void myfree(Node *p){
    for(int i = 0; i < MAX; i++){
        if(p->next[i] != NULL){
            myfree(p->next[i]);
        }
    }
    delete p;
    return ;
}

string str[1111];
char st[11111];
int d[1111],ans,sum;

void dfs(int k,int m,int n){
    for(int i=1;i<=m;i++)
    {
        d[k]=i;
        if(k==n){
            int tot=0;
            for(int j=1;j<=m;j++){
                root=new Node;
                cnt=1;

                bool flag=false;
                for(int o=1;o<=n;o++)
                if(d[o]==j)
                {
                    strcpy(st,str[o].c_str());
                    Insert( st );
                    flag=true;
                }
                if(flag)
                    tot+=cnt;

                myfree(root);
            }

            if(tot>ans){
                ans=tot;
                sum=1;
            }else if(tot==ans)
                sum++;

        }
        else
            dfs(k+1,m,n);
        d[k]=0;
    }
}


int main()
{
    //freopen("d.in","r",stdin);
    //freopen("d.out","w",stdout);
    int cas,cass=0,n,m;
    cin>>cas;
    while(cas--){
        cass++;
        cin>>m>>n;

        for(int i=1;i<=m;i++)
        {
            cin>>st;
            str[i]=st;
        }
        ans=-1000,sum=0;
        dfs(1,n,m);


        cout<<"Case #"<<cass<<": "<<ans<<' '<<sum<<endl;
    }


    return 0;
}
