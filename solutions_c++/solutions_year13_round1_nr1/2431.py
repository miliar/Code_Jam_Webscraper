// Jai Mata Di
#include <iostream>
using namespace std;
int main(int argc, char *argv[])
{
int c;
cin>>c;
for(int i=1;i<=c;i++)
{
    long long r,t;
    cin>>r>>t;
//    long long a = t*3.1415926;
  //  long long a = t;

    long long noOfRings = 1;
    long long s = r + r + 1;
    long long f = s + 4;
    while(true)
    {
            //   cout<<"s="<<s<<endl;
               s = s + f;
               f = f + 4;
            if(s > t)
                 break;
            noOfRings++;
//            r+=2;
    }
    cout<<"Case #"<<i<<": "<<noOfRings<<endl;
} 
   return 0;
}
