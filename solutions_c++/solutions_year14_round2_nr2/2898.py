#include <iostream>

using namespace std;

int main()
{
    int t;
    cin>>t;
    long long int a,b,k,temp,count;
    for(int z=1;z<=t;z++)
    {
        count=0;

        cin>>a>>b>>k;

            for(int j=0;j<a;j++)
            {
                for(int l=0;l<b;l++)
                {
                   temp=j&l;


                    if((j&l)<k)
                    {
                      count++;
                    }

                }
            }

        cout<<"Case #"<<z<<": "<<count<<endl;


    }
    return 0;
}
