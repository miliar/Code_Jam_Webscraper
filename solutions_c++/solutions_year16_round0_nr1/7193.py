#include<bits/stdc++.h>

using namespace std;
#define ll long long int

int main()
{
    ifstream cin("A-large.in");
    ofstream cout("b.txt");

    ll t;
    cin >> t;
    int arr[10];
    int counter=1;
    while(t--)
    {
        int dig =0; // keeping tarck of the digits that have occured
        for(int j=0;j<10;j++) arr[j]=0;
        ll n;
        cin >> n;
        if(n==0) // when n=0
        {
            cout << "Case #" <<counter<<": INSOMNIA"<< "\n";
        }
        else{
        int i=1; ll x;
        while(dig != 10) // loop till all the digits have not occured
        {
            x=i*n;
            while(x>0) // run till the no becomes zero
            {

                int rem=x%10;   // take out the last digit
                if(arr[rem]==0) //check if the digit have occured or not
                {
                    dig=dig+1;
                    arr[rem]=1;
                }
                x=x/10;
            }
            i++;
        }
        cout << "Case #" <<counter<<": "<< (i-1)*n << "\n";
        }
        counter++;
    }
    return 0;
}
