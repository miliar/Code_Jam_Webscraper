#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("ox1.in","r",stdin);
    freopen("ankur2.txt","w",stdout);
    long t,n,i,j,x,y,z=1;

    string a;
    vector<long>b;
    cin>>t;
    while(t--)
    {
      cin>>a;
      //cout<<a;
      vector<long>c(26,0);
      //cout<<c[25];
      for(i=0;i<a.size();i++)
      {
          c[a[i]-65]++;
      }
      //cout<<c[25];

      if(c[25]>0)
      {
        for(j=0;j<c[25];j++)
            b.push_back(0);
        c[4]-=c[25];c[17]-=c[25];c[14]-=c[25];
        c[25]=0;
      }

      if(c[22]>0)
      {
         for(j=0;j<c[22];j++)
            b.push_back(2);
         c[14]-=c[22];c[19]-=c[22];
         c[22]=0;
      }

      if(c[23]>0)
      {
         for(j=0;j<c[23];j++)
            b.push_back(6);
         c[18]-=c[23];c[8]-=c[23];
         c[23]=0;
      }

      if(c[6]>0)
      {
         for(j=0;j<c[6];j++)
            b.push_back(8);
        c[7]-=c[6];c[19]-=c[6];c[4]-=c[6];c[8]-=c[6];
        c[6]=0;
      }

      if(c[7]>0)
      {
         for(j=0;j<c[7];j++)
            b.push_back(3);
         c[19]-=c[7];c[17]-=c[7];c[4]=c[4]-2*c[7];
         c[7]=0;
      }

      if(c[18]>0)
      {
         for(j=0;j<c[18];j++)
            b.push_back(7);
         c[21]-=c[18];c[13]-=c[18];c[4]=c[4]-2*c[18];
         c[18]=0;
      }

      if(c[21]>0)
      {
          for(j=0;j<c[21];j++)
            b.push_back(5);
          c[8]-=c[21];c[4]-=c[21];c[5]-=c[21];
          c[21]=0;
      }

      if(c[5]>0)
      {
          for(j=0;j<c[5];j++)
            b.push_back(4);
         c[14]-=c[5];c[20]-=c[5];c[17]-=c[5];
         c[5]=0;
      }

      if(c[14]>0)
      {
        for(j=0;j<c[14];j++)
            b.push_back(1);
      }

      if(c[8]>0)
      {
          for(j=0;j<c[8];j++)
            b.push_back(9);
      }

      sort(b.begin(),b.end());
      /*for(i=0;i<b.size();i++)
        cout<<b[i];*/
      cout<<"Case #"<<z<<": ";
      for(i=0;i<b.size();i++)
        cout<<b[i];
      cout<<'\n';
      a.clear();b.clear();
      z++;
    }
    return 0;
}
