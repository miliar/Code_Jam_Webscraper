#include<bits/stdc++.h>
using namespace std;

#define X first
#define Y second
#define ii1 pair<char,int>
#define ii pair<char,char>
#define l long long
#define pb(x) push_back(x)
map< ii, ii1>map1;
ifstream ifs("rajesh.in");
ofstream ofs("raj.out",ofstream::app);
int main()
{
    int t;
    ifs>>t;
    map1[ii('1','1')]=ii1('1',0);
    map1[ii('1','i')]=ii1('i',0);
    map1[ii('1','j')]=ii1('j',0);
    map1[ii('1','k')]=ii1('k',0);
    map1[ii('i','1')]=ii1('i',0);
    map1[ii('i','i')]=ii1('1',1);
    map1[ii('i','j')]=ii1('k',0);
    map1[ii('i','k')]=ii1('j',1);
    map1[ii('j','1')]=ii1('j',0);
    map1[ii('j','i')]=ii1('k',1);
    map1[ii('j','j')]=ii1('1',1);
    map1[ii('j','k')]=ii1('i',0);
    map1[ii('k','1')]=ii1('k',0);
    map1[ii('k','i')]=ii1('j',0);
    map1[ii('k','j')]=ii1('i',1);
    map1[ii('k','k')]=ii1('1',1);
    for(int ix=1;ix<=t;ix++)
    {

         int L,X;
         ifs>>L>>X;
         string str;
         ifs>>str;
         ofs<<"Case #"<<ix<<": ";
         string str1=str;
         for(int i=1;i<X;i++)str+=str1;
         ii1 ar[100009];
         ar[0].X=str[0];
         ar[0].Y=0;
         for(int i=1;i<L*X;i++)
         {
             ar[i].X=map1[ii(ar[i-1].X,str[i])].first;
             ar[i].Y=ar[i-1].Y+map1[ii(ar[i-1].X,str[i])].second;
         }
         int flag=0;
         //for(int i=0;i<L*X;i++)cout<<ar[i].X<<" "<<ar[i].Y<<endl;
         if(ar[L*X-1].X=='1'&&ar[L*X-1].Y%2==1)
         {
             for(int i=0;i<L*X;i++)
             {
                if(ar[i].Y%2==0&&ar[i].X=='i')
                {
                     for(int j=i+1;j<L*X;j++)
                     {
                         if(ar[j].X=='k'&&ar[j].Y%2==0)
                         {
                             flag=1;
                             goto s;
                         }
                     }
                }
             }
         }
         s:
         if(flag==1)
         {
             ofs<<"YES"<<endl;
         }
         else
         {
             ofs<<"NO"<<endl;
         }


    }
}
