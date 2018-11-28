#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int tc,res=0,j,res1,dif;
    string cust;
    cin>>tc;
    int i,l,fin=0,len;
    for(i = 0;i < tc; i++)
    {
    	fin = 0;
        res = 0;
        cin>>len;
        cin>>cust;
        int arr[len+1];
        for(j = 0; j <= len; j++)
        {
            arr[j]=(int)cust[j] - 48;
        }
        res1 = 0;
        for(j=1 ; j <= len;j++)
        {
            res1 += arr[j-1];
            if(res1 < j)
            {
                dif = j - res1;
                fin += dif;
                res1 += dif;
            }
        }
        cout<<"Case #"<<i+1<<": "<<fin<<endl;
    }
}