#include<bits/stdc++.h>
using namespace std;
int main()
{
  // freopen("A-large.in","r",stdin);
    //freopen("output-large.txt","w",stdout);

    unsigned long long int t,n,tmp,rem,cnt;
   // int arr[10] = {0};
    cin>>t;
     int l =0;
    while(l<t)
    {

        cin>>n;
        int arr[10] = {0};
        for(int  k =1 ;k<100;k++)
        {
            cnt = 0;
            tmp = n*k;
            if(n*(k+1)==tmp)
            {
                cout<<"Case #"<<l+1<<": "<<"INSOMNIA"<<endl;
                break;
            }

            do
            {
                rem = tmp%10 ;
                arr[rem] =1;
                tmp = tmp/10;
            }while(tmp>0);
            for(int j =0;j<10;j++)
            {
              /*  if(a[j]!=1)
                {
                    flg = 0;
                    break;
                }*/
                if(arr[j]==1)
                    cnt++;
                if(cnt == 10)
                    break;
            }
            if(cnt==10)
            {
                cout<<"Case #"<<l+1<<": "<<n*k<<endl;
                break;
            }

        }
        l++;
    }

}
