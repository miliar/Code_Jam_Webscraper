#include<iostream>
#include<fstream>
#include<map>
#include<stdlib.h>
#include<string.h>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout;
    fin.open("input.txt");
    fout.open("ans.txt");
    int t,j;
    long long int val,count,i,n,k,number,val1,k1;
  //  char b[100100];
    bool arr[11];
    fin>>t;
    //cout<<t;
    for(j=1;j<=t;j++)
    {
        fin>>n;
        memset(arr,0,sizeof(arr));
        fout<<"Case #"<<j<<": ";
        if(n==0) fout<<"INSOMNIA\n";
        else
        {
            count=0;
            number=n;
            k=1;
            while(count<10)
            {
                val=n*(k);
                val1=val;
               // cout<<"val "<<val<<endl;
                while(val>0)
                {
                    k1=val%10;
                    if(arr[k1]==0)
                    {
                        arr[k1]=1;
                        count++;
                        if(count==10) break;
                    }
                    val/=10;
                }
                k++;
            }
           // cout<<n<<" "<<k<<" "<<n*k<<val1;
            fout<<val1<<endl;
        }
    }
    return 0;
}
