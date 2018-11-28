#include<bits/stdc++.h>
#include<stdio.h>
#include<fstream>
using namespace std;

int main()
{
    freopen("B-large(2).in","r",stdin);
    freopen("ans.txt","w",stdout);
    int T;
    cin >> T;
    int cases=1;
    while(T--)
    {
      long long int arr[1010]={0};
      long long int tot,max1=0,time=0,xx=0,yy=0,z=0;

      cin >> tot;

      for(long long int i=1;i<=tot;i++)
      {
          cin >> arr[i];
          if(arr[i]>max1) max1=arr[i];
      }

     time=max1;
     for(long long int i=1;i<=max1;i++)
		{
			xx=0,yy=0;
			for(long long int j=1;j<=tot;j++)
			{
				if(arr[j]>i)
				{
					xx = xx + (arr[j]/i)-1;

					if(arr[j]%i!=0) xx = xx + 1;

					if(i>yy) yy=i;
				}
				else
                {
                    if(arr[j]>yy) yy=arr[j];
                }
			}
            xx+=yy; if(xx<time)time=xx;
		}

  cout << "Case #" << cases << ": " << time << endl;
     cases++;

    }

    return 0;
}

