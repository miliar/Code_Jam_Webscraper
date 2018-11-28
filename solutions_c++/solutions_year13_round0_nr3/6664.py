#include <iostream>
#include<math.h>

using namespace std;

int palin( long long n)
{    int num=0,i=0,k[100];
    if (n<10)
    return 1;
    else
    {
        while(n!=0)
        {
            k[i++]=n%10;
            n=n/10;
          }
        int  flag=1;
          for(int j=i-1,l=0;j>=0;j--,l++)
          {
             if(k[j]!=k[l])
             {
                 flag=0;
                 break;
             }
             else
             continue;
          }
          if(flag)
          {return 1;
          }

          else
          return 0;

    }
}

int alg(long long lb,long long up) {



      int count=0;
      for (long i=lb;i<=up;i++)
           {
               if(palin(i))
                 if(sqrt(i)==ceil(sqrt(i)))
                      if(palin(sqrt(i)))
                       count++;
               }

           return count;
           }



     int main() {
    int n_cases;
    cin >> n_cases;
     long long a,b;
     int count[n_cases];
    for (int test_case = 0; test_case < n_cases; test_case++)
    {
        cin>>a>>b;
        count[test_case]=alg(a,b);
    }
    for(int i=0;i<n_cases;i++)
        cout << "Case #" << i +1<< ": "<<count[i]<<endl;

    }

