#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int flag;
    int T,j=1;
    int arr[11];

    long long int N,r,i,test;
    cin>>T;
    while(j<=T)
    {
          for(int k=0;k<=9;k++)
    {
        arr[k]=k;
    }
        cin>>N;
        for(i=1;;i++)
        {
            if(N==0)
            {
                cout<<"Case #"<<j<<": "<<"INSOMNIA"<<endl;
                flag=0;
                break;
            }
            test=N*i;
              while(test!=0)
              {
                  r=test%10;
                 for(int l=0;l<=9;l++)
                 {
                     if(r==arr[l])
                     {
                         arr[l]=-1;

                     }
                 }
                  test=test/10;
              }
              for(int l=0;l<=9;l++)
              {
                  if(arr[l]<0)
                    flag=1;
                  else
                  {
                    flag=0;
                    break;
                  }
              }

              if(flag)
              {
                  break;
              }

        }

        if(flag)
        {
            cout<<"Case #"<<j<<": "<<(N*i)<<endl;
        }

        j++;
    }

    return 0;
}
