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


ct=0;
mul=1;
st=0;
num=0;
    for(int i=0;i<=9;i++)
        mp[i]=1;


cin>>n;
cout<<"Case #"<<++p<<": ";
int f=0;
while(1)
{
    ct++;
    if(ct>100000000)
        break;
    m=mul*n;
    while(m)
    {

        if(mp[m%10])
        {
            mp[m%10]=0;
            num++;
        }
        m/=10;
        if(num==10)
        {
            num=mul*n;
            f=1;
            break;
        }
    }
    if(num==10)
        {
            f=1;
            num=mul*n;
            break;
        }
if(f)
    break;
    mul++;
}
if(f)
    cout<<num<<endl;
else
    cout<<"INSOMNIA"<<endl;

    }
return 0;
}
