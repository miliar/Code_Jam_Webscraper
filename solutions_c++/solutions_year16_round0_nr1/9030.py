#include <iostream>
#include<bits/stdc++.h>

using namespace std;
int ar[10];



int main()
{

for(int i=0;i<10;i++)
{
    ar[i]=0;
}


    freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);


int t;
cin>>t;

for(int i=1;i<=t;i++)
{

    for(int i=0;i<10;i++)
{
    ar[i]=0;
}


    int n;
    cin>>n;

    if(n==0)
    {
        cout<<"Case #"<<i<<": INSOMNIA\n";
        continue;
    }

    int x=0;
    int j=1;
    while(true)
    {

        x=n*j;
        int xx=x;

        while(xx>0)
        {
            int y=xx%10;
            xx=xx/10;
            ar[y]++;

        }

        j++;

        int flag=0;
        for(int i=0;i<10;i++)
        {
            if(ar[i]<=0)
            {
                flag=1;
                break;

            }


        }
        if(flag==0)
        {
            break;
        }




    }



    cout<<"Case #"<<i<<": "<<x<<"\n";











}












return 0;




}
