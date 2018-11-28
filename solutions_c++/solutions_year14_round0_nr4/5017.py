#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;

int main()
{
    int T;
    cin>>T;
     int t=0;
    while(T--)
    {

        int l=0,m=0;
        int S;
        cin>>S;
        double A[S],B[S];
        for(int i=0;i<S;i++)
            cin>>A[i];

        for(int i=0;i<S;i++)
            cin>>B[i];

        sort(A,A+S);
        sort(B,B+S);
        int i=0;
        int j=0;

        while(i<S&&j<S)
           {

            if(A[i]<B[j])
        {
            i++;
            j++;
        }
        else
        {
            j++;
            l++;
        }
           }

          for(i=0;i<S;i++)
            for(j=0;j<S;j++)
            if(A[i]>B[j]&&A[i]!=-1&&B[j]!=-1)
          {
              m++;
              A[i]=-1;
              B[j]=-1;
          }
          t++;
          cout<<"Case #"<<t<<": "<<m<<" "<<l<<endl;
          //cout<<m<<endl;




    }
}
