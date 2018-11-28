//includes
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <utility>
#include <algorithm>
#include <cassert>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

using namespace std;

#define inf 1e8

int main()
{
    freopen("/Users/arkanathpathak/Downloads/A-small-attempt0.in","r",stdin);
    freopen("/Users/arkanathpathak/Downloads/A-small-output","w",stdout);
    
    int test;
    cin >> test;
//    cout << test;
    
    for(int k=0;k<test;k++)
    {
        int a;
        cin >> a;
        a--;
        vector<int> v1,v2;
        for(int i = 0 ;i<4;i++)
        {
            
                int a1,a2,a3,a4;
                cin >> a1 >> a2 >> a3 >> a4;
                if(i==a)
                {
                    v1.push_back(a1);
                    v1.push_back(a2);
                    v1.push_back(a3);
                    v1.push_back(a4);
                }
        }
        int b;
        cin >> b;
        b--;
        for(int i = 0 ;i<4;i++)
        {
            
            int a1,a2,a3,a4;
            cin >> a1 >> a2 >> a3 >> a4;
            if(i==b)
            {
                v2.push_back(a1);
                v2.push_back(a2);
                v2.push_back(a3);
                v2.push_back(a4);
            }
        }
        vector<int> ans;
        for(int i=0;i<v1.size();i++)
        {
            if(find(v2.begin(), v2.end(), v1[i])!=v2.end())
            {
                ans.push_back(v1[i]);
            }
        }
        cout << "Case #" << k+1 <<": ";
        if(ans.size()==0) cout << "Volunteer cheated!" << endl;
        else if(ans.size()>1) cout << "Bad magician!" << endl;
        else cout << ans[0] << endl;
    }

    
    return 0;
}