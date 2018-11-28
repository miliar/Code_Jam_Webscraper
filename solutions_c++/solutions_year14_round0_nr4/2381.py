#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
int main()
{
    freopen("D-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int t;
    cin>>t;
    int tt=0;
    while(t--)
    {
              tt++;
     int n;
     cin>>n;
     double ar1[2000],ar2[2000];
     for(int i=0;i<n;i++)
     {
             cin>>ar1[i];
     }
     for(int i=0;i<n;i++)
     {
             cin>>ar2[i];
     }
     sort(ar1,ar1+n); //accending order
     sort(ar2,ar2+n);
    /* for(int i=0;i<n;i++)
     cout<<ar1[i]<<" ";
     cout<<endl;
     for(int i=0;i<n;i++)
     cout<<ar2[i]<<" ";
     cout<<endl;*/
     int actual=0;
     int maxl=n-1,minl=0;
     for(int i=n-1;i>=0;i--)
     {
            if(ar1[i]>ar2[maxl])
            {
                                minl++;
                                actual++;
            }
            else
            {
                                maxl--;
            }
     }
     int cheat=0;
      maxl=n-1,minl=0;
     for(int i=0;i<n;i++)
     {
            if(ar1[i]<ar2[maxl] && ar1[i]<ar2[minl])
            {
                                maxl--;;
            }
            else if(ar1[i]<ar2[maxl] && ar1[i]>ar2[minl])
            {
                                minl++;
                                cheat++;
                                
            }
            else 
            cheat++;
     }
     
     cout<<"Case #"<<tt<<": "<<cheat<<" "<<actual<<endl;
    //string s=string("Case #")+ +itoa(tt,ch,10)+string(": ");
    }
//cin>>t;
}
