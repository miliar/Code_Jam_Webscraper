#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long int r,tmp;

    int t,N;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        cin>>N;
        if(N==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }
        else
        {
            int chk[11];
            memset(chk, 0, sizeof chk);
            for(int j=1; j<100; j++)
            {
                r = N*j;
                while (r > 0)
                {
                    chk[r%10] = 1;
                    r = r / 10;
                    if(chk[0]==1 && chk[1]==1 && chk[2]==1 && chk[3]==1 && chk[4]==1 && chk[5]==1 && chk[6]==1 && chk[7]==1 && chk[8]==1 && chk[9]==1)
                    {
                        cout<<"Case #"<<i<<": "<<N*j<<endl;
                        j=100;
                        break;

                    }
                }
            }

        }
    }
}
