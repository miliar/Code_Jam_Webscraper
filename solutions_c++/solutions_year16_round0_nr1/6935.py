#include <iostream>
#include <cstring>
#include <fstream>
using namespace std;

int main()
{
    int t,n,i,j,num,m,temp;
    ifstream fp("read.txt");
    ofstream outf("write.txt");
    fp>>t;
    int l=1;
    //cin>>t;
    while(t--)
    {
        int a[10]={0};
      //  cin>>n;
        fp>>n;
        //cout<<n<<"\n";
        //getchar();
        if(n==0)
        {
             outf<<"Case #"<<l++<<":"<<" INSOMNIA\n";

        }
        else{for(i=1;;i++)
        {
            m=n*i;
            num=m;
            while(num>0)
            {
                temp=num%10;
                a[temp]=1;
                num=num/10;
            }
            for(j=0;j<10;j++)
            {
                if(a[j]==0)
                  {
                     break;
                  }

            }
            if(j==10)
            {
                outf<<"Case #"<<l++<<":"<<" "<<m<<"\n";
        //        cout<<m<<"\n";
                break;
            }

        }}
    }
    return 0;
}
