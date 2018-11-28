#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

typedef long long ll;

int main()
{

    freopen("ain.txt","r",stdin);
    freopen("aout.txt","w",stdout);
    int test_case, T;
    scanf("%d" , &T);
    for(test_case=1;test_case<=T;test_case++)
    {
        printf("Case #%d: " , test_case);
        int i,j;
        int N;
        scanf("%d" , &N);
        bool X[10];
        for(i=0;i<10;i++)
        {
            X[i]=false;
        }
        if(N==0)
        {
            printf("INSOMNIA\n");
            continue;
        }
        int num=0;
        for(i=1;;i++)
        {
            int tmp=i*N;
            while(tmp!=0)
            {
                if(!X[tmp%10])
                {
                    X[tmp%10]=true;
                    num++;
                }
                tmp=(tmp/10);
            }
            if(num==10)break;

        }
        printf("%d\n" , i*N);



    }



    return 0;

}
