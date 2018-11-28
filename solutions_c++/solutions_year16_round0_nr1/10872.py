#include<bits/stdc++.h>
#define max 1000000007
#define rep(i,n) FOR(i,1,n)
#define FOR(i,a,b) for(i=a;i<=b;i++)

using namespace std;
 
int main()
{
    std::ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
 
     long long int t,n;
     cin>>t;
     long long int tr=0;
     while(tr<t)
     {    tr++;
          std::vector<int>::iterator it;
          long long int i=1;
          cin>>n;
          if(n==0)
          {cout<<"case #"<<tr<<": INSOMNIA"<<endl;}
          else
          {   
               long long int m;
               int d;
               
               vector<int> vec;
               while(1)
               {
                    m=i*n;
                    //cout<<" "<<m<<"M"<<n<<"N"<<i<<"I ";
                    while(m>0)
                    {
                         d=m%10;
                         it = find (vec.begin(),vec.end(),d);
                           if (it==vec.end())
                              {
                                   vec.push_back(d);
                              }
                         m=m/10;     

                    }

                         if(vec.size()==10)
                         {
                         cout<<"case #"<<tr<<": "<<n*(i)<<endl;
                         break;
                         }
                    i++;
               }
          }
//          tr++;
     }
    return 0;
}
