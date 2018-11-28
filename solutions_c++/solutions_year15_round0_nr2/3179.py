#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int T;
    cin >> T;
    for(int i=1;i<=T;i++)
    {
        int D;
        vector <int> P;
        cin >> D;
        for(int j=0;j<D;j++)
        {
            int m;
            cin >> m;
            P.push_back(m);
        }
        make_heap (P.begin(),P.end());
        int k,l,a,ack=0,res,sum;
        k=P.front();
        res=k;
            for(int r=1;r<=k;r++)
            {
                sum=r;
                for(int d=0;d<D;d++)
                {
                    if (P[d]>r)
                    {
                        if (P[d]%r==0)
                            sum+=P[d]/r-1;
                        else
                            sum+=P[d]/r;
                    }
                }
                res=min(res,sum);
            }



        cout << "Case #"<< i <<": "<<res<<endl;
    }
    return 0;
}
