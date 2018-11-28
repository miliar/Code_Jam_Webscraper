#include <iostream>
#include <vector>
#include <string>
using namespace std;
class solution
{
    public:
        void insertion_sort(string &a,int n)
        {
            vector<char> b;
            b.push_back(a[0]);
            long len=a.length();
            for(int i=1;i<len;i++)
            {
                if(a[i]>=b[0])
                {
                    b.insert(b.begin(),a[i]);
                }
                if(a[i]<b[0])
                {
                    b.push_back(a[i]);
                }
                
            }
            cout<<"Case #"<<n<<": ";
            for(long i=0;i<b.size();i++)
            {
                cout<<b[i];
            }
            cout<<endl;
        }
    };
    int main()
    {
        int n;
        cin>>n;
        vector<string> b;
        for(int i=0;i<n;i++)
        {
            string cval;
            cin>>cval;
            b.push_back(cval);
        }
        solution po;
        for(int i=0;i<n;i++)
        {
            po.insertion_sort(b[i],i+1);
        }
        return 0;
    }
