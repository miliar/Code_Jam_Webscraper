#include <iostream>

using namespace std;

int main()
{
    int t,count;
    int temp=0,y;
    int p,q,k;
    cin>>t;
    int z=t;

    while(t--)
    {
        int a,b,c,d;
        int x[16]={0};
        temp++;
        y=0;
        count=0;
        cin>>p;
        k=1;
        while(k<=4)
        {
            cin>>a>>b>>c>>d;
            if(k==p)
            {
                x[a-1]++; x[b-1]++; x[c-1]++; x[d-1]++;
            }
            k++;

        }
         cin>>q;
        cout<<endl;
        k=1;
        while(k<=4)
        {
            cin>>a>>b>>c>>d;
            if(k==q)
            {
                x[a-1]++; x[b-1]++; x[c-1]++; x[d-1]++;
            }
            k++;

        }
        for(int i=0;i<16;i++)
        {
            if(x[i]>1)
            {
                count++;
                y=i+1;
            }
        }

      if(count==1)
      {
          cout<<"Case #"<<temp;
          cout<<":"<<" "<<y;
          if(temp!=z)
          cout<<endl;
      }
      if (count>1)
     {
          cout<<"Case #"<<temp;
          cout<<":"<<" ";
          cout<<"Bad magician!";
          if(temp!=z)
          cout<<endl;

     }
     if(count==0)
     {
         cout<<"Case #"<<temp;
         cout<<":"<<" ";
         cout<<"Volunteer cheated!";
         if(temp!=z)
          cout<<endl;
     }
    }

    return 0;
}
