#include<stdio.h>
#include<conio.h>
#include<iostream>
using namespace std;
int main()
{

    int sum;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    sum=0;
    int i, t, n, incount,j;
    i=0;
    char *data;
    cin>>t;
    while(t--)
    {
        i++;
        cin>>n;
        data = new char[n+2];
        cin>>data;
        sum = 0;
        incount=0;
        for(j=0;j<=n;j++)
        {
            if(sum<j)
            {
                incount += j-sum;
                sum += (j-sum);
            }

            sum+= (data[j] - 48);

        }
        cout<<"Case #"<<i<<": "<<incount;
        cout<<endl;
    }


    return 0;
}
