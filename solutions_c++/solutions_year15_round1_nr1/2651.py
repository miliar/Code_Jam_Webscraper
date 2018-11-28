#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    int array[100000];
    cin>>t;
    for(int l=1;l<=t;l++)
        {
        int n;
        cin>>n;
        for(int i=0;i<n;i++)
        {
            cin>>array[i];
        }
        int y=0,z=0,maxi=0;
        for(int i=1;i<n;i++)
        {
            if(array[i]-array[i-1]<0)
            {
                y+=(array[i-1]-array[i]);
            }
            maxi=max(maxi,array[i-1]-array[i]);
        }
        //printf("%d %d\n",y,maxi);
        for(int i=0;i<n-1;i++)
        {
            if(array[i]>=maxi)z+=maxi;
            else z+=array[i];
        }
      printf("Case #%d: %d %d\n",l,y,z);
   }
	return 0;
}
