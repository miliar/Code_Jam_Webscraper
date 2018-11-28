#include<bits/stdc++.h>
using namespace std;
long long int isPrime(long long int n)
{
     int flag=0;
     long long int i;
     for(i=2;i<=sqrt(n);++i)
     {
          if(n%i==0)
          {
              flag=1;
              break;
          }
      }
      if(flag)
      return i;
      else
      return 0;
}
long long int power(long long int x, unsigned int y)
{
    if( y == 0)
        return 1;
    else if (y%2 == 0)
        return power(x, y/2)*power(x, y/2);
    else
        return x*power(x, y/2)*power(x, y/2);

}
long long int changeBase(string s,int b)
{

    long long int k=1,p=0;
    int i;
    for(i=15;i>=0;i--)
    {
        p+=(s[i]-48)*power(b,15-i);
    }
    return isPrime(p);
}

int main()
{
    long long int l,i,ans[11];

    ifstream infile;
	infile.open("main.txt");
    printf("Case #1:\n");
    l=0;

    string str;
    while(l<50)
    {
         infile >> str;

        for(i=0;i<=10;i++)
        {
            ans[i]=0;
        }
        int flag =0;

        for(i=2;i<=10;i++)
        {
           ans[i]=changeBase(str,i);

        }
        for(i=2;i<=10;i++)
        {
            if(ans[i]==0)
            {
                flag=1;
                break;


            }
        }
        if(flag)
        {

        continue;
        }
        else
        {
            cout<<str<<" ";
            for(i=2;i<=10;i++)
            cout<<ans[i]<<" ";
            cout<<endl;
            l++;
        }


    }
    return 0;
}
