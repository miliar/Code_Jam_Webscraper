#include <iostream>
#include <cmath>

using namespace std;

long long int power(long long int x, long long int y)
{
    long long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}

int main(){
    int t;
    int k,c,s;
    cin>>t;
    for (int x=1;x<=t;x++){
        cin>>k>>c>>s;
        cout<<"Case #"<<x<<": ";
        long long int a = 1;
        long long int d = power(k,c-1);
        for (int i=1;i<=s;i++){
            cout<<a<<" ";
            a = a + d;
        }
        cout<<"\n";
    }
}
