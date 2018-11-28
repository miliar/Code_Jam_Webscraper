
#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <iterator>
#include <list>
using namespace std;
int main () {
   
    ofstream fout ("out.txt");
    ifstream fin("in.txt");
    
    long long int s,p,q; 
    int t,n,i,j,k,l;
    fin>>t;
    for(i=0;i<t;i++)
    {
      list<long long int> pq;
      list<long long int>::iterator it;
      fin>>s>>n;
      
      for(j=0;j<n;j++)
      {
        fin>>p;
        pq.push_back(p);
      }
      pq.sort();
      it=pq.begin();
      for(j=0,k=0;j<n;)
      {

        q=*it;
        cout<<q<<" "<<s<<"\n";
        if(s>q)
          s+=q,it++,j++;
        else 
        {
          l=1;
          if(s!=1)
         {for(;;l++)
            if((1<<l)*s-(1<<l)+1>q )
              break;
          }else
            break;
          if(l<n-j)
            k+=l,j++,it++,s=(1<<l)*s-(1<<l)+1+q;
          else
            break;
        }
      }
      if(j!=n)
        k+=n-j;
      fout<<"Case #"<<i+1<<": "<<k<<"\n";
    }
    return 0;
}
