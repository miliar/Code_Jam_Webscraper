#include<iostream>
#include<cmath>
#include<string>

using namespace std;
string str;




void calculate()
{
    string ans;

   for(auto i=str.begin();i!=str.end();++i)
    {
        if(ans.empty())
        {
            ans.push_back(*i);
        }
        else{
            if(*i<ans[0])
                ans.push_back(*i);
            else
                ans.insert(0,1,*i);
            }

    }

    cout<<ans<<endl;
}

int main()
{
    int n;
    cin>>n;

    for(int i=1;i<=n;i++)
    {
       cin>>str;
     cout<<"Case #"<<i<<": ";
     calculate();

    }

    return 0;
}
