#include<iostream>
#include<cstdio>
#include<string>
#include<cstring>
#define MAX 110
char str[MAX];
using namespace std;
bool has(int l)
{
  for(int i=0;i<l;i++)
  {
    if(str[i]=='-')
      return false;
  }
  return true;
}
void flip(int l)
{
  bool present=false;
  int index,i;
  for(i=l-1;i>=0;i--)
  {
    if(str[i]=='-')
    {
      index=i;
      break;
    }
  }
  for(i=0;i<=index;i++)
  {
    if(str[i]=='-')
      str[i]='+';
    else
      str[i]='-';
  }
}
int main()
{
  int T,i,j,k,l,m,n,ans;
  ios::sync_with_stdio(false);
  // freopen("in.txt","r",stdin);
  // freopen("out.txt","w",stdout);
  cin>>T;
  for(m=0;m<T;m++)
  {
    ans=0;
    cin>>str;
    l=strlen(str);
    bool done;
    done=has(l);
    if(done)
      cout<<"Case #"<<(m+1)<<": "<<ans<<endl;
    else
    {
      while(1)
      {
        ans++;
        flip(l);
        done=has(l);
        if(done)
          break;
      }
      cout<<"Case #"<<(m+1)<<": "<<ans<<endl;
    }
  }
}
