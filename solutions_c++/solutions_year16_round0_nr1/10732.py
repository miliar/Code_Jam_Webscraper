#include <iostream>
#include <algorithm>
#include <iomanip>
using namespace std;
bool sleep(long int seen[])
{
    for(int i=0;i<10;i++)
    {
        if(seen[i]==0) return false;
    }
    return true;
}
int main()
{
    long int T,i=1;
    cin>>T;
    while(T--)
    {
        long int N;
        cin>>N;
        long int seen[10];
        fill_n(seen, 10, 0);
        if(N==0)
            cout<<"Case #0: INSOMNIA"<<endl;
        else
        {
            int j=0;
            long int x=N;
            while(N>0)
            {
                j++;
                long int m=N;
                while(m>0)
                {
                    int r=m%10;
                    seen[r]=seen[r]+1;
                    m/=10;
                }
                if(sleep(seen)){
                    cout<<"Case #"<<i<<": "<<N<<endl;
                    break;
                }
                N=(j+1)*x;
            }
        }
        i++;
    }
    return 0;
}

