#include<bits/stdc++.h>

using namespace std;

main()
{
    long long int T,N,P,tst=1,j;
    vector<long int>a;
    a.resize(10);
    FILE *in,*out;
    in=fopen("inputalarge.txt","r");
    out=fopen("outputalarge.txt","w");
    fscanf(in,"%lld",&T);

    while(T--)
    {
        fscanf(in,"%lld",&N);
        int dcs=0;
        for(int i=0;i<10;i++)
            a[i]=0;
        if(N==0){
            fprintf(out,"Case #%lld: INSOMNIA\n",tst++);
            }
        else{
        int cnt=1;
        while(1)
        {

            P=(N*cnt);
            while(P!=0)
            {
                a[P%10]=1;
                P/=10;
            }

            for(j=0;j<10;j++)
            {
                if(a[j]==0)
                {
                    dcs=0;
                    break;
                }
            }
            if(j==10)
            {
                fprintf(out,"Case #%lld: %lld\n",tst++,(cnt*N));
                break;
            }
            cnt++;
        }}
    }
    fclose(in);
    fclose(out);
    return 0;
}
