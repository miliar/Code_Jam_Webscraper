    #include <vector>
    #include <list>
    #include <map>
    #include <set>
    #include <queue>
    #include <deque>
    #include <stack>
    #include <bitset>
    #include <algorithm>
    #include <functional>
    #include <numeric>
    #include <utility>
    #include <sstream>
    #include <iostream>
    #include <iomanip>
    #include <cstdio>
    #include <cmath>
    #include <cstdlib>
    #include <ctime>

    using namespace std;

    int main()
    {
        freopen("A-small-attempt0.in","r",stdin);
        freopen("output.txt","w",stdout);
        int t;
        cin>>t;
        for(int i=0;i<t;i++)
        {
            int n,cnt=0,sum=0;
            cin>>n;
            string s;
            cin>>s;
            for(int j=0;j<s.size();j++)
            {
                if(sum<j){cnt+=j-sum; sum+=j-sum;}
                sum+=s[j]-'0';
            }
            cout<<"Case #"<<i+1<<": "<<cnt<<endl;

        }
        return 0;
    }
