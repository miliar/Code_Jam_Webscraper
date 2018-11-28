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
int d, p[1003], test;
string s;
int main()
{
    freopen("jam1.txt", "w", stdout);
    cin>>test;
    for(int t=1 ; t<=test ; t++)
    {
        int ans , a = 1000;
        cin>>d;
        for(int i= 0 ; i < d ; i++)
        {
            cin>>p[i];
        }
        for(int i = 1 ; i < 1000; i++)
        {
            ans = i;
            for(int j = 0; j < d ; j++)
            {
                ans += (p[j] + i -1) / i -1;
            }
            a= min(a, ans);
        }
        print(a, t);
    }
}
