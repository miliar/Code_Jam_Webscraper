#include <iostream>
#include<cstdio>
#include<cmath>

using namespace std;

int main()
{
    FILE* in= fopen("C:\\мои файлы\\олимпы\\GoogleCodeJam2016\\квалификация\\A-large.in", "r");
    FILE* out= fopen("C:\\мои файлы\\олимпы\\GoogleCodeJam2016\\квалификация\\A-large.out", "w");
    int T;
    fscanf(in,"%d",&T);
    for(int num=1;num<=T;num++){
        long long n;
        fscanf(in,"%I64d",&n);
        if(n==0) fprintf(out,"Case #%d: INSOMNIA",num);
        else{
            int a[10];
            for(int i=0;i<10;i++) a[i]=0;
            bool fl=false;
            long long i=n;
            while(i<=max(n*n,n*10000) && !fl)
            {
                long long ci=i;
                while(ci>0){a[ci%10]++;ci=ci/10;}
                fl=true;
                for(int j=0;j<10 && fl;j++) if(!a[j]) fl=false;
                if(!fl) i+=n;
            }
            if(fl) fprintf(out,"Case #%d: %I64d",num,i);
            else fprintf(out,"Case #%d: INSOMNIA",num);
        }
        fprintf(out,"\n");
    }
    fclose(out);
    return 0;
}

