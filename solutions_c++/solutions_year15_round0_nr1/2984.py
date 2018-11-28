#include<iostream>
#include<math.h>
#include<stdio.h>
#include<string>
using namespace std;
int print(int a, int n)
{
    cout<<"Case #"<<n<<": "<<a<<endl;
    return 0;
}
int n, test;
string s;
int main()
{
    freopen("jam1.txt", "w", stdout);
    cin>>test;
    for(int t=1 ; t<=test ; t++)
    {
        cin>>n;
        cin>>s;
        int sl = s.length(), acc=0, ans=0;
        for(int i = 0 ; i < sl ; i++)
        {
            if(i > acc)
            {
                ans += i - acc;
                acc = i;
            }
            acc += s[i] - '0';
        }
        print(ans, t);
    }
}
