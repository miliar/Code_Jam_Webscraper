#include<iostream>
#include<fstream>
using namespace std;
ifstream fin("A-small-attempt0 (2).in");
ofstream fout("out.txt");
int main()
{
    int t,tc,n,*p,tot,ev[2],cnt,j,atot;
    char c;
    fin>>t;
    cout<<"test cases:"<<t<<endl;
    for(int tc=0;tc<t;tc++)
    {
        fout<<"Case #"<<tc+1<<": ";
        tot=0;
        fin>>n;
        p=new int[n];
        for(int i=0;i<n;i++)
        {
            fin>>p[i];
            tot=tot+p[i];
        }
        cout<<"No of parties"<<tc+1<<"  "<<n<<"  "<<tot<<endl;
        ev[0]=ev[1]=0;
       cnt=tot; //no of parties with strength
        while(tot>0)
        {
            j=0;
            ev[0]=ev[1]=99;
            atot=(tot-2)/2;
            for(int i=0;i<n;i++)
            {
                if(p[i]>atot)
                {
                    if(j<2)
                    {
                        ev[j]=i;
                        cout<<"hi";
                        j++;
                        p[i]--;
                    }
                    else
                    {
                        p[ev[1]]++;
                        cout<<p[ev[1]];
                        j--;
                    }
                }
            }
            if(j==0)
            {
                ev[j]=0;
                p[0]--;
                j++;
                ev[j]=1;
                p[1]--;
                j++;
            }
            for(int i=0;i<j;i++)
            {

                c=ev[i]+65;
                fout<<c;
                cout<<c;
            }
            fout<<" ";
            for(int i=0;i<n;i++)
                cout<<p[i]<<"  ";
            cout<<endl;
            if(j==1)
                tot--;
            else if(j==2)
                tot=tot-2;
            cout<<tot<<endl;
        }
        delete p;
        fout<<endl;
    }
    return 0;
}
