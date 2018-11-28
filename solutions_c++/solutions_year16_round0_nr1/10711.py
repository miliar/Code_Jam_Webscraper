#include<cstdio>
#include<vector>

using namespace std;

vector<bool> all_true(10,true);
int main()
{
    long long int T,N,i,ANS;
    void ck(long long int N,vector<bool> &ch);
    scanf("%lld",&T);
    for(i=0;i<T;++i)
    {
        scanf("%lld",&N);

        ANS=0;
        vector<bool> check(10,false);
        do
            {
                if(N==0)
                    break;
                ANS+=N;
                ck(ANS,check);
            }while(check!=all_true);

        printf("Case #%lld: ",i+1);
        if(N==0)
            printf("INSOMNIA\n");
        else
            printf("%lld\n",ANS);
    }
    return 0;
}

 void ck(long long int N,vector<bool> &ch)
        {
            int temp;
            do
            {
                temp=N%10;
                N=N/10;
                ch[temp]=true;
            }while(N!=0);
        }
