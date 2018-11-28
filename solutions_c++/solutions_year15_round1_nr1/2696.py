#include <bits/stdc++.h>
using namespace std;


long long int a[10000];
int main()
{
     ofstream fout;

        fout.open("ans.txt");
    long long int p,n,j ;
    cin>>p;
    long long int i;


    for(i=0;i<p;i++)
    {
        cin>>n;
        for(j=0;j<n;j++)
        {   cin>>a[j];
        }
        long long int sum =0;
        long long int maxi=-1;
        for(j=0;j<n-1;j++)
        {

            if(a[j]>a[j+1])
            {

                maxi=max(maxi,a[j]-a[j+1]);

                    sum+=a[j]-a[j+1];
            }



        }

        long long int pre,sum2;
        pre=0; sum2=0;
      for(j=0;j<n-1;j++)
      {
          if(a[j]<maxi)
          {

              sum2+=a[j];
              pre=0;

          }
          else if(a[j]>maxi)
          {

              sum2+=maxi;


          }
          else if(a[j]==maxi)
          {

              sum2+=maxi;

          }

      }

        if(sum2<0)
            sum2=0;




                   cout<<sum<<" "<<sum2<<"\n";
                   fout<<"Case #"<<i+1<<": "<<sum<<" "<<sum2<<"\n";









    }





}
