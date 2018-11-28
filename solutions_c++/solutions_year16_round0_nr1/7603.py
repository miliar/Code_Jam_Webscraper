#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
    int t,k,i,z,ans=0,digit,n,x;
    bool flag=true;
    int count[10];
    ifstream fin;
    ofstream fout;
    fin.open("A-large.in",ios::in);
    fout.open("output1.txt",ios::out);
    fin>>t;
    x=1;
    while(x<=t)
    {
        fin>>n;
        k=1;
        ans=0;
        for(i=0;i<10;++i)
        {
            count[i]=0;
        }
        while(true)
        {
            z=k*n;
            ++k;
            while(z!=0)
            {
                digit=z%10;
                count[digit]++;
                z=z/10;
            }
            flag=false;
            for(i=0;i<10;++i)
            {
                if(count[i]==0)
                {
                   flag=true;
                   break;
                }
            }
            if(flag==false)
            {
                ans=k*n-n;
                break;
            }
            if(k==100)
            {
                break;
            }
        }

        if(ans==0)
        {
            fout<<"Case #"<<x<<": "<<"INSOMNIA\n";
        }
        else
        {
            fout<<"Case #"<<x<<": "<<ans<<endl;
        }
        x++;
    }
}
