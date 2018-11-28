#include <iostream>
#include <set>
#include <stdio.h>

using namespace std;

void parse(set<int>& myDigits,long long x)
{
    while(x > 0)
    {
        myDigits.insert(x%10);
        x /= 10 ;
    }
}

long long solve(long long x)
{
    set<int> myDigits ;
    long long i = 1 ;
    while(myDigits.size() < 10)
    {
        parse(myDigits , x*i++);
    }
    return (x*(i-1)) ;
}

int main()
{
    freopen("input2.in","r",stdin);
    freopen("output2.out","w",stdout);
    int test ; long long input ;
    cin >> test ;
    for(int i = 1 ; i <= test ; i++)
    {
        cin >> input ;
        cout << "Case #"<<i<<": " ;
        if(input!=0)
            cout << solve(input) << endl ;
        else cout << "INSOMNIA" << endl ;
    }
    return 0;
}
