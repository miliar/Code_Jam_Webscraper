#include <iostream>
#include <fstream>
using namespace std;
void quicksortf(float a[],int l,int r)
{
     int i,j;
     float x;
     if(l>=r) return;
     i=l;
     j=r;
     x=a[i];
     while(i!=j)
     {
          while(a[j]>x&&j>i) j--;
          if(i<j)
            {
                 a[i]=a[j];
                 i++;
            }
          while(a[i]<x&&j>i) i++;
          if(i<j)
             {
                 a[j]=a[i];
                 j--;
             }
     }
     a[i]=x;
     quicksortf(a,l,j-1);
     quicksortf(a,i+1,r);
}

int main()
{
    ofstream fout("c:\\me5.txt");
    ifstream fin("c:\\D-large.in");
    int i,j,m,p;
    int num,n;
    float naomi[1000],ken[1000];
    int counter[1000];
    int max,min;
    fin>>n;
    for(m=0;m<n;m++)
    {
    fin>>num;

    for(i=0;i<num;i++)
    {
        fin>>naomi[i];


    }
    for(i=0;i<num;i++)
    {
        fin>>ken[i];
    }
    quicksortf(naomi,0,num-1);
    quicksortf(ken,0,num-1);


    max=0;min=1000;
    for(i=0;i<num;i++)
    {
        counter[i]=0;
        for(j=0;j<num;j++)
        {
            p=(i+j)%num;

            if(naomi[p]>ken[j])
            counter[i]++;
        }
    }

    for(i=0;i<num;i++)
    {
        if (counter[i]>max)
        max=counter[i];
        if(counter[i]<min)
        min=counter[i];

    }

    fout<<"Case #"<<m+1<<": "<<max<<" "<<min<<endl;
    }


}
