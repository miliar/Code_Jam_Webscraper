#include <iostream>

using namespace std;

int main()
{
   int T,t;
   cin>>T;
  for(int t=1;t<=T;t++)
  {
    int j,k,l;
    int i;
        int N;
            cin>>N;
        if(N==0)
        { cout<<"Case #"<<t<<": INSOMNIA"<<endl;
        continue;
        }

        string sting = "nnnnnnnnnn";

        for(k=1;sting!="yyyyyyyyyy";k++)
        {
            int n;
            n=N*k;

            while(n!=0)
            {
                i = n%10;
                sting[i]='y';
                n=n/10;
             }
        }
        k--;
        cout<<"Case #"<<t<<": "<<N*k<<endl;
  }
    return 0;
}
