#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <limits.h>
#include <vector>
#include <map>
#include <string>
#include <iterator>
#include <set>
#include <utility>
#include <queue>
#include <numeric>
#include <functional>
#include <ctype.h>
#include <stack>
#include <algorithm>
#include <cstdlib>
#define MAX 100100
#define mod 1000000007
#define MS0(x) memset(x, 0, sizeof(x))
#define ll long long int
#define in(x) scanf("%I64d", &x)
#define ind(x) scanf("%d", &x)

using namespace std;
int main()
{
	//#ifndef ONLINE_JUDGE
//#endif

	 ios_base::sync_with_stdio(false);
 cin.tie(NULL);
    int tc,t;
    cin>>tc;
    for(t=1;t<=tc;t++)
    {
    	string s;
    	cin>>s;
    	int i;
    	//cout<<"lol";
    	int arr[27]={0};
    	int a[2001]={0};
    	for(i=0;i<s.length();i++)
    	{
    		arr[s[i]-'A'+1]++;
    	}
    	int j=0;
         if(arr[26]>0)
         {
             a[0]=arr[26];
              arr[26]=arr[26]-a[0];
             arr[5]=arr[5]-a[0];

             arr[18]=arr[18]-a[0];
             arr[15]=arr[15]-a[0];
         }
         if(arr[7]>0)
         {
             a[8]=arr[7];
             arr[5]=arr[5]-a[8];
             arr[9]=arr[9]-a[8];
             arr[7]=arr[7]-a[8];
             arr[8]=arr[8]-a[8];
             arr[20]=arr[20]-a[8];
         }
         if(arr[24]>0)
         {
              a[6]=arr[24];
             arr[19]=arr[19]-a[6];
             arr[9]=arr[9]-a[6];
             arr[24]=arr[24]-a[6];

         }
         if(arr[23]>0)
         {
              a[2]=arr[23];
               arr[20]=arr[20]-a[2];
             arr[23]=arr[23]-a[2];
             arr[15]=arr[15]-a[2];
         }
         if(arr[21]>0)
         {
                  a[4]=arr[21];
              arr[6]=arr[6]-a[4];
             arr[15]=arr[15]-a[4];
             arr[21]=arr[241]-a[4];
             arr[18]=arr[18]-a[4];
         }
          if(arr[15]>0)
         {
                  a[1]=arr[15];
              arr[15]=arr[15]-a[1];
             arr[14]=arr[14]-a[1];
             arr[5]=arr[5]-a[1];
         }
         if(arr[8]>0)
         {
                  a[3]=arr[8];
              arr[20]=arr[20]-a[3];
             arr[8]=arr[8]-a[3];
             arr[18]=arr[18]-a[3];
               arr[5]=arr[5]-a[3];
             arr[5]=arr[5]-a[3];
         }
         if(arr[6]>0)
         {
                  a[5]=arr[6];
              arr[6]=arr[6]-a[5];
             arr[9]=arr[9]-a[5];
             arr[22]=arr[22]-a[5];
               arr[5]=arr[5]-a[5];
         }
         if(arr[19]>0)
         {
                  a[7]=arr[19];
              arr[19]=arr[19]-a[7];
             arr[5]=arr[5]-a[7];
             arr[22]=arr[22]-a[7];
               arr[5]=arr[5]-a[7];
               arr[14]=arr[14]-a[7];
         }
         if(arr[5]>0)
         {
                  a[9]=arr[5];
              arr[14]=arr[14]-a[9];
             arr[9]=arr[9]-a[9];
             arr[14]=arr[14]-a[9];
               arr[5]=arr[5]-a[9];
         }
         cout<<"Case #"<<t<<": ";
         for(i=0;i<=9;i++)
         {
             for(j=1;j<=a[i];j++)
             {
                cout<<i;
             }
         }
         cout<<"\n";
    }
	return 0;
}