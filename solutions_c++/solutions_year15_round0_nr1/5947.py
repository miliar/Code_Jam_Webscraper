#include<iostream>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int test=1;test<=t;test++)
    {
        int ppl;
        long long total=0;
        long long needed=0;
        cin>>ppl;
        string arr;
        cin>>arr;
        for(long long i=0;i<=ppl;i++)
        {
            int
             l=arr[i]-48;
            if(total>=i)
                total+=l;
            else{
                needed=needed+i-total;
                total=i+l;
            }

        }
        cout<<"Case #"<<test<<": "<<needed<<"\n";
    }
    return 0;
}
