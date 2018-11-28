#include <iostream>
#include <algorithm>
#include <map>
#include <bitset>
#include <set>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <string>
#include <string.h>
#include <cstring>
#include <iomanip>
#include <stdio.h>
#include <sstream>
#include <bitset>
#include <locale>
#include <iostream>
#include <cmath>
#include <iomanip>
#include <math.h>
#include <bitset>
#include<sstream>
#include<string>
#include<string.h>
using namespace std;
#define ll  long long
ll carry;
vector<unsigned ll>numbers;
int n,j;

void bt(unsigned ll number=1,int digits=1)
{
    if(digits==n-1)
    {
        numbers.push_back(number*10+1);
        return ;
    }
    bt(number*10+1,digits+1);
    bt(number*10,digits+1);
}


bool isprime(ll number)
{
    for(ll i=2;i*i<=number;i++)
        if(number%i==0)
        {
            carry=i;
            return 0;
        }
    return 1;
}


unsigned ll transform(ll number,unsigned ll base)
{
    if(base==10)
        return number;
    unsigned ll answer=1;
    unsigned base_temp=base;
    number/=10;
    while(number)
    {
        answer+=(number%10)*base;
        base*=base_temp;
        number/=10;
    }
    return answer;

}

void GOT(ll number)
{
    ll arr[11];
    for(int i=2;i<=10;i++)
        arr[i]=transform(number,i);
    for(int i=2;i<=10;i++)
        if(isprime(arr[i]))
        return;
    else
        arr[i]=carry;
    cout<<number;
    for(int i=2;i<=10;i++)
        cout<<" "<<arr[i];
    cout<<endl;
    j--;
}

int main()
{
ios::sync_with_stdio(false);
ios_base::sync_with_stdio(false);
cin.tie(nullptr), cout.tie(nullptr);
freopen("O.txt","w",stdout);
freopen("I.txt","r",stdin);

int t;
cin>>t;
for(int i=1;i<=t;i++)
{
cout<<"Case #"<<i<<":"<<endl;
cin>>n>>j;
bt();
sort(numbers.begin(),numbers.end());
for(ll i=0;j && i<numbers.size();i++)
{
    GOT(numbers[i]);
}
}
return 0;
}
