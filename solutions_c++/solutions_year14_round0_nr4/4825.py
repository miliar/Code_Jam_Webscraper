#include<iostream>
using namespace std;
#include<algorithm>

float n[1001],k[1001];
int main()
{
    int t,s;
    cin>>t;
    for(s=1;s<=t;s++)
    {
       int no,i,j;
       cin>>no;
       for(i=0;i<no;i++)
           cin>>n[i];


        for(i=0;i<no;i++)
         cin>>k[i];

        sort(n,n+no);
        sort(k,k+no);

        int np=0,kp=0,npd=0,kpd=0;
        for(i=0,j=0;i<no&&j<no;)
        {
            if(n[i]<k[j])
            {
                kp++;
                i++;
                j++;
            }
            else
            {
                j++;
            }

        }
        np=no-kp;
         for(i=0,j=0;i<no&&j<no;)
        {
            if(n[i]>k[j])
            {
                i++;
                j++;
                npd++;
            }
            else
            {
                i++;
            }

        }
        cout<<"Case #"<<s<<":"<<" "<<npd<<" "<<np<<"\n";
    }
}
