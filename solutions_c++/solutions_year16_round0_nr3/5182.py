/* itoa example */
#include <bits/stdc++.h>
using namespace std;
#define ll long long
string decm(int number)
{
    string result = "";

    do
    {
        if ( (number & 1) == 0 )
            result += "0";
        else
            result += "1";

        number >>= 1;
    } while ( number );

    reverse(result.begin(), result.end());
    return result;
}
ll conver(ll num,ll b)
{
    ll bin, dec = 0, rem, base = 1;
    cin >> num;
    bin = num;
    while (num > 0)
    {
        rem = num % 10;
        dec = dec + rem * base;
        base = base * b;
        num = num / 10;
    }
    //cout << "The decimal equivalent of " << bin << " : " << dec << endl;
    return dec;

}   
bool notprime(ll num){

    if(num < 2) return true;
    if(num == 2) return false;
    if(num % 2 == 0) return true;
    for(ll i=3; (i*i)<=num; i+=2){
        if(num % i == 0 ) return true;
    }
    return false;

}
int main ()
{
