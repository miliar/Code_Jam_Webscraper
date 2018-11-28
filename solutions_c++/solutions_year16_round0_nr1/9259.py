#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <cstdlib>
#include <iostream>
#include <math.h>
#include <stack>
using namespace std;
typedef long long ll;


#include <cstdlib>
#include <iostream>
#include <math.h>
#include <stack>

ll countDigitsInInteger(ll n)
{
    ll count =0;
    while(n>0)
    {
        count++;
        n=n/10;
    }
    return count;
}

using namespace std;

int main(int argc, char *argv[])
{

    int arr[10];
    for(int a=0;a<10;a++){
        arr[a]=0;
    }
    
    FILE *fin = freopen("A-Large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("A-large.out", "w", stdout);
    ll T;
    cin >> T;
    for(ll t = 1; t <= T; t++){
        ll a;
        cin>>a;

        for (ll i=1;i<10000000;i++){
            if (a==0){
                cout<<"Case #" << t << ": INSOMNIA "<<endl;
                break;
            }
            ll number=a*i;
            ll track=number;
            ll intLength =0;
            ll digit;
            string s;
            
            intLength = countDigitsInInteger(number);
        
            stack<ll> digitstack;
            while(number>0)
            {
                digit = number % 10;
                number = number / 10;
                digitstack.push(digit);
            }
            
            while(digitstack.size() > 0)
            {
                arr[digitstack.top()]=1;
//                cout<<"top is"<<digitstack.top();
                digitstack.pop();
            }

            if (arr[0]==1&&arr[1]==1&&arr[2]==1&&arr[3]==1&&arr[4]==1&&arr[5]==1&&arr[6]==1&&arr[7]==1&&arr[8]==1&&arr[9]==1){
            cout << "Case #" << t << ": ";
            cout << track<< endl;
                for(int a=0;a<10;a++){
                    arr[a]=0;
                }
            break;
            }
        }
    }
}

