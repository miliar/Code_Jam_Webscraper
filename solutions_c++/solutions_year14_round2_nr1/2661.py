#include <iostream>
#include <fstream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <vector>

using namespace std;

typedef long long ll;
typedef long double ld;

vector<int> arr[100];

string gett(string s)
{
    string ans="";
    char lst=' ';
    for (int i=0;i<s.size();++i)
    {
        if (s[i]!=lst)
        {
            ans+=s[i];
            lst=s[i];
        }
    }
    return ans;
}

void check(string s)
{
    s+=" ";
    char lst=' ';
    int cnt=0;
    int now=-1;
    for (int i=0;i<s.size();++i)
    {
        if (s[i]!=lst)
        {
            if (lst!=' ')
                arr[now].push_back(cnt);
            ++now;
            cnt=1;
            lst=s[i];
        }
        else
            ++cnt;
    }

}

int main()
{
    ios_base::sync_with_stdio(false);
    int t;
    cin>>t;
    for (int ij=1;ij<=t;++ij)
    {
        for (int i=0;i<100;++i)
            arr[i].clear();
        int n;
        cin>>n;
        cout<<"Case #"<<ij<<": ";
        string s;
        string s2;
        cin>>s2;
        s=gett(s2);
        check(s2);
        bool fl=false;
        for (int i=1;i<n;++i)
        {
            cin>>s2;
            if (gett(s2)!=s)
            {
                cout<<"Fegla Won\n";
                fl=true;
                break;
            }
            check(s2);
        }
        if (fl)
            continue;
        int ans=0;
        for (int i=0;i<s.size();++i)
        {
            nth_element(arr[i].begin(),arr[i].begin()+arr[i].size()/2,arr[i].end());
            //cout<<arr[i].size()<<"\n";
            int x=arr[i][arr[i].size()/2];
            //cout<<x;
            for (int j=0;j<arr[i].size();++j)
                ans+=abs(arr[i][j]-x);
        }
        cout<<ans<<"\n";
    }

    return 0;
}

