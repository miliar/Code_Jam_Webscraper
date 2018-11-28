#include <cstdio>
using namespace std;
short nrm,j;
int v[101];
void quicksort(int v[], int stanga, int dreapta)
{
   int i, j, mijloc, aux;         // variabilele
   i=stanga;                       //  initializarea
   j=dreapta;                    //   indicilor
   mijloc=v[(stanga+dreapta)/2];  // initializarea variabilei - pivot
  while(i<=j)
  {
   while(v[i]<mijloc)  // apropierea i-ului de mijloc
      ++i;
   while(v[j]>mijloc)   // apropierea j-ului de mijloc
      --j;
    if(i<=j)   //conditia efectuarii operatiei de interschimbare
    {
       aux=v[i];
       v[i]=v[j];   // operatia de interschimbare
       v[j]=aux;
       ++i;
       --j;
     }
  }
 if(stanga<j)                    //recursivitatea
   quicksort(v, stanga, j);   // in partea stanga
 if(i<dreapta)
   quicksort(v, i, dreapta);  // in partea dreapta

}
void back(int a,short q,short w,short nr)
{
    if (q==0)
    {
        a+=v[w];
        if (w<j)
        {
            if (a>v[w+1]) back(a,0,w+1,nr);
            else
            {
                back(a,1,w+1,nr);
                back(a,2,w+1,nr);
            }
        }
        else if (nr<nrm) nrm=nr;
    }
    else if (q==1)
    {
        a=(a<<1)-1;
        ++nr;
        if (a>v[w]) back(a,0,w,nr);
        else
        {
            back(a,1,w,nr);
            back(a,2,w,nr);
        }
    }
    else
    {
        ++nr;
        if (w<j)
        {
            if (a>v[w+1]) back(a,0,w+1,nr);
            else
            {
               if (a!=1) back(a,1,w+1,nr);
                back(a,2,w+1,nr);
            }
        }
        else if(nr<nrm) nrm=nr;
    }

}
int main()
{
    FILE * in, *out;
    short k,n,i,T;
    int a,x;
    in=freopen("A-small-attempt2.in","r",stdin);
    out=freopen("out.out","w",stdout);
    scanf("%hd",&T);

    for(k=1;k<=T;++k)
    {
        nrm=101;
        scanf("%d%hd",&a,&n);
        j=0;
        for(i=0;i<n;++i)
        {
            scanf("%d",&x);
            if (x<a) a+=x;
            else
            {
                v[j]=x;
                ++j;
            }
        }
        quicksort(v,0,j-1);
        --j;
        if (j>=0) {
            if (a>v[0]) back(a,0,0,0);
            else
            {
              if (a!=1) back(a,1,0,0);
                back(a,2,0,0);
            }
        }
        if (nrm==101) nrm=0;
        printf("Case #%hd: %hd\n",k,nrm);

    }
    fclose(in);
    fclose(out);
    return 0;
}
