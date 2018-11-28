#include<iostream>
#include<math.h>
using namespace std;
int main()
{ int n,l,r,b[1001]={0},a[1001]={0};
  int i;
  for(i=1;i<=1000;i++)
  { int k=0,m=i;
    while(m>0)
    { k*=10;
      k+=m%10;
      m/=10;
    }
    if(k==i)
    { b[i]=1;
      float p=floor(sqrt(i));
      if((p-sqrt(i))==0)
      { if(b[int(p)]==1)
        { a[i]=1;
        }
      }
    }  
  }   
  freopen("C-small-attempt0.in","r",stdin);
  i=1;
  cin>>n;
  while(n)
  { cin>>l>>r;
    int cnt=0;
    while(l<=r)
    { if(a[l]==1)
      { cnt++;
      }
      l+=1;
    }
    cout<<"Case #"<<i<<": "<<cnt<<'\n';
    i+=1;
    n--;
  }
  return 0;
}  
