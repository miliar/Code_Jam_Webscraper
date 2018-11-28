#include<iostream>
#include<vector>
#include<string>

using namespace std;
int find(string s);
int main()
{
    string s;
    vector<int>v;
    int t,a;
    cin>>t;
    for(int i=0;i<t;i++)
   {
       cin>>a;
       cin>>s;
       v.push_back(find(s));
   }
   for(int i=0;i<t;i++)
   {
       cout<<"Case #"<<i+1<<": "<<v[i]<<endl;
   }
   return 0;
}

int find(string s)
{
    int count=0,p=s[0]-'0';
    for(int i=1;i<s.length();i++)
    {
        if(i>p)
        {
            count++;
            p++;
        }
        p=p+(s[i]-'0');
    }
    return count;
}
