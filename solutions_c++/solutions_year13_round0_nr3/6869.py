#include<iostream.h>
#include<fstream.h>
#include<math.h>
#include<conio.h>

using namespace std;
bool pald(long long int num)
{
      long long int n = num;
      long long int rev = 0;
      int dig;
      while (n > 0)
       {
      dig = n%10;
      rev = rev*10 + dig;
      n/=10;
       }
     if(num==rev)return true;
     else return false;
}      
int main()
{
    ifstream f;
    ofstream ans;
    f.open("input.txt");
    ans.open("output.txt");
    int t,a,b;
    f>>t;
    for(int i=1;i<=t;i++)
    {
            f>>a>>b;
            int c=0;
            a=ceil(sqrt(a));
            b=sqrt(b);
            for(int k=a;k<=b;k++)
            {
                    if(pald(k))
                               {
                                    if(pald(k*k))c++;
                                    
                               }
            }
            ans<<"Case #"<<i<<": "<<c<<endl;
    }
    getch();
}
