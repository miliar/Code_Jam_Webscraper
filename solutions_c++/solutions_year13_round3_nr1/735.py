#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#define N 1000010

using namespace std;

long long int a[N],b[N],d[N];

bool fcheck(char c)
{
    if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u')
        return true;
    else
        return false;
}

int main(int argc, char *argv[])
{
    long long int t;
    long long int n;
    long long int i,j,k;
    long long int l;
    long long int z;
    string s;
    
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "w+t", stdout);
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>s>>n;
        l=s.length();
        a[0]=0;
        b[0]=0;
        d[0]=0;
        for(j=0;j<l;j++)
        {
            if(fcheck(s[j]))
            {
                d[j+1]=0;
            }
            else
                d[j+1]=d[j]+1;
        }
        for(j=1,z=0;j<=l;j++)
        {
            if(d[j]<n)
            {
                a[j]=a[j-1]+b[j-1];
                b[j]=b[j-1];
            }
            else
            {
                a[j]=a[j-1]+b[j-1]+j-z-n+1;
                b[j]=b[j-1]+j-z-n+1;
                z=j-n+1;
            }
            
        }
        cout<<"Case #"<<i<<": "<<a[l]<<endl;
     /*   for(j=1;j<=l;j++)
        {
            cout<<j<<" ";
        }
        cout<<endl;
        for(j=1;j<=l;j++)
        {
            cout<<d[j]<<" ";
        }
        cout<<endl;
        for(j=1;j<=l;j++)
        {
            cout<<a[j]<<" ";
        }
        cout<<endl;
        for(j=1;j<=l;j++)
        {
            cout<<b[j]<<" ";
        }
        cout<<endl;
        cout<<endl;*/
    }
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
