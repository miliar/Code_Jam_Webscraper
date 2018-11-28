#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>
#include <vector>
#include <map>
#include <utility>
#include <queue>
#include <stdio.h>
#include <stdlib.h>

#define FO(i,a,b) for (int i = (a); i < (b); i++)
#define RO(i,b,a) for (int i = (b); i >= (a); i--)
#define pb push_back
#define ARR0(A) memset((A), 0, sizeof((A)))

using namespace std;
typedef long long LL;
typedef long double LD;

// Constants
const LD PI = 3.1415926535897932384626433832795;


int ps[26];
void A()
{
    int t;cin>>t;
    LL sol=0;

    FO(i,0,t)
    {   int n;
        cin>>n;


        FO(j,0,n) cin>>ps[j];

        int sum = 0;

        FO(j,0,n) sum+=ps[j];
        int actsum = sum;

        cout<<"Case #"<<(i+1)<<": ";
        FO(j,0,sum)
        {
            int max1=-1,ind1=-1;
            FO(k,0,n)
            {
                if(ps[k]>max1)
                    {
                        max1= ps[k];ind1=k;
                    }
            }

            int max2=-1,ind2=-1;
            FO(k,0,n)
            if(k!=ind1)
            {
                if(ps[k]>max2)
                    {
                        max2= ps[k];ind2=k;
                    }
            }

            int remain = actsum - (j+1);
            ps[ind1]--;
          //  cout<<ind1<<"--" <<ps[ind1]<<endl;
            int majority = (actsum-remain)%2==0?(actsum-remain)/2:(actsum+1-remain)/2;

//            cout<<ind1<<" " <<ind2<< " "<< actsum<<" " <<remain << " (" << ps[ind1]<< ":" <<ind1<< ") "<<majority<<endl;
            
            if(max1!=0)
                cout<< char('A'+ind1);

            int remmaj = (remain-1)%2==0?1+(remain-1)/2:(remain+1)/2;

            if(ps[ind1]>remmaj)
                {

                }
            else if(max2!=0&&remain!=2)
                {
                    cout<<char('A'+ind2);
                    ps[ind2]--;
                    j=j+1;
                }   

            cout<<" ";

        }
        
        cout<< endl;

    }
}

int main () {
    ios::sync_with_stdio(false);
    A();

    return 0;
}
