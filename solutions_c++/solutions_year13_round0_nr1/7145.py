#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
    int n,flag=0;
    int i,j,k,l,ans=0;
    cin >> n;
    //int m=n;
    int array[n];
    for(i=0;i<n;i++)
    {
        cin >> array[i];
    }
    for(i=0;i<(n-2);i++)
    {
        for(j=i+1;j<(n-1);j++)
        {
            if(array[j]>array[i])
            {
                for(k=j+1;k<n;k++)
                {
                    if(array[j]<array[k])
                    {
                        flag=0;
                        for(l=k+1;l<n;l++)
                        {
                            if(array[l]==array[k])
                            {flag=1;break;}

                        }
                        if(flag==0)
                        ans++;
                    }
                    else if(array[j]==array[k])
                    break;
                }
            }
            else if(array[j]==array[i])
            break;
        }
    }
   /* int elements = sizeof(array) / sizeof(array[0]);
    std::sort(array, array + elements);
    for(i=0;i<(n-1);i++)
    {
        if(array[i]==array[i+1])
        {m--;i++;}
        if(m==n/2)
        break;
    }
    cout<< m <<endl;
    for(i=(m-1);i>1;i--)
    {
        ans=ans+(fact(i)/(fact(i-2)*2));
       // cout<< ans <<endl;
    }*/
    cout<< ans <<endl;
    return 0;
}
