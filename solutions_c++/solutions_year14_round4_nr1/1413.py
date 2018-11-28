#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

int main()
{
    int t,c;
    cin>>t;
    c=1;
    while(c<=t)
    {
        vector<int> num;
        int n,x;
        cin>>n>>x;
        int mid;
        int i,j;
        for(i=0;i<n;i++)
        {
            cin>>mid;
            num.push_back(mid);
        }
        sort(num.begin(), num.end());
        int disc=0;
        for(i=0, j=num.size()-1; i<=j;)
        {
            if(num[i]+num[j] <= x){
                disc++;
                i++;
                j--;
            } else {
                j--;
                disc++;
            }
        }
        if(i==j)
        {
            disc++;
        }
        cout<<"Case #"<<c<<": "<<disc<<endl;
        c++;
    }
    return 0;
}

