#include <bits/stdc++.h>

using namespace std;
#define ll long long

ll n,j;
#define set vector
#define insert push_back
vector < string > answer;
#define MAX 100000000
string temp;
ll totalprinted=0;
bool prime[MAX+3];

void sieve(ll n)
{
    memset(prime, true, sizeof(prime));

    for (ll p=2; p*p<=n; p++)
    {
        if (prime[p] == true)
        {
            for (ll i=p*2; i<=n; i += p)
                prime[i] = false;
        }
    }
  

}

bool isprime(ll n)
{
  if(n==1||n==0)
    return 0;
  if(n==2)
    return 1;
  if(n%2==0)
    return 0;
  for(ll i=3;i*i<=n;i+=2)
    if(n%i==0)
      return 0;
  return 1;  

}

 bool isvalid(string error)
{
 // cout<<"inside isvalid\n";
  ll value=0;
  for(ll bases=2;bases<=10;bases++)
  {
    value=0;
    ll power=1;
    for(ll i=n-1;i>=0;i--)
    {
      value+=(error[i]-'0')*power;
      power*=bases;
    }
    /*if(value<MAX)
       {if(prime[value]==true)
        return 0;
      }
      else*/
       {
        if(isprime(value))
          return 0;
      }
  }

  return 1;
}


void check(string temp)
{ //cout<<"check str is "<<temp<<endl;
   if(totalprinted<=j&&isvalid(temp))
    {
   //   cout<<"inside if of isvalid\n";
      answer.push_back(temp);
      totalprinted++;
    }
}

ll hello=0;

void generate(ll pos);

void printdivisor(ll value)
{
  for(ll i=2;i<=value;i++)
    if(value%i==0)
      {cout<<i<<" ";return;}
}

void printer(string error)
{
  ll value=0;
  for(ll bases=2;bases<=10;bases++)
  {
    value=0;
    ll power=1;
    for(ll i=n-1;i>=0;i--)
    {
      value+=(error[i]-'0')*power;
      power*=bases;
    }
    printdivisor(value);

   }

}

int main()
{
  //sieve(MAX);

  ll t;
  cin>>t;
  for(ll cases=1;cases<=t;cases++)
  {
    printf("Case #%lld:\n",cases );
    answer.clear();
    totalprinted=0;
    temp="";
    cin>>n;
    cin>>j;
    for(ll i=0;i<n;i++)
      temp+='0';
    generate(0);
   
   // cout<<"total ans valid is "<<answer.size()<<endl;
    
    for(ll i=0;i<j;i++,cout<<endl)
      {cout<<answer[i]<<" ";printer(answer[i]);}

  }
  return 0;
}

void generate( ll pos)
{
  if(totalprinted>j)
    return;
  if(pos<n-1&&pos>0)
  {
    //cout<<hello++<<" "<<pos<<endl;
    temp[pos]='0';
    generate(pos+1);
    //check(temp);
    temp[pos]='1';
    generate(pos+1);
    //check(temp);
  }
  else if(pos==n-1)
  {
    temp[pos]='1';
    check(temp);
   }
   else if(pos==0)
   {
   temp[pos]='1';
   generate(1);
   }

}
