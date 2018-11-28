#include<bits/stdc++.h>
using namespace std;
int arr[32];
int n;
int jam;
vector<int> v;
vector<long long int> data;
void printarr()
{
    for(int i=0;i<n;i++)
        cout<<arr[i];
}
void init()
{
    for(int i=0;i<=n;i++)
        arr[i]=1;
}
long long int isprime(long long int n)
{
    long long int ans=-1;
    long long int srot=sqrt(n);
 for(int i=2;i<=srot;i++)
 {
     if(n%i==0)
     {
         return i;
     }
 }
 return ans;
}
long long int convertbase(int base)
{
   long long  int ans=0,num=1;
    for(int i=n-1;i>=0;i--)
    {
        ans+=arr[i]*num;
        num=num*base;
    }
    return ans;
}
bool inv(int val)
{
    int siz=v.size();
    for(int i=0;i<siz;i++)
    {
        if(v[i]==val)
            return true;
    }
    return false;
}
bool indata(long long int val)
{
    int siz=data.size();
    for(int i=0;i<siz;i++)
    {
        if(data[i]==val)
            return true;
    }
    return false;
}
void printfac()
{
    for(int i=2;i<=10;i++)
    {
        long long int data=convertbase(i);
        cout<<isprime(data)<<" ";
    }
}
void rec()
{

    if(jam==0)
        return;
    int temp=-2;
    for(int j=1;j<n-1;j++)
    {
        temp=-2;
        if(inv(j)==false)
        {
        arr[j]=0;
        v.push_back(j);
        for(int i=2;i<=10;i++)
        {

            long long int data=convertbase(i);
             int ex=isprime(data);
            if(ex==-1)
            {
                temp=2;
                break;
        }
        }
        if(temp==-2 && indata(convertbase(10))==false)
        {
            if(jam==0)
                return;
                data.push_back(convertbase(10));
            jam--;
            printarr();
            cout<<" ";
            printfac();
            cout<<endl;
        }
        rec();
        arr[j]=1;
        v.erase(find(v.begin(),v.end(),j));
        }
    }
    }

int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("coinjamssssss1234576894u594.out","w",stdout);
    int t;
    cin>>t;
    cin>>n>>jam;
    cout<<"Case #1:"<<endl;
    init();
    int temps=-99;
    for(int i=2;i<=10;i++)
        {

            long long int data=convertbase(i);
             long long int ex=isprime(data);
            if(ex==-1)
            {
                temps=200;
                break;
        }
        }
        if(temps==-99)
        {
            data.push_back(convertbase(10));
            jam--;
            printarr();
            cout<<" ";
            printfac();
            cout<<endl;
        }
    rec();
}
