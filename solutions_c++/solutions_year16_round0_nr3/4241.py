#include <iostream>
#include<cstring>
#include<cmath>
using namespace std;
string increment(string);
bool isprime(long int);
int trivial(long int);
long int base(int i,string s)
{
    long int n=0,k=0;
    for(int j=s.size()-1;j>=0;j--){
        n=n+pow(i,k)*(s[j]-'0');
        k++;
    }
    return n;
}
bool isprime(long int n)
{
    for(int i=2;i<=sqrt(n);i++)
    {
        if(n%i==0)
            return false;
    }
    return true;
}
string increment(string s)
{
    char carry='1';
    for(int i=s.size()-1;i>=0;i--)
    {
        if(s[i]=='1'&&carry=='1'){
                s[i]='0';
                carry='1';
        }
        else if(s[i]=='0'){
            s[i]=carry;
            carry='0';
        }
    }
    s[s.size()-1]='1';
    return s;
}
int trivial(long int n)
{
    for(int i=3;i>0;i++)
    {
        if(n%i==0)
            return i;
    }
}
int main()
{
    int t,p=0;
    cin>>t;
    while(t--){++p;
        int n,j;
        cin>>n>>j;
        string str="";
        for(int i=0;i<n;i++)
        {
            if(i==0||i==n-1)
                str=str+"1";
            else
                str=str+"0";
        }
        cout<<"Case #"<<p<<": "<<endl;
        while(j--){
            long int num;
            int a[11]={0};
            for(int i=2;i<=10;i++){
                num=base(i,str);
                if(isprime(num)){
                    str=increment(str);
                    i=1;
                    continue;
                }
                else{
                    a[i]=trivial(num);
                }
            }
            cout<<str<<" ";
            for(int i=2;i<=10;i++)
                cout<<a[i]<<" ";
            cout<<endl;
            str=increment(str);
        }
    }
    return 0;
}
