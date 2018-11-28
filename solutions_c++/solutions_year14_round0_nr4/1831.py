#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int n;

int fun(vector<double> vec1, vector<double> vec2)
{
    int ans = 0;
    int begin = 0;
    int end = vec1.size()-1;

    for(int i=n-1;i>=0;i--)
    {
        if(vec2[i] >= vec1[end])
        {
            begin++;
        }
        else
        {
            end--;
            ans++;
        }
    }

    return ans;
}


int main()
{
    freopen("D:\\a.in","r", stdin);
    freopen("D:\\b.txt","w", stdout);

    int q;
    double num;
    cin>>q;

    for(int t=1;t<=q;t++)
    {
        cin>>n;
        vector<double> vec1;
        vector<double> vec2;

        for(int i=0;i<n;i++)
        {
            cin>>num;
            vec1.push_back(num);
        }
        for(int i=0;i<n;i++)
        {
            cin>>num;
            vec2.push_back(num);
        }

        sort(vec1.begin(),vec1.end());
        sort(vec2.begin(),vec2.end());

        int ans1 = fun(vec1,vec2);
        int ans2 = n - fun(vec2,vec1);


        cout<<"Case #"<<t<<": ";
        cout<<ans1<<" "<<ans2<<endl;

    }

}
