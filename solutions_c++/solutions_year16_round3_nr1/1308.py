#include <iostream>
#include <algorithm>
#include <set>
#include <fstream>
using namespace std;
int a[123];



int main()
{
    ifstream inf;
    inf.open("a.in");
    int T;
    inf >> T;
    for(int tt = 1 ; tt <= T ; tt++)
    {
        int n;
        inf >> n;
        int sum = 0;
        for(int i = 0 ; i < n ; i++)
        {
            inf >> a[i];
            sum += a[i];
        }
        cout << "Case #" << tt << ": ";
        while(sum != 0)
        {
            if(sum == 3)
            {
                int cnt = 0;
                int mx = 0;
                for(int i = 0 ; i < n ; i++)
                {
                    if(a[i] == 1)cnt++;
                }
                if(cnt == 3)
                {
                    bool q = false;
                    for(int i = 0 ; i < n ; i++)
                    {
                        if(a[i] == 1 && q == false)
                        {
                            q = true;
                            cout << char('A' + i) << " ";
                        }
                        else if(a[i] == 1)
                        {
                            cout << char('A' + i);
                        }
                    }
                }
                else
                {
                    for(int i = 0 ; i < n ;i++)
                    {
                        if(a[i] == 2)
                        {
                            cout << char('A' + i)<<" ";
                        }
                    }
                    for(int i = 0 ; i < n ; i++)
                    {
                        if(a[i] != 0)cout << char('A' + i);
                    }
                }
                //cout << endl;
                break;
            }
            int mx = -1;
            for(int i = 0 ; i < n ; i++)
            {
                mx = max(mx , a[i]);
            }
            int idx = -1;
            for(int i = 0 ; i < n ; i++)
            {
                if(a[i] == mx)
                {
                    idx = i;
                    break;
                }
            }
            a[idx]--;
            sum--;
            
            cout << char('A' + idx);
            if(sum == 0)break;
            mx = -1;
            for(int i = 0 ; i < n ; i++)
            {
                mx = max(mx , a[i]);
            }
            idx = -1;
            for(int i = 0 ; i < n ; i++)
            {
                if(a[i] == mx)
                {
                    idx = i;
                    break;
                }
            }
            a[idx]--;
            sum--;
            cout << char('A' + idx);
            cout << " ";
        }
        cout << endl;
    }
}