#include<iostream>
#include<cmath>
using namespace std;
int n,k,c,s;

void calculate(int k,int c,int s)
{
    long long point;
    int temp;

    if(s<(k/c+k%c))
    {
        cout<<" IMPOSSIBLE"<<endl;
        return;
    }

    temp=k-1;

    for(int i=0;i<k/c;i++)
    {
        point=0;
        for(int j=0;j<c;j++)
        {
            point=point*k+temp;
            --temp;
        }

        cout<<" "<<point+1;
    }

    point=0;
    for(int i=0;i<k%c;i++)
    {
         point=point*k+temp;
            --temp;

            if(i==(k%c-1))
                cout<<" "<<point+1;
    }
     cout<<endl;

}

int main()
{
    cin>>n;

    for(int i=0;i<n;i++)
    {
        cin>>k>>c>>s;
         cout<<"Case #"<<i+1<<":";
        /*if(s>=k)
        {
            for(j=1;j<=k;j++)
                cout<<" "<<k;

            cout<<endl;

            continue;
        }*/

     calculate(k,c,s);

    }

    return 0;
}
