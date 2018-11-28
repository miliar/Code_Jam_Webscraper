#include<bits/stdc++.h>
using namespace std;
int main()
{
    int c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,N,tcase;
    cin>>tcase;
    for(int j=1;j<=tcase;j++)
    {
        int i=1,a,ans;
        c0=0,c1=0,c2=0,c3=0,c4=0,c5=0,c6=0,c7=0,c8=0,c9=0;
        cin>>N;
        if(N>0)
            {
                while(1)
               {
            int reverse=0;
            ans=N*i;
            a=ans;
            while(ans!=0)
            {
                int r;
                 reverse = reverse * 10;
                 r=ans%10;
                 if(r==0)
                 {
                     c0++;
                 }
                 else if(r==1)
                 {
                     c1++;
                 }
                 else if(r==2)
                 {
                     c2++;
                 }
                 else if(r==3)
                 {
                     c3++;
                 }
                 else if(r==4)
                 {
                     c4++;
                 }
                 else if(r==5)
                 {
                     c5++;
                 }
                 else if(r==6)
                 {
                     c6++;
                 }
                 else if(r==7)
                 {
                     c7++;
                 }
                 else if(r==8)
                 {
                     c8++;
                 }
                 else if(r==9)
                 {
                     c9++;
                 }
                 reverse = reverse + r;
                 ans       = ans/10;
            }
            i++;
            if(c0>0 && c1>0 && c2>0 && c3>0 && c4>0 && c5>0 && c6>0&& c7>0 && c8>0 && c9>0)
                break;
        }
        cout<<"Case #"<<j<<": "<<a<<endl;
        }
        else
        {
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        }
    }
    return 0;
}
