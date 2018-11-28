#include<iostream>
#include<fstream>

using namespace std;
unsigned long long int n,nam,tp,r,m=10;

int main()
{
ifstream ip;
ofstream o;
    ip.open("A-large.in");
     o.open("outl.txt");
    int t;
    ip>>t;
    int op[t];
    int k=0,l=1;
    while(t--)
    {
    l=1;
            ip>>nam;
            tp=nam;
        if(nam==0)
            {
            op[k]=-1;
            k++;
            }
            else
            {
        int count;
        int maincount=0;
        int flag[10]={0};
        while(1){
                n=nam;

                while(n)
                {
                    r=n % m;
                    flag[r]=1;
                    n=n/m;


                }
                    count=1;

                         for(int i=0;i<10;i++)
                            {
                                if(flag[i]==0)
                                    count=0;
                            }
                    maincount++;
                    if(count==1)
                    { maincount=nam;
                    break;
                    }
                l++;
                nam=l*tp;

        }

    op[k++]=maincount;

      }
    }

    for(int j=0;j<k;j++)
    {   if(op[j]==-1)
            o<<"Case #"<<j+1<<": INSOMNIA"<<'\n';
            else
                o<<"Case #"<<j+1<<": "<<op[j]<<'\n';
        }
}
