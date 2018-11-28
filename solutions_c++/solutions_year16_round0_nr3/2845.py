#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    long long int t,sv,n,j;
    long long int ct,num,ind;//b2,b3,b4,b5,b6,b7,b8,b9,b10,num,ind;
    char str[18];
    long long int fac[11];
    scanf("%lld",&t);
    sv=t;

    while(t--)
    {
        ct=0; //cout<<"ash\n";
        scanf("%lld%lld",&n,&j);

        str[0]='1';
        str[n-1]='1';
        str[n]='\0';
        for(long long int i=1;i<n-1;i++)
        str[i]='0';

        printf("Case #%lld:\n",sv-t);

        //b2=pow(2,n-1)+1;
        //b3=pow(3,n-1)+1;
        //b4=pow(4,n-1)+1;
        //b5=pow(5,n-1)+1;
        //b6=pow(6,n-1)+1;
        //b7=pow(7,n-1)+1;
        //b8=pow(8,n-1)+1;
        //b9=pow(9,n-1)+1;
        //b10=pow(10,n-1)+1;

        while(1)
        {
            memset(fac,-1,sizeof(fac));
            for(long long int i=2;i<=10;i++)
            { //cout<<"ash\n";
                num=0;
                ind=0;
                for(long long int jp=n-1;jp>=0;jp--)
                { //cout<<"ash\n";
                    num=num+(pow(i,ind)*(str[jp]-'0'));
                    ind++;
                } //cout<<num<<"\n";
                for(long long int qp=2;qp<=sqrt(num);qp++)
                { //cout<<"ash\n";
                    if(num%qp==0)
                    {
                        fac[i]=qp;
                        break;
                    }
                }
            }

            int fl=0;
            for(int lp=2;lp<=10;lp++)
            {
                if(fac[lp]==-1)
                {
                    fl=1;
                    break;
                }
            }

            if(fl==0)
            {
                printf("%s",str);

                for(int op=2;op<=10;op++)
                printf(" %lld",fac[op]);
                printf("\n");

                ct++;
                if(ct==j)
                break;
            }

            int bn=n-2;
            char cr='1';
            while(bn>=1)
            { //cout<<"ash\n";
                if(str[bn]=='0')
                { //cout<<"ash\n";
                    str[bn]='1';
                    cr='0';
                    break;
                }
                else
                {
                    str[bn]='0';
                    cr='1';
                }
                bn--;
            }
        }
        //cout<<"ash\n";
    }

    return 0;
}
