#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t,s,sum,res;
    char aux;
    vector <int> vec;
    cin>>t;
    for (int c=0;c<t;c++)
    {
        sum=0;
        res=0;
        vec.clear();
        cin>>s;
        for(int d=0;d<s+1;d++)
        {
            cin>>aux;
            vec.push_back(aux-48);
        }
        sum+=vec[0];
        for(int pos=1;pos<s+1;pos++)
        {
            if (pos<=sum) sum+=vec[pos];
            else
            {
                res+=pos-sum;
                sum+=pos-sum+vec[pos];
            }
        }

        cout<<"Case #"<<c+1<<": "<<res<<endl;
    }
    return 0;
}
