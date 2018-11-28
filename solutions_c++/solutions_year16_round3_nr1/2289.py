#include<bits/stdc++.h>
using namespace std;
int p[27];
char a[27];
void sortn(int n)
{
    int sw;char s;
   for (int c = 0 ; c < ( n  ); c++)
  {
    for (int d = 0 ; d < n - c - 1; d++)
    {
      if (p[d] < p[d+1])
      {
        sw   = p[d];
        s=a[d];
        p[d]   = p[d+1];
        a[d]=a[d+1];
        p[d+1] = sw;
        a[d+1]=s;
      }
    }
  }
}
int sum(int n)
{
    int s=0;
    for(int i=0;i<n;i++)
        s+=p[i];
    return s;
}
int main()
{
    int t,c,i,n;
    cin>>t;
    for(c=1;c<=t;c++)
    {
        for(i=0;i<26;i++)
        {
            a[i]='A'+i;
        }
        memset(p,0,sizeof(p));
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>p[i];
        }
        cout<<"Case #"<<c<<":";
        while(1)
        {
            sortn(n);
            if(p[0]==0)
                break;
            if(p[0]==p[1]&&p[2]==p[0])
            {
                cout<<" "<<a[0];
                p[0]--;
            }
            else if(p[1]>(sum(n)-2)/2)
            {
                cout<<" "<<a[0]<<a[1];
                p[0]--;
                p[1]--;
            }
            else if(p[0]>1)
            {
                cout<<" "<<a[0]<<a[0];
                p[0]-=2;
            }
            else
            {
                cout<<" "<<a[0];
                p[0]--;
            }/*cout<<endl;
            for(i=0;i<n;i++)
            {
                cout<<" "<<p[i]<<" "<<a[i];
            }*/
        }
        cout<<endl;
    }
    return 0;
}
