#include<iostream>
#include<cmath>
#include<cstdio>
#include<queue>
#include<stack>
#include<vector>
#include<climits>
using namespace std;
#define mx 100001
#define read(x) scanf("%d",&x)
#define MOD 1000000007
typedef pair<int,int> pr;
typedef long long int ull;


 
 int visited[1030]={0};
 int target,len;
 queue <pr> q;

/*
   +-+--

   pos=2
   len=5 
   1010
   0100
*/
   

int fn(int n,int pos)
{
   int newnum=0,i,j;

   for(i=pos,j=0;i>=0;i--,j++)
   {
    int bit=!!(n&(1<<(len-i-1)));
    //cout<<bit<<endl;
    if(bit==0)
      newnum|=1<<(len-j-1);
   }
   //cout<<".";
   for(i=pos+1;i<len;i++)
   {
     int bit=!!(n&(1<<(len-i-1)));
     //cout<<bit<<endl;
     if(bit==1)
      newnum|=1<<(len-i-1);
   }
   return newnum;
}

int bfs()
{

  pr ele;
  int i,j,k,num,newnum;

  while(!q.empty())
  {
    ele=q.front();
     q.pop();
     //cout<<ele.first<<endl;
     if(ele.first==target)
      return ele.second;
     
     num=ele.first;
     
     for(i=0;i<len;i++)
     {
         newnum=fn(num,i);
         //cout<<newnum<<endl;
         if(!visited[newnum])
         {
          q.push(make_pair(newnum,ele.second+1));
          visited[newnum]=1;
         }
     }  
  }
  return -1; 
}

 int main()
 {
   
   int t,i,j,k,tt;
   //  len=4;
   // cout<<fn(10,0);
   read(t);
   string s;
   

   
   for(tt=1;tt<=t;tt++)
   {
      cin>>s;
      len=s.length();

      target=(1<<len)-1;
      int num=0;
      
      for(i=0;i<len;i++)
      {
        if(s[i]=='+')
          num|=1<<(len-1-i);
      }

      //cout<<num<<" "<<target<<endl;

        memset(visited,0,sizeof(visited));
        visited[num]=1;
        q.push(make_pair(num,0));

        int ans=bfs();
        printf("Case #%d: %d\n",tt,ans);

        while(!q.empty())
          q.pop();
   }

 }