#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int h=1;h<=t;h++)
    {
        int n;
       scanf("%d",&n);
        bool* mark=new bool[10];
        for(int i=0;i<=9;i++)
            mark[i]=false;
        int num=0,i=-1;
        for(i=1;i<=1000;i++)
        {
           num=i*n;
           int num_now=num;
           while(num_now>0)
           {
              if(mark[num_now%10]==false)
              mark[num_now%10]=true;
           num_now=num_now/10;

           }
           bool alldone=true;
           for(int l=0;l<=9;l++)
           {
               if(mark[l]==false)
               {
                   alldone=false;
                   break;

               }
           }
           if(alldone==true)
            { //cout<<num<<" "<<i<<"\n";
                break;
                }
        }
           if(i<=1000)
            printf("Case #%d: %d\n",h,num);
           else
            printf("Case #%d: INSOMNIA\n",h);
    }


}

