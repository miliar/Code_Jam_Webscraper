#include <iostream>
#include <set>

using namespace std;

int main()
{
    long long int n,k,p,r,l;


    cin>>n;
    for(long long int i=0;i<n;i++){
    set <int> s;
    cin>>k;
    if(k==0)
    cout<<"Case #"<<i+1<<": "<<"INSOMNIA\n";
    else{
    for(long long int j = 1;;j++)
    {
        p=k*j;
        l=p;
        while(p)
        {
        r=p%10;
        s.insert(r);
            p=p/10;
        }

    if(s.size()==10)
    {cout<<"Case #"<<i+1<<": "<<l<<"\n";break;}

            }
            }
            }
return 0;
}
