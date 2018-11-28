#include<fstream>
#include<iostream>
#include<string>
#include<cstring>
using namespace std;
void sor(long a[],long n)
{
        long count1;long count2;long count3;long i;
        count1=0;count2=0;count3=0;i=0;
        long array1[n];
        long array3[n];
        long array2[n];
        if (n>1)
        {
            for(i=0;i<n;i++)
            {
                if (a[i]>a[0])
                {
                    array1[count1]=a[i];
                    count1++;
                }
                else if (a[i]<a[0])
                {
                    array3[count3]=a[i];
                    count3++;
                }
                else
                {
                    array2[count2]=a[i];
                    count2++;
                }
            }
            sor(&array1[0],count1);
            sor(&array3[0],count3);
            for (i=0;i<count1;i++)
            {
                a[i]=array1[i];
            }
            for (i=i;i<count1+count2;i++)
            {
                a[i]=array2[i-count1];
            }
            for (i=i;i<n;i++)
            {
                a[i]=array3[i-count1-count2];
            }
        }
}
long c(long mote[],long N,long A)
{
    if(N<=1){return(mote[0]<A?0:1);}
    else
    {
        if (mote[N-1]<A){return(c(mote,N-1,A+mote[N-1]));}
        else
        {
            long co=(c(mote,N,2*A-1)+1);
            return(co<N?co:N);
        }
    }
}
int main()
{
char str[30];
cin>>str;
fstream fi,fo;
fi.open(str,fstream::in);
fo.open("output.txt",fstream::out);long T;
fi>>T;
for(long k=0;k<T;k++)
{
   float A;long N;
   fi>>A;fi>>N;
   long a[N];
   for (long i=0;i<N;i++){fi>>a[i];}
   sor(a,N);
   fo<<"Case #"<<k+1<<": "<<(A==1?N:c(a,N,A))<<endl;
}
fi.close();
fo.close();
return (0);
}
