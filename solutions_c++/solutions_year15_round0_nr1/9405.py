//pranjalr34
#include<bits/stdc++.h>
using namespace std;
long long int gcd(long long int m, long long int n){if(n == 0) return m;return gcd(n, m % n);}  
long long int fastpow(long long int a, long long int b,long long int m){long long int r = 1;while (b > 0){if (b % 2 == 1)r = (r * a) % m;b = b >> 1;a = (a * a) % m;}return r;}
int prime(long long int x){if(x==1)return 0;if(x<=3)return 1;if(x%6==1||x%6==5){long long int y=sqrt(x),i;for(i=2;i<=y;i++)if(x%i==0)return 0;return 1;} return 0;}
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    long long int s,t,current,invite,i,j=1;
    string str;
    cin >>t;
    vector <int> vec(1010);
    while(t--)
    {
        cin >>s;
        cin >>str;
        current=0,invite=0;
        for(i=0;i<(s+1);i++)
            vec[i]=str[i]-'0';
        for(i=0;i<(s+1);i++)
        {
            if(vec[i]!=0)
            {
                if(i>current){
                    invite+=(i-current);
                    current=i;}
                current=current+vec[i];
            }
        }
        cout <<"Case #"<<j<<": "<<invite<<"\n";
        j++;
    }
    return 0;
}
