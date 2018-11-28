#include <iostream>
#include <vector>
#include <string>
using namespace std;
class solution
{
public:
    void sol(vector<int> each,int i)
    {
        int k=each[0];
        int c=each[1];
        int s=each[2];
        vector<int> ans;
        for(int j=1;j<=k;j++)
        {
            ans.push_back(j);
        }
        cout<<"Case #"<<i<<": ";
        for(int j=0;j<k;j++)
        {
            cout<<ans[j]<<" ";
        }
        cout<<endl;
    }
};
int main()
{
    int t;
    cin>>t;
    vector<vector<int>> a;
    for(int i=0;i<t;i++)
    {
        vector<int> each;
        int k,c,s;
        cin>>k>>c>>s;
        each.push_back(k);
        each.push_back(c);
        each.push_back(s);
        a.push_back(each);
    }
    solution po;
    for(int i=0;i<t;i++)
    {
        po.sol(a[i],i+1);
    }
    
}