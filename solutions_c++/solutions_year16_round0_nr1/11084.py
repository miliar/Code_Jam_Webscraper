#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,j;
    scanf("%d",&t);
    for(j=1;j<=t;j++)
    {
        long long n;
        scanf("%lld",&n);
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",j);
        }
        else
        {
            set<int> s;
            long long int temp,k,i=2,l,ck;
            l = n;
            while(s.size()<10)
            {


                temp = n;

                while(temp != 0)
                {
                    //cout<<temp<<" "<<k<<endl;
                    k = temp%10;
                    s.insert(k);
                    temp /=10;

                }

                ck = l*i;
                if(n==ck){
                 printf("Case #%d: INSOMNIA\n",j);
                 break;
                }
                n = ck;
                i++;


            }

            printf("Case #%d: %lld\n",j,n-l);

        }

    }

}
