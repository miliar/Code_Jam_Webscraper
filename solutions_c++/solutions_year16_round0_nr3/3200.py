#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("TasO.txt","r",stdin);
    freopen("tas_o.txt","w",stdout);
    long long n=1,f,i,r,j;
    long long str;
    cout << "Case #1:\n";
    while(n<=50)
    {
        n++;
        //cin >> str;
        //cout << str << endl;
        //cout<< "This is "  << n << endl;
        for(j=1; j<=10; j++)
        {
            cin>> r;
            if(j==1)
            {
                cout << r << " ";
            }
            else
            {
                f=0;
                  for(i=2; i*i<=r; i++)
                {
                    if(r%i==0)
                    {
                        f=1;
                        cout << r/i << " ";
                        break;
                    }
                }
                if(f==0)
                    cout << "-1 " ;
            }

        }
        cout << endl;
    }
}
