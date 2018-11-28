#include<bits/stdc++.h>
using namespace std;

//return -1 if x is prime
//return a divisor of x if x is non-prime
long long int isPrime(long long int x)
{
    if(x<2)
        return x;

    //2 is prime
    if(x==2)
        return -1;

    //even number
    if(x%2==0)
        return 2;

    long long int i,j,y;

    for(i=3;i<=sqrt(x);i+=2)
    {
        if(x%i==0)
            return i;
    }
    
    return -1;
}

//string of length n of least value eligible for jamcoins
string getMin(int n)
{
    string str(n,'0');
    str[0]='1';
    str[n-1]='1';

    return str;
}

//get next eligible string of length n
string getNext(string str, int n)
{
    int i=n-2;

    while(str[i]=='1' && i>0)
    {
        str[i]='0';
        i--;
    }

    //out of range
    if(i==0)
    {
        str[0]='0';

        return str;
    }

    str[i]='1';

    return str;
}

int main()
{
    //freopen("in2.in","r",stdin);
    //freopen("out2.out","w",stdout);

    long long int i,j,k;
    long long int n,x,y,z,a,b,c;

    int t;
   
    string str,str2;
    vector<long long int> div(11);
    bool prime;

    cin>>t;

    int cs=1;

    while(t--)
    {
        cin>>n>>j;

        cout<<"Case #"<<cs<<": "<<endl;
        
        str=getMin(n);

        i=0;

        while(i<j)
        {
            bool prime=false;
            //check if this string is non-prime
            

            k=2;
            while(!prime && k<=10)
            {
                //get the base k integer equivalent of str
                y=stoll(str,nullptr,k);

                //this will return a divisor of x, if y is non-prime
                //if y is prime, it will return -1
                x=isPrime(y);

                if(x==-1)
                {
                    //this is a prime
                    prime=true; 

                    str=getNext(str,n);
                }

                else
                {
                    div[k]=x;
                }

                k++;
            }

            if(prime==false)
            {
                //we got a jamcoin
                //now, print it
               
                cout<<str<<" ";

                for(int abc=2;abc<=10;abc++)
                {
                    cout<<div[abc]<<" ";    
                }

                cout<<endl;

                str=getNext(str,n);

                i++;
            }
        }

        cs++;
    }
   
    return 0;
}
