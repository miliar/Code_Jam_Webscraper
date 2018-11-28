#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cmath>
#define N 10000000
#define M 10
#define O 3163
#define P 14

using namespace std;

vector <long long int> b;
int a[N];//0 :none 1:p  2:p&square 3:ans
//int c[M]={0,1,2,3,4,5,6,7,8,9}
int d[M];
int c[M]={1,10,100,1000,10000};
void f(int x,int y,int z)
{
    int i;
    int p,q;
    int ans,ans10,ans2;
    if(z==x)
    {
        
        p=c[x];
        q=c[x+1]; 
        for(i=0,ans=0,ans2=0;i<z;i++)
        {
            ans=ans*10+d[i];
            ans2=ans2*10+d[z-i-1];
        }
        if(y==1)
        {
            
            ans10=ans*q;
            for(i=0;i<M;i++)
            {
                a[ans10+i*p+ans2]=1;
            }
        }
        else
        {
            a[ans*p+ans2]=1;
        }
        return;
    }
    for(i=0;i<M;i++)
    {
        if(z==0&&i==0)
            continue;
        d[z]=i;
        f(x,y,z+1);
    }
}

int main(int argc, char *argv[])
{
    freopen("C-large-1.in", "rt", stdin);
    freopen("C-large-1.out", "w+t", stdout);
    
    long long int i,j,k;
    int t;
    long long int A,B;
    int x,y,z;
    stringstream ss;
    string s;
    int l,l2;
    long long int tmp;
    memset(a,0,sizeof(a));
   /* for(i=0;i<P;i++)
    {
        b[i].clear();
    }*/
    for(i=1;i<=9;i++)
    {
        a[i]=1;
    }
    for(i=2;i<=7;i++)
    {
        x=i/2;
        y=i%2;
        f(x,y,0);
    }
/*    for(i=0,k=0;i<N;i++)
    {
        if(a[i])
        {
            k++;
            cout<<i<<" ";
        }
        if(k==10)
        {
            cout<<endl;
            k=0;
        }
    }*/
    for(i=1;i<O;i++)
    {
        k=i*i;
        if(a[k])
        {
            if(a[i])
            {
                a[k]=3;
                b.push_back(k);
            }
            else
                a[k]=2;
        }
    }
    for(i=O;i<N;i++)
    {
        if(a[i])
        {
            tmp=i*i;
            ss.clear();
            ss<<tmp;
            ss>>s;
            l=s.length();
            l2=l/2;
            l--;
            for(j=0;j<l2;j++)
            {
                if(s[j]!=s[l-j])
                    break;
            }
            if(j==l2)
                b.push_back(tmp);
        }
    }
    l=b.size();
  //  l2=b[1].size();
   /* cout<<l<<" "<<l2<<endl;
    for(i=0;i<l;i++)
    {
        cout<<b[0][i]<<" ";
    }
    cout<<endl<<endl;
    for(i=0;i<l2;i++)
    {
        cout<<b[1][i]<<" ";
    }
    */
  /*  for(i=0;i<l;i++)
    {
        cout<<b[i]<<endl;
    }*/
    cin>>t;
    for(j=1;j<=t;j++)
    {
        cin>>A>>B;
        for(i=0,k=-1;i<l;i++)
        {
            if(b[i]>=A)
            {
                k=i;
                break;
            }
        }
        if(k!=-1)
        {
            for(i=k;i<l;i++)
            {
                if(b[i]>B)
                    break;
            }
            k=i-k;
            //cout<<k<<" "<<i<<endl;
        }
        else 
            k=0;
        cout<<"Case #"<<j<<": "<<k<<endl;
    }
    //system("PAUSE");
    return EXIT_SUCCESS;
}
