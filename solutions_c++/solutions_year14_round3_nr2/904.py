#include <algorithm>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <cstdlib>
#include <string>
#include <vector>
#include <cstdio>
#include <cmath>
//#include <ctime>
#include <map>

using namespace std;

char s1[101][101];
char s[101][101];
int l[101];
int a[101];
int b[101];
int p[101];
char c[101][2];
char num[101][101];
int v[101];
int cou,n,t;


void swap(int t1,int t2)
{
int tmp;
tmp=a[t1];
a[t1]=a[t2];
a[t2]=tmp;
}

void allPermutation(int t)
{
for(int k=t;k<=n;k++)
{
  swap(k,t);
  if(t>=n)
  {
      string str="";
     //   for (int i=1;i<=n;i++) cout<<a[i]<<":";
     //   cout<<endl;
        int flag=1;
        for (int i=1;i<=n;i++)
        str=str+s[a[i]];
        int p;
        p=str.length();
       // cout<<p<<endl;
        //cout<<str<<endl;
        int i=0;
        while (i<p)
        {
            while (str[i]==str[i+1]) i++;
            if (i<p && str[i]!=str[i+1])
            if (flag==0) break;
            if (str[i]!=str[i+1])
            {
                for (int j=i+2;j<=p-1;j++)
                if (i!=j)
                if (str[j]==str[i])
                {
                    flag=0;
                    break;
                }
            }
            i++;
        }
        if (flag==1) cou++;

  }
  else
   allPermutation(t+1);
  swap(k,t);
}
}
int main()
{

    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
	ios :: sync_with_stdio(false);
  //  int t,n;
    cou=0;
    scanf("%d",&t);
    for (int k=1;k<=t;k++)
    {
        cou=0;
        cout<<"Case #"<<k<<": ";
        scanf("%d",&n);
        for (int i=1;i<=n;i++)
        {
            scanf("%s",s[i]);
            int l=strlen(s[i]);
            //cout<<s[i]<<endl;
            int newsize = unique(s[i], s[i]+strlen(s[i]))-s[i];
            s[i][newsize]=0;
          //  cout<<s[i]<<endl;
        //    cout<<endl;
           // cout<<newsize<<endl;
          //  c[i][1]=s[i][0];
           // c[i][2]=s[l-1];
            //cout<<c[i][1]<<c[i][2]<<
//            (for int i=0;i<=l-1;i++ )
        }
        for(int i=1;i<=n;i++) a[i]=i;
        allPermutation(1);
        cout<<cou<<endl;
    }

    return 0;
}
