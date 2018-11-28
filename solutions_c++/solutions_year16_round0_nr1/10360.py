#include<stdlib.h>
#include<stdio.h>
#include <iomanip>
#include<string>
#include<stack>
#include<map>
using namespace std;


int main()
{
    unsigned long int n,num,numd,i,j,k,r,chk[11],cnt;
    FILE *ifp,*ofp;
    ifp=fopen("C:/Users/Ram_Krishna/Desktop/A-large.in","r");
    ofp=fopen("C:/Users/Ram_Krishna/Desktop/try.txt","w");
    fscanf(ifp,"%lu",&n);
    for(k=0;k<n;k++)
    {
        fscanf(ifp,"%lu",&num);
        cnt=10;
        if(num==0)
        {
            fprintf(ofp,"Case #%lu: INSOMNIA\n",k+1);
        }
        else
        {
            for(i=0;i<10;i++)
            {
                chk[i]=0;
            }
            i=1;
            numd=num;
            while(cnt)
            {
                if(i>1)
                {
                    numd/=(i-1);
                }
                numd*=i;
                num=numd;
                //j=10;
                while(num)
                {
                    //j*=10;
                    if(chk[num%10])
                    {
                        num/=10;
                    }
                    else
                    {
                        //cout<<num%10<<endl;
                        chk[num%10]++;
                        cnt--;
                        num/=10;
                    }
                }
                i++;

            }
            fprintf(ofp,"Case #%lu: %u\n",k+1,numd);
        }
    }
    fclose(ifp);
    fclose(ofp);
}
