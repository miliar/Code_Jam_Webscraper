#include <iostream>
#include <algorithm>
#include <sstream>
#include<math.h>

using namespace std;

int main()
{

    string a;
    long long  t,n,b[3][100],sum,l,i,j,count,flag=0,k,li;
    cin >> t;
    for(k=1;k<=t;k++)
    {
        cin >> a >> n;
        sum=0;
        l=a.length();
        flag=0;
        li=0;
        for(i=0;i<l;i++)
        {
            count=0;
            if(a[i]!='a' && a[i]!='e' && a[i]!='i' && a[i]!='o' && a[i]!='u')
            {
                count=0;
                j=i;
                while(a[j]!='a' && a[j]!='e' && a[j]!='i' && a[j]!='o' && a[j]!='u' && j<l )
                {
                    count++;
                    
                    j++;
                    

                }
                
                if(count>=n)
                {
                    sum+=((j-count-li+1)*(l-j+count-n+1));
                    
                    li=j-count+1;
                    count=0;
                }

            }
        }
        //if(flag<=1)
        cout << "Case #"<<k<<": "<<sum << endl;
        //else
        //cout << "Case #"<<k<<": "<<sum-1 << endl;
    }
}

