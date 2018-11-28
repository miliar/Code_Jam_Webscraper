#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream cin("in.dat");
    ofstream cout("out.dat");
    int t;
    cin>>t;
    for(int k=0;k<t;k++)
    {
        int n;
        int cur=0;
        int res=0;
        char c;
        int i=0;
        cin>>n;
        n++;
        while(n--)
        {
            cin>>c;
            cur+=c-'0';
            i++;
            if(cur<i)
            {
                cur++;
                res++;
            }
        }
        cout<<"Case #"<<k+1<<": "<<res<<endl;
    }
    return 0;
}
