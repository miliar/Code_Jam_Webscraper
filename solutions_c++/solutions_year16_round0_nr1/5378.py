#include<iostream>
#include<algorithm>
#include<math.h>
#include<cmath>
#include<sstream>
#include<string>
#include<string.h>
using namespace std;
#define ll  long long
bool arr[10];
bool finish()
{
    for(ll i=0;i<10;i++)
        if(!arr[i])
        return 0;
    return 1;

}
void calc(ll number)
{
    while(number)
    {
        arr[number%10]=1;
        number/=10;
    }
}
int main()
{
freopen("O.txt","w",stdout);
freopen("I.txt","r",stdin);

ll t,n,counter,temp;
cin>>t;
for(ll i=1;i<=t;i++)
{
    cin>>n;
    memset(arr,false,sizeof arr);
    temp=n;
    counter=0;
    if(!n)
        cout<<"Case #"<<i<<": INSOMNIA"<<endl;
    else
    {
    while(true)
    {
        calc(n);
        counter++;
        if(finish())
            break;
        n+=temp;

    }
cout<<"Case #"<<i<<": "<<n<<endl;
    }
}
return 0;
}


