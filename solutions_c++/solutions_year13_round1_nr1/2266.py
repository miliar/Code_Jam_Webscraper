#include<iostream>
using namespace std;
long long int r,th;
int main()
{
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
        cin>>r>>th;
        int n=1;
        while((2*n*r + 2*n*n - n) <= th)
        {
            n++;
        }
        cout<<"Case #"<<cas<<": "<<n-1<<endl;
        cas++;
    }
}
