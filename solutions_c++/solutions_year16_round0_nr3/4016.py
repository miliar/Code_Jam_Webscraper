#include<bits/stdc++.h>
using namespace std;

#define M 100000000

int sf[M+1];
int prime[M+1];
int index=1;
vector<long long> psf(9);


int sieve()
{

   long long i; prime[0]=2;
  for(i=0;i<=M;i++)
      sf[i]=1;
	long long j;


  for(j=4;j<=M;j+=2)
      sf[j]=2;
  for(i=3;i*i<=M;i+=2)
  {
      if(sf[i]!=1)
        continue;
      prime[index++]=i;

      for(j=i*i;j<=M;j+=2*i)
          sf[j]=i;
  }
  for(j=i;j<=M;j+=2)
  {
      if(sf[j]==1)
         prime[index++]=j;

  }
/*
 for(i=0;i<index;i++)
     cout<<i<<"\t"<<prime[i]<<endl;
*/
}

bool isPrime(long long n)
  {
      int i;
          for(i=0;i<index;i++)
          {
          	if(n==prime[i])
          		return true;
              if(n%prime[i]==0)
                 {
                    psf.push_back(prime[i]);
                    return false;

                 }
                // cout<<i<<endl;
          }

      //cout<<n<<endl;
      return true;


  }
bool check(string s)
 {
     int i,j;
     for(i=2;i<=10;i++)
      {
      	 long long no=0;

         long long pw=1;
         for(j=s.size()-1;j>=0;j--)
           {
                if(s[j]=='1')
                    no+=pw;
                pw*=i;
           }

              if(isPrime(no)==true)
                  return false;

            /*else
                  {
                      cout<<"base "<<i<<" passed"<<endl;
                  }*/
      }
      return true;

 }
int makeEqualLength(string &str1, string &str2)
{
    int len1 = str1.size();
    int len2 = str2.size();
    if (len1 < len2)
    {
        for (int i = 0 ; i < len2 - len1 ; i++)
            str1 = '0' + str1;
        return len2;
    }
    else if (len1 > len2)
    {
        for (int i = 0 ; i < len1 - len2 ; i++)
            str2 = '0' + str2;
    }
    return len1; // If len1 >= len2
}
string addBitStrings( string first, string second )
{
    string result;  // To store the sum bits

    // make the lengths same before adding
    int length = makeEqualLength(first, second);

    int carry = 0;  // Initialize carry

    // Add all bits one by one
    for (int i = length-1 ; i >= 0 ; i--)
    {
        int firstBit = first.at(i) - '0';
        int secondBit = second.at(i) - '0';

        // boolean expression for sum of 3 bits
        int sum = (firstBit ^ secondBit ^ carry)+'0';

        result = (char)sum + result;

        // boolean expression for 3-bit addition
        carry = (firstBit & secondBit) | (secondBit & carry) | (firstBit & carry);
    }

    // if overflow, then add a leading 1
    if (carry)
        result = '1' + result;

    return result;
}
 int main()
 {
   // freopen("output.txt","w",stdout);
   sieve();
  // int t;
   //cin>>t;
   psf.clear();

   //char p[]="00000000000000";
   //long long n=1000000000000001;
   string s="1000000000000001";
   int ctr=0;
   cout<<"Case #1: "<<endl;

   //int arr[]={0,0,0,0,0,0,0,0,0,0,0,0,0,0};
while(ctr<50)
   {

       //s+="1";

       if(check(s)==true )
       {
        //cout<<"check works"<<endl;

        ctr++;
        cout<<s<<" ";
        for(int p=2;p<=10;p++)
             cout<<psf[p-2]<<" ";
             cout<<endl;
        //cout<<ctr<<"true "<<check(s)<<endl;
       // cout<<check("11")<<" for 11"<<endl;


       }
       psf.clear();

          //cout<<"IN"<<endl;

          s=addBitStrings(s,"10");
          //cout<<s<<endl;

   }

 }
