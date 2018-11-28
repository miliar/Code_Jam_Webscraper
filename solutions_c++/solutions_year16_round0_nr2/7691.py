#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class solution
{
public:
    void sol(string &n,int i)
    {
        long len=n.length();
        int count=0;
        if(judge(n,'+'))
        {
            cout<<"Case #"<<i<<": "<<count<<endl;
            return;
        }
        for(int in=1;in<len;in++)
        {
            while(n[in-1]==n[in])
            {
                in++;
                if(in+1==len) break;
            }
            if(n[in-1]!=n[in])
            {
                for(int j=0;j<in;j++)
                {
                    change(n[j]);
                }
                count++;
                if(n[len-1]=='+'&&judge(n,n[len-1]))
                   {
                       cout<<"Case #"<<i<<": "<<count<<endl;
                       return;
                   }
                if(n[len-1]=='-'&&judge(n,n[len-1]))
                   {
                       cout<<"Case #"<<i<<": "<<count+1<<endl;
                       return;
                   }
            }
        }
        if(n[0]=='-')
        {
            count++;
        }
        cout<<"Case #"<<i<<": "<<count<<endl;
        return;
        
    }
private:
    void change(char &a)
    {
        if(a=='+')
        {
            a='-';
        }
        else a='+';
    }
    bool judge(string &a,char c)
    {
        long len=a.size();
        for(int i=0;i<len;i++)
        {
            if(a[i]!=c)
                return false;
        }
        return true;
    }
    
};
int main()
{
    int t;
    cin>>t;
    vector<string> ar;
    for(int i=0;i<t;i++)
    {
        string cval;
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