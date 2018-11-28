#include <iostream>
using namespace std;
int main() {
    freopen("C-small-attempt0.in","r",stdin);
    freopen("cj_3.txt","w",stdout);
    int t,l,x,k,flag,r,sign,tot,a,b,i,e;
    int req[3]={2,3,4};
    int m[4][4]={1,2,3,4,2,-1,4,-3,3,-4,-1,2,4,3,-2,-1};
    cin>>t;
    for(int z=0;z<t;z++)
    {
        cin>>l>>x;
        string str;
        cin>>str;
        tot=l*x;
        k=0;
        flag=0;
        i=0;
        while(i<tot&&flag==0)
        {
            if(str[i%l]=='1')
                r=1;
            else
                r=(int)str[i%l]-103;
            i++;
            sign=0;
            while((r!=req[k]||sign==1)&&(i<tot))
            {
                a=r;
                if(str[i%l]=='1')
                    b=1;
                else
                    b=(int)str[i%l]-103;
                r=m[a-1][b-1];
                if(r<0)
                {
                    sign++;
                    r*=(-1);
                }
                sign=sign%2;
                i++;
            }
            if(r==req[k]&&flag==0)
            {
                    k++;
            }
            if(k==3)
                    flag=1;
        }
      e=1;
      if(i<tot)
      {
      while(i<tot)
      {
        b=(int)str[i%l]-103;
        e=m[e-1][b-1];
        if(e<0)
        {
            sign++;
            e*=(-1);
        }
        sign=sign%2;
        i++;
      }
      if(e==1&&sign==0)
                       flag=1;
      else
                       flag=0;
      }
        if(flag==1)
            cout<<"Case #"<<z+1<<": YES"<<endl;
        else
            cout<<"Case #"<<z+1<<": NO"<<endl;
    }
	return 0;
}
