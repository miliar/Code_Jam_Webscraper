#include <cstdio>
#include <cmath>
#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <map>
#include <cassert>
#include <string>
#include <cstring>
#include <queue>

using namespace std;

 
typedef long long int LL;

int main()
{
	ios::sync_with_stdio(0);

    int T;
    int t=1;
    cin>>T;

    while(t<=T)
    {

        string s;
        cin>>s;
        string ans;
        ans.push_back(s[0]);
        for(int i=1;i<s.size();i++)
        {
            if(s[i]>=ans[0])
            {
                string temp;
                temp=s[i]+ans;
                ans.clear();
                ans=temp;
            }
            else
            {
                ans.push_back(s[i]);
            }
        }
        cout<<"Case #"<<t<<": "<<ans<<endl;
        t++;
    }
	

return 0;
}    