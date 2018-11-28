#include<iostream>
using namespace std;

void sortdecite(float a[],int n)
{
    int i,j;
    float s;
     for(i=0;i<n;i++)
    {

      for(j=0;j<n;j++)
      {
        if(a[i]>a[j])
        {
            s=a[j];
            a[j]=a[i];
            a[i]=s;
        }
      }
    }
}
void sortasec(float a[],int n)
{
    int i,j;
    float s;
     for(i=0;i<n;i++)
    {

      for(j=0;j<n;j++)
      {
        if(a[i]<a[j])
        {
            s=a[j];
            a[j]=a[i];
            a[i]=s;
        }
      }
    }
}
class player
{
    float nomie[1000];
    float ken[1000];
    int n;
    public:
    void length()
    {
        cin>>n;
    }
    void get()
    {
        int i,j;
        for(i=0;i<n;i++)
        cin>>nomie[i];
        for(j=0;j<n;j++)
        cin>>ken[j];
    }
    int comparedecite()
    {
        int i,j,c=0;
        sortdecite(nomie,n);
        sortdecite(ken,n);

            for(i=0,j=0;j<n&&i<n;j++)
            {
                if(nomie[i]>ken[j])
               {
                 c++;
                 i++;
               }

            }


        return c;
    }
     int comparewar()
    {
        int i,j,c=0;
        sortasec(nomie,n);
        sortasec(ken,n);

            for(i=0,j=0;j<n&&i<n;j++)
            {
                if(ken[i]>nomie[j])
               {
                 c++;
                 i++;

               }
               else
               {
               i++;
               j--;
               }

            }
         return n-c;
    }
};
int main()
{
   int n,n1,i;
   cin>>n;
   player c[n];
   n1=n;
   i=0;
   while(n>0)
   {
       c[i].length();
       c[i].get();
       n--;
       i++;
   }
   i=0;
   while(n1>0)
   {
       cout<<"Case #"<<i+1<<": "<<c[i].comparedecite()<<" "<<c[i].comparewar()<<"\n";
       n1--;
       i++;
   }
   return 0;
}
