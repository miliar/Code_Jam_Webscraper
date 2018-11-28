//created by shikhar vishnoi

#include <iostream>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <string.h>
#include <math.h>
#define ll long long
#define pb push_back
#define iosync ios_base::sync_with_stdio(false);cin.tie(0);
const ll mod=1000000007;
const double pi=3.14159265358979323846;
using namespace std;

string digits[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int cont[10],alpha[26];

void f(char x,int d)
{
    cont[d]=alpha[x-'A'];
    string s = digits[d];
    for (int i = 0; i < s.size(); ++i)
    {
        alpha[s[i]-'A'] -= cont[d];
    }
}

int main ()
{
    
    // freopen("input.txt", "r", stdin); 
    // freopen("output.txt", "w", stdout);
    iosync
    ll T;
    cin>>T;
    for(ll t=1;t<=T;t++)
    {
        memset(cont,0,sizeof(cont));
        memset(alpha,0,sizeof(alpha));
        string s;
        cin>>s;
        for (int i = 0; i < s.size(); ++i)
        {
            alpha[s[i]-'A']++;
        }
        f('Z',0);
        f('W',2);
        f('U',4);
        f('X',6);
        f('G',8);
        f('H',3);
        f('F',5);
        f('V',7);
        f('O',1);
        f('I',9);
        cout<<"Case #"<<t<<": ";
        for (int i = 0; i < 10; ++i)
        {
            for (int j = 0; j < cont[i]; ++j)
            {
                cout<<i;
            }
        }
        cout<<endl;
    }
    return 0;
}