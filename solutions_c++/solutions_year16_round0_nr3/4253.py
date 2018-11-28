#include <bits/stdc++.h>
using namespace std;
bool isprime(long long int k)
{
    if(k%2==0) return false;
    else
    {
        for(long long int j=3;j<=sqrt(k)+1;j=j+2)
            if(k%j==0) return false;
        return true;
    }
}
int main()
{
    freopen("C.in","r",stdin);
    freopen("output2.in","w",stdout);
    long long int n,t,k,rem,temp,no[9], c=0,te=0,l,i;
    string s;
    cin>>l>>n>>t;
    while(l--)
    {k=pow(2,n-1)+1;
    cout<<"Case #1: \n";
    while(te!=t)
    {
        temp=k;
        while(temp!=0)
        {
           rem=temp%2;
           temp=temp/2;
           s+= static_cast<ostringstream*>( &(ostringstream() << rem) )->str();
        }
        reverse(s.begin(),s.end());
        for(int j=2;j<=10;j++)
        {
        i=stoll(s,nullptr,j); //cout<<i << " ";
        if(isprime(i))
           {break;}
        else
        {
            for(long long int z=2;z<=i-1;z++)
            {
                if(i%z==0) { //cout<< i << "\t"<< z << "\n";
                        no[c]=z;c++; break;}
            }
        }

    if(c==9)
    {   if(s[s.length()-1]=='1')
        {cout<< s << " ";
        for(int z=0;z<9;z++)
            cout<<no[z]<<" ";
    cout<<" \n";
    te++;}
    }
    }
    c=0;
    s.erase(s.begin(),s.end());
    k++;
    }
    }
    return 0;
}
