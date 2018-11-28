#include<iostream>
#include<cstdlib>
#include<fstream>
#include<cstdlib>
using namespace std;
int war(double *a,double *b,int n)
{
int i=0;
   while(a[0]<b[n-1])
   {
       i++;
       int flag=0;
       srand(i+6);
       int t1=rand()%n;
       // cout<<"\nValue is  "<<t1<<"  "<<a[t1]<<"  "<<b[n-1]<<" "<<n<<"\n";
       int j=0;
       while((j<n) &&(j>=0) && (a[0]<b[n-1]))
       {
           if (flag==1)
            break;
           if (a[t1]>b[j])
           {
               j++;
           }
           else
           { // cout<<"\nlarger val at "<<j<<"  "<<b[j];
               for(int k=t1;k<n-1;k++)
                a[k]=a[k+1];
          // cout<<"\ndssfdf"<<a[n-3]<<"  "<<n-2;
               for(int k=j;k<n-1;k++)
                b[k]=b[k+1];
                n--;
                flag=1;
           }
       }
   }
   return n;
}

int dwar(double *a,double *b,int n)
{
    int p=0;
    for(int i=0,j=0;i<n;i++)
    {
        if(a[i]>b[j])
        {
            p++;
            j++;
        }
    }
    return p;
}
int split(double *a,int i,int j);
void qsort(double *a,int i,int j)
{
    if (i<j)
    {
    int s=split(a,i,j);
    qsort(a,i,s-1);
    qsort(a,s+1,j);
    }
}
int split(double *a,int i,int j)
{
    int p=i;
    double r=a[j];
    int q=j-1;
    double t;
    while(q>=p)
    {
	while( a[p] <r)
	  p++;

    while ( a[q]>= r )
        q--;
	if (p<q)
	  {
	    t=a[q];
  	    a[q]=a[p];
	    a[p]=t;
	  }
    }
   t=a[j];
   a[j]=a[p];
   a[p]=t;
   return p;
}
int main()
{
    fstream f1,f2;
    int i,j,k,n1,n2;
    double *a,*b,*c,*d,m,n3;
    f1.open("D-large.in",ios::in);
    f2.open("ans4.txt",ios::out);
    f1>>n1;
    for(int k=0;k<n1;k++)
        {
            f1>>n2;
            a=new double[n2];
            b=new double[n2];
            c=new double[n2];
            d=new double[n2];
            for(int i=0;i<n2;i++)
            {
                f1>>n3;
                a[i]=n3;
                c[i]=n3;
               // cout<<a[i]<<" ";
            }
            // cout<<"\n";
            for(int i=0;i<n2;i++)
            {
                f1>>n3;
                b[i]=n3;
                d[i]=n3;
                //cout<<b[i]<<" ";
            }
            qsort(a,0,n2-1);
            qsort(b,0,n2-1);
            qsort(c,0,n2-1);
            qsort(d,0,n2-1);
           int c1= war(a,b,n2);
           // cout<<"  count  "<<c1;
           int d1=dwar(c,d,n2);
           f2<<"Case #"<<k+1<<": ";
           f2<<d1<<" "<<c1<<endl;
        delete []a;
        delete []b;
        delete []c;
        delete []d;
        }

    f1.close();
    f2.close();
    return 0;
}
