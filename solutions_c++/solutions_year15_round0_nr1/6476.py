#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
using namespace std;
int main()
{
    int t;
    cin >> t;
    for(int j=1;j<=t;j++)
    {
        int n;
        cin >> n;
        char c;
        cin >> c;
        int sum = c - '0',ans=0;
        for(int i=1;i<=n;i++)
        {
            if(sum < i)
            {
                ans += i-sum;
                sum += i-sum;
            }
            cin >> c;

            sum += c - '0';
        }
        cout << "Case #" << j <<": "<< ans <<endl;
    }
    return 0;
}
