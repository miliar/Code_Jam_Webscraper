#include<iostream>
#include<bitset>
#include<string>

using namespace std;

int main()
{
 int t,t1;
 cin>>t;
 t1=t;
 bitset<10> b;
 while(t--)
 {
    int n,l;
    string s;
    cin>>n;
    int i=1;
    int flag=0;
    long long m;
    while(!b.all())
    {
        m=n*i;
        if(m==0)
        {
            cout<<"Case #"<<(t1-t)<<": INSOMNIA"<<endl;
            flag=1;
            break;
        }

        s=to_string(m);
        l=s.length();
        for(int j=0;j<l;j++)
        {
            b.set(s[j]-48);
        }
        i++;
    }
    if(flag==0)
    {
        cout<<"Case #"<<(t1-t)<<": "<<m<<endl;
    }
    b.reset();
 }
 return 0;
}

