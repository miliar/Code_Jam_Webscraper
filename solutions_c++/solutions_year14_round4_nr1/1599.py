//#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <math.h>

#define cout out
#define cin in

using namespace std;
ofstream out("output.txt");
ifstream in("input.txt");
int main()
{
    int t;
    cin>>t;
    for (int i=1;i<=t;i++)
    {
        int n;
        cin>>n;
        int x;
        cin>>x;
        vector<int> v;
        for (int j=0;j<n;j++)
        {
            int y;
            cin>>y;
            v.push_back(y);
        }
        sort(v.begin(),v.end());
        int sch=0;
        int l=0;
        int r=n-1;
        while(l<=r)
        {
            if (l==r)
            {
                sch++;
                l++;
            }
            else
            {
                if (v[l]+v[r]<=x)
                {
                    l++;
                    r--;
                    sch++;
                }
                else
                {
                    sch++;
                    r--;
                }
            }
        }
        cout<<"Case #"<<i<<": "<<sch<<endl;
    }
    return 0;
}