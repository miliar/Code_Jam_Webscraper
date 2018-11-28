#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int main()
{
    int T,x=1;
    cin>>T;
    while(T--)
    {
        int N=0;
        cin>>N;
        if(N==0)
        { cout<<"Case #"<<x++<<": "<<"INSOMNIA\n"; continue;}
        vector <int> digits {0,1,2,3,4,5,6,7,8,9};
        vector<int> :: iterator dptr;
        int i=1;
        for(i=1;;i++)
        {
            int n=i*N;
            while(n)
            {
                int d=0;
                d=n%10;
                dptr=find(digits.begin(),digits.end(),d);
                if(dptr!=digits.end())
                    digits.erase(dptr,dptr+1);
                n=n/10;
            }
            if(digits.empty())
                break;
        }
        cout<<"Case #"<<x++<<": "<<i*N<<endl;
    }
    return 0;
}
