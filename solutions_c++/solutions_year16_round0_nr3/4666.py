#include <bits/stdc++.h>
using namespace std;

vector<int>v;
vector<int>::iterator it;
int prime(long long int n)
{
    long long int temp=n;

    if(n%2 == 0)
    {
        v.push_back(2);
        return 0;
    }
    for (int i = 3; i <= sqrt(n); i = i+2)
    {
        if(n%i == 0)
        {
            v.push_back(i);
            return 0;
        }
    }
    if (n > 2 && n!=temp)
        {
        v.push_back(n);
        return 0;
        }
}

string addstrings( string first, string second )
{
    string result;
    int length = first.length();
    int carry = 0;
    for (int i = length-1 ; i >= 0 ; i--)
    {
        int firstBit = first.at(i) - '0';
        int secondBit = second.at(i) - '0';
        int sum = (firstBit ^ secondBit ^ carry)+'0';
        result = (char)sum + result;
        carry = (firstBit & secondBit) | (secondBit & carry) | (firstBit & carry);
    }
    if (carry)
        result = '1' + result;
    return result;
}

long long int b2d(string s,int k)
{
    long long int sum2=0;
    int j=1;
    sum2=1+pow(k,s.length()-1);
    int i=(s.length()-2);
    do
    {
    if(s[i]=='1')
    {
    sum2+=pow(k,j);
    }
    i--;
    j++;
    }while(i>=1);
    return sum2;
}

int main()
{
    freopen("abc.out","w",stdout);
    string s;
    string s2;
    int t;
    cin>>t;
    int n,j;
    cin>>n>>j;
    long long int f;
    s.assign(n,'0');
    s2.assign(n,'0');
    s[0]='1';
    s[n-1]='1';
    s2[n-2]='1';
    //s=addstrings(s,s2);
    cout<<"Case #"<<t<<":"<<endl;
    while(j!=0)
    {
    for(int k=2;k<=10;k++)
    {
      f=b2d(s,k);

      prime(f);
    }
    if(v.size()==9)
            {
                cout<<s;
                for(it=v.begin();it!=v.end();++it)
                {
                    cout<<" "<<*it;
                }
                j--;
                cout<<endl;
            }
    v.clear();
    s=addstrings(s,s2);
    }

    return 0;
}
