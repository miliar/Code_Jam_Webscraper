#include<iostream>
using namespace std;
int main()
{int t,i,j,cal,a,b,ar[10]={1,4,9,121,484,10201};
cin>>t;

for(i=0;i<t;i++)
{cal=0;
cin>>a;
cin>>b;
for(j=0;j<6;j++)
    {if(ar[j]>=a&&ar[j]<=b)
        {cal++;

        }

    }
cout<<"Case #"<<i+1<<": "<<cal<<endl;
}

}
