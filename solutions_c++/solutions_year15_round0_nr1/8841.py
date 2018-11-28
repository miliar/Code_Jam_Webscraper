#include <iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
   {
   freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
    int T,maximumshyness,case1=1,sum=0,sum2=0;
    bool y=true;
    string s;
    cin>>T;
    while(T--)
    {
        cin>>maximumshyness;
    cin>>s;

  for(int i=0;i<s.size();i++)
{
    if(sum<i)
    {
        sum2+=i-sum;
        sum+=i-sum;
        y=false;
    }

    sum+=s[i]-'0';
}
if(y)
    cout<<"Case "<<"#"<<case1++<<": "<<"0"<<endl;
else
 cout<<"Case "<<"#"<<case1++<<": "<<sum2<<endl;
    sum=0,y=true,sum2=0;
    }

    return 0;
}
