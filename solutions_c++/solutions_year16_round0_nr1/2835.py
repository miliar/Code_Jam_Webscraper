#include<bits/stdc++.h>

using namespace std;

#define f(i, a, b) for(int i=a; i<=b; i++)

bool visto[15];

int main()
{
    int T, n, k;
    cin>>T;

    f(t, 1, T)
    {
        cin>>n;
        if(n==0)
            cout<<"Case #"<<t<<": INSOMNIA"<<endl;
        else
        {

            f(i, 0, 9)
            visto[i]=false;

            for(k=1; ; )
            {
                int x = k*n;
                for(; x>0 ; )
                {
                    visto[x%10]=true;
                    x/=10;
                }


                bool parar = true;
                f(i, 0, 9)
                {
                    if(!visto[i])
                    {
                        parar = false;
                        break;
                    }
                }

                if(parar)
                    break;
                k++;

            }
            cout<<"Case #"<<t<<": "<<k*n<<endl;
        }
    }



    return 0;
}
