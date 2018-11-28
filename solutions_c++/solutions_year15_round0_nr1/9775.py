#include <iostream>
#include<cstring>

using namespace std;

int main()
{
    int t;
    cin>>t;
    int j;
    for(j=1;j<=t;j++)
    {
        int i,sm;
        cin>>sm;

        char a[sm+1];
        char b='0';

            cin>>a;





        int sum=0;
        int count=0;

        for(i=1;i<=sm+1;i++)
        {
            int k=a[i-1]-b;
            int x=0;
            sum=sum+k;

            if(sum<i)
            {
                if(a[i]=='0') continue;



                else
                {
                    count+=i-sum;
                    x=count;
                    sum=sum+x;
                }
            }

        }
        cout<<"Case #"<<j<<": "<<count<<endl;

    }

    return 0;
}
