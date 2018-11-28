#include<iostream>
#include<fstream>
#include<set>
#include<algorithm>
#include<vector>
#include<cstring>
#include<map>
#include<iomanip>
using namespace std;

int T,R,C;
vector<string>v;
int a[101][101];
int b[101][101];
int c[101][101];
int d[101][101];


bool visited[101][101];
void fun(int i,int j,int dir)
{
    if(visited[i][j])
        return;
    visited[i][j]=true;
    if(v[i][j]=='^')
        dir=0;
    if(v[i][j]=='>')
        dir=1;
    if(v[i][j]=='v')
        dir=2;
    if(v[i][j]=='<')
        dir=3;
   if(dir==0)
   {
       if(i-1<0)
       {
           a[i][j]=1;
           return;
       }
    fun(i-1,j,dir);
   }
   else if(dir==1)
   {
    if(j+1>=C)
    {
        b[i][j]=1;
        return;
    }
    fun(i,j+1,dir);
   }
   else if(dir==2)
   {
       if(i+1>=R)
       {
           c[i][j]=1;
        return;
       }
       fun(i+1,j,dir);

   }
   else if(dir==3)
   {
       if(j-1<0)
       {
           d[i][j]=1;
        return;
       }
       fun(i,j-1,dir);
   }

}
int main(){
    ifstream  fin("/Users/anupsing/Desktop/GCJ/input.txt");
    ofstream  fout("/Users/anupsing/Desktop/GCJ/output.txt");
    fin>>T;
    int cases=1;
    while(T--) {
        fin>>R>>C;
        v.clear();
        for(int i=0;i<R;i++)
        {
            string str;
            fin>>str;
            v.push_back(str);

        }

        memset(a,0,sizeof(a));
        memset(b,0,sizeof(b));
        memset(c,0,sizeof(c));
        memset(d,0,sizeof(d));

        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
        {
            memset(visited,false,sizeof(visited));
            if(v[i][j]=='^')
                fun(i,j,0);
            if(v[i][j]=='>')
                fun(i,j,1);
            if(v[i][j]=='v')
                fun(i,j,2);
            if(v[i][j]=='<')
                fun(i,j,3);
        }
        int ans=0;
        for(int i=0;i<R;i++)
            for(int j=0;j<C;j++)
            {
                int temp=0;
                temp=a[i][j]+b[i][j]+c[i][j]+d[i][j];
                if(v[i][j]!='.')
                {
                    if(temp)
                        temp=1;
                }
                ans+=temp;
            }
        bool flag=true;
        bool zero=true;
        for(int i=0;i<R;i++)
        {
            int ct=0;
            for(int j=0;j<C;j++)
            if(v[i][j]!='.')
                ct++;
            if(ct>1)
                flag=false;
            if(ct)
                zero=false;
        }

        for(int i=0;i<C;i++)
        {
            int ct=0;
            for(int j=0;j<R;j++)
            if(v[j][i]!='.')
                ct++;
            if(ct>1)
                flag=false;
            if(ct)
                zero=false;
        }

        if(flag&&(!zero))
            fout<<"Case #"<<cases++<<": "<<"IMPOSSIBLE"<<endl;
        else
        fout<<"Case #"<<cases++<<": "<<ans<<endl;
    }

    return 0;
}
