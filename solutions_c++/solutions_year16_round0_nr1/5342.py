#include<iostream>
#include<cstring>
#include<fstream>

using namespace std;
int main()
{
    ifstream fin;
    ofstream fout("out_large.txt");
    fin.open ("in_large.in");
    
        int t,c,l,s,n,q,count=1,flag=0,flag1=0;
        int x[10];
        
        fin>>t;
        s=t;
        while(t--)
        {
            count= flag=0;
            fin>>c;
            if(c==0)
            {
                fout<<"Case #"<<s-t<<": "<<"INSOMNIA"<<endl;
            }
            else {
            fill_n(x,10,0);
            while(flag==0)
            {
                n=c*count;
                while(n!=0)
                {
                    x[n%10]++;
                    n/=10;
                }
                count++;
                flag1=0;
                for(int i=0;i<10;i++)
                {
                    if(x[i]==0)
                        flag1=1;
                }
                if(flag1==0)
                    flag=1;
            }
            fout<<"Case #"<<s-t<<": "<<c*(count-1)<<endl;
            }
        }
        fin.close();
        fout.close();
}
