#include <bits/stdc++.h>

using namespace std;

int main()
{
	freopen("Input.txt","r",stdin);
	freopen("Output.txt","w",stdout);
    int t,r=1;
    long long  n,num,z,y;
    int a[10];

    cin>>t;
    for(int j=0;j<t;j++)
    {
        for(int j=0;j<10;j++)
        {
            a[j]=-1;
        }
        int c=0,i=1,s=0,p,flag=0;
        cin>>n;
        if(n==0)
            {
                cout<<"Case #"<<r<<": INSOMNIA"<<endl;

            }
        while(true&&n!=0)
        {

            num=i*n;
            z=num;
            for (int l = 0; z > 0; l++)
            {
                flag=0;
                p=z%10;
                z=z/10;
               for(int k = 0;k < 10; k++)
               {
                   if(p==a[k])
                    flag=1;

               }

               if(flag==0)
               {
                  a[s]=p;
                  c++;
                  if(c==10)
                  {
                      y=num;
                      break;
                  }
                  s++;
               }
            }
            if(c==10)
            {
                cout<<"Case #"<<r<<": "<<y<<endl;
                break;

            }
            i++;
        }


        r++;
    }
    return 0;
}
