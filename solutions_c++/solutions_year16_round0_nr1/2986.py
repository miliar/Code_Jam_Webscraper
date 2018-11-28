#include<bits/stdc++.h>
using namespace std;
int main()
{
    ifstream fin;
    ofstream fout("ans.txt");
    fin.open ("input.txt");

    if(!fin.is_open())
    {
        cout<<"file error";
    }
    else
    {
        long long t,x[10],c,l,s,cou=1,n,q,flag=0,fl=0;
        fin>>t;
        s=t;
        while(t--)
        {
            cou= flag=0;
            fin>>c;
            if(c==0)
            {
                fout<<"Case #"<<s-t<<": "<<"INSOMNIA"<<endl;
            }
            else {
            fill_n(x,10,0);
            while(flag==0)
            {
                n=c*cou;
                while(n!=0)
                {
                    x[n%10]++;
                    n/=10;
                }
                cou++;
                fl=0;
                for(int i=0;i<10;i++)
                {
                    if(x[i]==0)
                        fl=1;
                }
                if(fl==0)
                    flag=1;
            }
            fout<<"Case #"<<s-t<<": "<<c*(cou-1)<<endl;
            }
        }
        fin.close();
        fout.close();
    }
}
