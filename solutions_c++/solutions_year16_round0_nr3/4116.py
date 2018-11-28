#include <iostream>
#include <cmath>
using namespace std;
long long int a[11][20];

int ans[11];
/* Generate Power */
void pw()
{
    int i,j;
    for(i=2;i<=10;i++)
    {
        for(j=0;j<20;j++)
        {
            if(j==0)
                a[i][j]=1;
            else
                a[i][j]=a[i][j-1]*i;
        }
    }
}

bool prime(long long int n,int x)
{
    for(int i=2;i<1000 && i<n;i++)
    {
        if(n%i==0)
        {
            ans[x]=i;
            return true;
        }
    }
    return false;
}

string bin(int n)
{
    string s="";
    while(n>0)
    {
        s+=n%2+'0';
        n/=2;
    }
    string s1="";
    for(int i=s.size()-1;i>=0;i--)
    {
        s1+=s[i];
    }
    return s1;
}

bool check(string n)
{
    
    for(int i=2;i<=10;i++)
    {
        long long int y=0;
        int z=0;
        for(int j=n.size()-1;j>=0;j--)
        {
            if(n[j]=='1')
                y+=a[i][z];
            z++;
        }
        if(!prime(y,i))
            return false;
        
    }
    cout<<n<<" ";
    return true;
}

int main()
{
    int t;
    cin>>t;
    int n,j;
    cin>>n>>j;
    cout<<"Case #1:"<<endl;
    pw();
    int count=0;
    for(int x=32769;x<=65536;x+=2)
    {
        string s=bin(x);
        if(check(s))
        {
            for(int i=2;i<11;i++)
            {
                cout<<ans[i]<<" ";
            }
            cout<<endl;
            count++;
        }
        if(count==j)
        break;
        
    }
    return 0;
}

