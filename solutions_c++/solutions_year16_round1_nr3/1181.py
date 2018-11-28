#include<bits/stdc++.h>
using namespace std;
#define popcount __builtin_popcount
int arr[10010];
int t,i,n;
vector<int> vec;
int main()
{
    ifstream IF;
    IF.open("input.txt");
    ofstream OF;
    OF.open("output.txt");


    IF >> t;
    for(int tc=1;tc<=t;tc++)
    {
       IF>>n;
       int ans=0;
       for(i=1;i<=n;i++)
         IF>>arr[i];
            int lim = (1<<n)-1;
         for(i=0;i<=lim;i++)
         {
            if(popcount(i)>=2)
            {
                int tmp=i;
                int bin[40]={0};
                int j=0;

                while(tmp)
                {
                  bin[j++]=tmp%2;
                  tmp>>=1;
                }
                vec.clear();
                for(j=0;j<n;j++)
                {
                  if(bin[j]==1)
                  {
                        vec.push_back(j+1);
                  }
                }

                 int sz=vec.size();


                do
                {


                   int flag=0;
                    for(int k=0;k<sz;k++)
                    {
                        if(k==0)
                        {
                            if(!(arr[vec[k]]==vec[k+1] || arr[vec[k]]==vec[sz-1]))
                            {  flag=1; break; }
                        }
                        else if(k<sz-1)
                        {
                            if(!(arr[vec[k]]==vec[(k+1)%sz] || arr[vec[k]]==vec[(k-1+sz)%sz]))
                                { flag=1;break; }
                        }
                        else
                        {
                            if(!(arr[vec[k]]==vec[0] || arr[vec[k]]==vec[k-1]))
                            {  flag=1; break; }
                        }
                    }

                    if(!flag)
                    {
                      ans=max(ans,sz);
                      break;
                    }
                }while(next_permutation(vec.begin(),vec.end()));

            }

         }

        OF <<"Case #" << tc << ": " <<ans << endl;
    }

    OF.close();
    IF.close();
}
