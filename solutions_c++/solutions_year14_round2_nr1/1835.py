#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstdlib>
#include <map>
#include <stack>

using namespace std;

int foo(string s1, string s2)
{
    int cnt = 0, i = 0, j = 0, n = s1.size(), m = s2.size();
    
    while(i < n && j < m)
    {
        if(s1[i] == s2[j])
            i++, j++;
        else    
        {
            if(i != 0 && s1[i] == s1[i-1])
                i++, cnt++;
            else if(j != 0 && s2[j] == s2[j-1])
                j++, cnt++;
            else
                return -1;
        }
    }
    
    if(i != n)
    {
        if(s1[i] == s2[m-1])
            cnt += n-i;
        else
            return -1;
    }
    else if(j != m)
    {
        if(s1[n-1] == s2[j])
            cnt += m-j;
        else
            return -1;
        
    }
    return cnt;
}
int main()
{
    int n, cases, ctr = 1, res;
    cin >> cases;
    
    while(cases--)
    {
        cin >> n;
        string str1, str2;
        
        cin >> str1 >> str2;
        
        res = foo(str1, str2);
        cout << "Case #" << ctr++ << ": ";
        if(res == -1)
            cout << "Fegla Won" << endl;
        else
            cout << res << endl;
    }     
    
    return 0;
}
