#include<bits/stdc++.h>
using namespace std;

long long isPrime(long long n)
{
    long long r,f;
    if (n==1)
        return n;
    else if (n<4)
        return 0;
    else if (n%2==0)
        return 2;
    else if (n<9)
        return 0;
    else if (n%3==0)
        return 3;
    else
    {
        r=sqrt(n);
        f=5;
        while(f<=r)
        {
            if (n%f==0)
            {
                return f;
                break;
            }
            if (n%(f+2)==0)
            {
                return f+2;
                break;
            }
            f=f+6;
        }
        return 0;
    }
}

string print_binary(int n, int digit){
    string str="";
    int bit = 1<<digit - 1;
    while ( bit ) {
        str+=((n & bit ? 1 : 0)+'0');
        bit >>= 1;
    }
    return '1'+str+'1';
}

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tt;
    cin>>tt;
    for(int qq=1;qq<=tt;qq++){
        int nn,jj;
        cin>>nn>>jj;
        cout<<"Case #"<<qq<<":"<<endl;
        int digit=nn-2;
        int n=1<<digit;
        string str;
        for(int i=0;i<n && jj>0;i++){
            str=print_binary(i,digit);
            long long divisor[11]={0};
            int flag=0;
            for(int j=2;j<=10;j++){
                divisor[j]=isPrime(stoll(str,nullptr,j));
                if(!divisor[j]) flag=1;
            }
            if(flag==0){
                cout<<str<<" ";
                for(int j=2;j<=10;j++)
                    cout<<divisor[j]<<" ";
            cout<<endl;
            jj--;
            }
        }
    }
    return 0;
}

