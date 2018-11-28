#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int i,j,t,n,r,k,num[10];
    unsigned long long m;
    ifstream infile("input.txt");
    ofstream outfile("output.txt");
    infile>>t;
    for(k=1;k<=t;k++)
    {
        infile>>n;
        for(i=0;i<10;i++)
        {
            num[i]=0;
        }
        m=n;
        i=1;
        j=0;
        while(m>0)
        { m=i*n;
            while(m!=0)
            {
                r=m%10;
                if(num[r]==0)
                {   
                    num[r]=1;
                    j++;
                }
                m/=10;
            } 
           m=i*n; 
           if(j==10)
            break;  
          i++;
        }
        if(j==10)
         outfile<<"Case #"<<k<<": "<<m<<endl;
        else
         outfile<<"Case #"<<k<<": INSOMNIA"<<endl;
    }
    infile.close();
    outfile.close();
    return 0;
}
