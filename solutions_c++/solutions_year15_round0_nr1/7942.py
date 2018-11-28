#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int t;
    int smax;
    string s;
    cin>>t;
    int j=1;
    while(t--)
    {
   cin>>smax>>s;
   int sum =0, ans=0,temp;
   for(int i=0;i<s.length();i++)
   {
       temp = s[i]-'0';
        if(sum< i && temp!=0)
        {
            ans += i-sum;
            sum += i-sum;
        }
        sum += temp;
   }
   cout<<"Case #"<<j++<<": "<<ans<<endl;
    }
    return 0;
}

