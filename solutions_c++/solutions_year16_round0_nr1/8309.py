#include<iostream>
#include<fstream>
#include<set>
using namespace std;

int main()
{
    FILE *fin = freopen("A-large.in", "r", stdin);
	FILE *fout = freopen("A-small.out", "w", stdout);
  long long int t,n,l,x,i,temp,index=1;
   set<int> myset;
   cin>>t;
   while(t>0)
   {
       i=1;
       myset.clear();
       cin>>n;
       temp=n;
       if(n==0)
       {
           cout<<"Case #"<<index<<":"<<" "<<"INSOMNIA"<<"\n";
           index++;
       }
       else{
       while(myset.size()!=10)
       {
           while(temp>0)
           {
               l=temp%10;
               temp=temp/10;
               myset.insert(l);
           }
           i++;
           temp=i*n;
       }
      cout<<"Case #"<<index<<":"<<" "<<(i-1)*n<<"\n";
       index++;
       }
       t--;
   }
    return 0;
}
