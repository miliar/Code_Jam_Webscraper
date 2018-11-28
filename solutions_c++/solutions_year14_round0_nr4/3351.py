#include <iostream>
#include <fstream>
#include <queue>
#include <algorithm>
#include <stack>

using namespace std;

int main()
{
    int t,n,res1,res2;
    bool elem[1001];
    bool at_all;
    double a;
    vector<double> noob1,noob2;
    ifstream in("D.in");
    ofstream out("D.out");
    in>>t;
    for (int i=0;i<t;i++)
    {
       res1=0;res2=0;
       noob1.clear();
       noob2.clear();
       in>>n;
       for (int j=0;j<n;j++)
       {
           elem[j]=true;
           in>>a;
           noob1.push_back(a);
       }
       sort(noob1.begin(),noob1.end());
       for (int j=0;j<n;j++)
       {
           in>>a;
           noob2.push_back(a);
       }
       sort(noob2.begin(),noob2.end());
       int k=0;
       for (int j=0;j<n;j++)
       {
           if (noob1[j]>noob2[k])
           {
               k++;
               res1++;
           }
       }

       for (int j=0;j<n;j++)
       {
           if ((noob1[j]>noob2[n-1])||(!(elem[n-1]))) {res2+=n-j; break;}
           if (noob1[j]<noob2[0])
           {
                for (int c=0;c<n;c++)
                {
                    if (elem[c]) {elem[c]=false;break;}
                }
                continue;
           }
           for (int b=n-2;b>=0;b--)
           {
               if (noob1[j]>noob2[b])
               {
                    for (int c=b+1;c<n;c++)
                    {
                        if (elem[c]) {elem[c]=false;break;}
                    }
                    break;
               }
           }
       }
       out<<"Case #"<<i+1<<": "<<res1<<' '<<res2<<endl;
    }
    return 0;
}
