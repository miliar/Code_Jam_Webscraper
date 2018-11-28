#include<stdio.h>
#include<iostream>
#include<string.h>
#include<algorithm>
#include<map>
#include<stdlib.h>
#include<climits>
#include<vector>
#include<iostream>
typedef long long int ll;
using namespace std;

int arr[5][5];
int brr[5][5];
int main()
{
   freopen("A-small-attempt4.in","r",stdin);
   freopen("output.txt","w",stdout);
   int t,r1,r2;
   cin>>t;
   for(int k=1;k<=t;k++)
   {
       cin>>r1;
       for(int i=0;i<4;i++)
       {
           for(int j=0;j<4;j++)
            cin>>arr[i][j];
           sort(arr[i],arr[i]+4);

       }
       cin>>r2;
       for(int i=0;i<4;i++)
       {
           for(int j=0;j<4;j++)
            cin>>brr[i][j];
           sort(brr[i],brr[i]+4);
       }
       r1--;
       r2--;

       vector<int> vec(4);
       vector<int>::iterator it;

       it=set_intersection(arr[r1],arr[r1]+4,brr[r2],brr[r2]+4,vec.begin());
       vec.resize(it-vec.begin());
       if(vec.size()==0)
       {
           cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
       }
       else if(vec.size()==1)
       {
           cout<<"Case #"<<k<<": "<<vec[0]<<endl;
       }
       else
       {
           cout<<"Case #"<<k<<": Bad magician!"<<endl;
       }
   }
   return 0;
}
