#include<iostream>
using namespace std;

int main()
{
    int t;
   cin>>t;
 // t = 200;  
    for (int ii = 1; ii <= t; ii++)
    {
        cout<<"Case #"<<ii<<": ";
    
    int a[101] ={0}, b[101] ={0};
    int n, p;
    int k = 10;
    bool u[10] = {0};
    cin>>n;
//  n= ii;  
    if(n == 0)
    {
        cout<<"INSOMNIA";
        //return 0;
    }
    else
    {
        while (n > 0)
        {
            a[0]++;
            a[a[0]] = n%10;
            b[0] ++;
            b[b[0]]= n%10;
            if(!u[n%10])
            {
                u[n%10] = 1;
                k--;
            }
            n = n/10;
        }
        
        while(k > 0)
        {
            p = 0;
            for (int i = 1; i<=a[0]; i++)
            {
                p += a[i] + b[i];
                a[i] = p%10;
                if(!u[a[i]])
                {
                    u[a[i]] = 1;
                    k--;
                }
                p = p/10;
            }
            if(p > 0)
            {
                a[0]++;
                a[a[0]] = p;
                if(!u[p])
                {
                    u[p] = 1;
                    k--;
                }
                p = p/10;
            }
            
      //  for (int i = a[0]; i>0; i--)
        //cout<<a[i];
    //    cout<<'\n';
        }
    }
    for (int i = a[0]; i>0; i--)
        cout<<a[i];
    cout<<'\n';
    }
    return 0;
}