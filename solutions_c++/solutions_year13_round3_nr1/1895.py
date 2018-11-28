#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <cstdio>
#include <sstream>
#include <numeric>
#include <iterator>
#include <queue>
#include <set>
#include <map>
#include <vector>

using namespace std;

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

char str[100];

int find_if(int i,int j,int k)
{
    int itr,ncount=0;
    for(itr=i;itr<=j;itr++)
    {
                          if(str[itr]!= 'a' && str[itr]!= 'e' && str[itr]!= 'i' && str[itr]!= 'o' && str[itr]!= 'u')
                                        ncount++;
                          else
                                        ncount=0;
                          if(ncount==k)
                                       return 1;        
    }        
    return 0;
}




int main()
{
    int test,count,i,j,k,n,ans[100];
    cin>>test;
    for(i=1;i<=test;i++)
    {                   
                        count=0;
                        cin>>str>>n;
                        for(j=0;j<strlen(str);j++)
                        {
                                                  for(k=j;k<strlen(str);k++)
                                                  {                         
                                                                            //cout<<j<<k<<"\n";
                                                                            if(find_if(j,k,n))
                                                                            {
                                                                                                                count++;
                                                                            }
                                                  }
                        }
                        ans[i]=count;
    }
    for(i=1;i<=test;i++)
                        cout<<"Case #"<<i<<": "<<ans[i]<<"\n";
    cin>>i;
    
}
