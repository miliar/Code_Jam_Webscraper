#include <iostream>
#include<cmath>
#include<cstdio>
#include<cstring>

using namespace std;

int main()
{
    int i,n,k=0;
    double r,c,f,t,s,ss,p,pp,fin,te,tee;
    FILE *q;
    q=fopen("suraj1.txt","w");

    scanf("%d",&n);
    while(n--)
    {
       cin>>c>>f>>t;
       s=ss=p=pp=0.0;
       r=2.0;
       if(c>t){
            fin=t/r;
       }
        else
        {
            while(1)
            {
                te=s;
                tee=p;
                s+=(c/r);
                p=(t/(r+f));
                ss=(s+(c/(r+f)));
                pp=(t/(r+f+f));

                if((p+s)<(pp+ss))
                    break;
                r+=f;

            }
            fin=s+p;
            if(fin>(t/2.0))
                fin=(t/2.0);
        }
        k++;
        fprintf(q,"Case #%d: %0.7lf\n",k,fin);
    }
    fclose(q);
    return 0;
}
