#include<iostream>
#include<fstream>
#include<algorithm>
using namespace std;

int main()
{

    ifstream input("input.txt");
    ofstream output("output.txt",ios::trunc);
   int t,x,n;
   double ar1[1000],ar2[1000];
   input>>t;
   for(x=1;x<=t;x++)
   {
       input>>n;
       for(int i=0;i<n;i++)
        input>>ar1[i];
        for(int i=0;i<n;i++)
        input>>ar2[i];
        sort(ar1,ar1+n);
        sort(ar2,ar2+n);
        /*for(int i=0;i<n;i++)
        {
            cout<<ar1[i]<<" ";
        }*/
        //decietful
        int i=0,j=n-1,k=n-1,c=0;
        while(k>=0)
        {
            if(ar1[j]>ar2[k])
            {
                c++;
                j--;
                k--;
            }
            else
            {
              k--;
            }
        }
        //war
        int c2=0;
        i=0,j=n-1,k=n-1;
        while(j>=0)
        {
            if(ar1[j]>ar2[k])
            {
                c2++;
                j--;

            }
            else
            {
              j--;
              k--;
            }
        }

        output<<"Case #"<<x<<": ";
        output<<c<<" "<<c2<<endl;
        c=0,c2=0;

   }
return 0;
}


