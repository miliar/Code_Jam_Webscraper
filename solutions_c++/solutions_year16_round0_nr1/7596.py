#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class solution
{
public:
    void sol(int &n,int i)
    {
        vector<int> s;
        for(int j=0;j<10;j++)
        {
            s.push_back(j);
        }
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            return;
        }
        int nl=n;
        int k=1;
        int res=0;
        int c=10;
        while(s.size()!=0)
        {
            n=k*nl;
            int t=n;
            while(t>0)
            {
                for(int j=0;j<c;j++)
                {
                    if(t%10==s[j])
                    {
                        s.erase(s.begin()+j);
                        c--;
                        break;
                    }
                }
                t=t/10;
                if(s.size()==0) break;
            }
            k++;
            res=n;
        }
        cout<<"Case #"<<i<<": "<<res<<endl;
        return;
        
    }
    
};
int main()
{
    int t;
    cin>>t;
    vector<int> ar;
    for(int i=0;i<t;i++)
    {
        int cval;
        cin>>cval;
        ar.push_back(cval);
    }
    solution po;
    for(int i=0;i<t;i++)
    {
        po.sol(ar[i],(i+1));
    }
    return 0;
}