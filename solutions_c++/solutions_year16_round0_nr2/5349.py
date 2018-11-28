#include<bits/stdc++.h>
using namespace std;
long long int n,st=0,mul=1,ct=0,num=0,m;
map<int,int> mp;
int main()
{

    freopen("inp.in","r",stdin);
freopen("ans.out","w",stdout);
    int t,p=0;
    cin>>t;
    while(t--)
    {




string s;
st=0;
cin>>s;
int i,j,k,l;
l=s.size();
if(s[l-1]=='+')
  {
      for(i=l-1;i>=0;i--)
      {
          if(s[i]=='+')
          {
              k=i;

          }
          else
            break;
      }
  }
else
    k=l;
cout<<"Case #"<<++p<<": ";
    int f=0;
    if(k)
    while(1)
    {
        st++;
        for(i=0;i<k;i++)
        {
            if(s[i]=='+')
            {
                s[i]='-';
            }
            else
            {
                s[i]='+';
            }
        }
        j=k;
        for(i=j-1;i>=0;i--)
        {
            if(s[i]=='+')
            {
                k=i;
            }
            else
                break;
        }

        for(i=0;i<l;i++)
        {
            if(s[i]=='-')
            {
                f=1;
                break;
            }
        }
        if(!f)
            break;
        f=0;

    }
cout<<st<<endl;
    }
return 0;
}
