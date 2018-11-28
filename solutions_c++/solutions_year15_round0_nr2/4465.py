#include<iostream>
#include<stdio.h>
#include<cmath>
#include<set>
#include<assert.h>
using namespace std;

int run(multiset<int, greater<int> > st)
{
  int ans= *(st.begin());
  if(ans<=2) 
  {
    return ans;
  }
  int x= *(st.begin());
  //cout<<x<<"tt"<<endl;
  int y,z;
  st.erase(st.begin());
        for(int i=2;i<=x/2;i++)
        {
          y=i;
          z=x-i;      
          multiset<int, greater<int> > sp=st;

          sp.insert(y);
          sp.insert(z);

          int w=run(sp)+1;
           if( ans > w )
           {
                ans=w;
           }

        }
        return ans;
}


int main()
{
    freopen("B-small-attempt4.in","r",stdin);
    freopen("B-small-attempt4.out","w",stdout);
   // freopen("test.in","r",stdin);
    //freopen("test.out","w",stdout);
    int T;
   // int p[1005];
   // scanf("%d",&T);
   cin>>T;
    for(int cas=0;cas<T;cas++)
    {
        multiset<int, greater<int> > st;
        multiset<int, greater<int> >::iterator it;
        int smax;
        int n,x;
        st.clear();
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>x;
            st.insert(x);
            //smax=max(smax,x);
        }

        printf("Case #%d: %d\n",cas+1,run(st));

    }
    return 0;
}
