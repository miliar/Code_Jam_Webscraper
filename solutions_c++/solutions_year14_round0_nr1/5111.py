#include <iostream>

using namespace std;

int main()
{
    int t,count1,a1,a2,a3,a4,q1,q2,k,count2=0,y;

    cin>>t;
    int k1=t;

    while(t--)
    {
        int a[16]={0};
        count2++;
        y=0;
        count1=0;
        cin>>q1;
        k=1;
        while(k<=4)
        {
            cin>>a1>>a2>>a3>>a4;
            if(k==q1)
            {
                a[a1-1]++;
                a[a2-1]++;
                a[a3-1]++;
                a[a4-1]++;
            }
            k++;

        }
         cin>>q2;
        cout<<endl;
        k=1;
        while(k<=4)
        {
            cin>>a1>>a2>>a3>>a4;
            if(k==q2)
            {
                a[a1-1]++;
                a[a2-1]++;
                a[a3-1]++;
                a[a4-1]++;
            }
            k++;

        }
        for(int i=0;i<16;i++)
        {
            if(a[i]>1)
            {
                count1++;
                y=i+1;
            }
        }

      if(count1==1)
      {
          cout<<"Case #"<<count2<<":"<<" "<<y;
          if(count2!=k1)
          cout<<endl;
      }
     else if (count1>1)
     {
          cout<<"Case #"<<count2<<":"<<" "<<"Bad magician!";
          if(count2!=k1)
          cout<<endl;

     }
     else
     {
         cout<<"Case #"<<count2<<":"<<" "<<"Volunteer cheated!";
         if(count2!=k1)
          cout<<endl;
     }
    }

    return 0;
}
