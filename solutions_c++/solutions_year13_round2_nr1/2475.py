#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
    string s[4],t1;
    ifstream fin;
    ofstream fout;
    fin.open("cji1.txt");
    fout.open("cjo1.txt");
    int t,i,flag=0,a,k,m,u;
    int *r,n,j,a1,temp;
    fin>>t;
    getline(fin,s[0]);
    for(k=0;k<t;k++)
    {
        j=0;
        fin>>a>>n;
        getline(fin,s[0]);
        r=new int[n];
        for(i=0;i<n;i++)
            fin>>r[i];
        getline(fin,s[0]);
        sort(r,r+n);

        for(i=0;i<n;i++)
        {
            if(r[i]<a)
                a=a+r[i];
            else if(r[i]<a+a-1)
            {
                a=a+a-1+r[i];
                j++;
            }
            else
            {
                temp=a;
                m=1;
                flag=0;
                while(m+i<n)
                {
                    a=((a*(pow(2,(m+1))))-(pow(2,m+1)-1));
                    for(u=0;u<=m+1;u++)
                    {
                        if(r[u+i]<a)
                        {
                            a=a+r[u+i];
                            flag=1;
                            continue;
                        }
                        flag=0;
                        break;
                    }
                    if(flag==1)
                    {
                        i=i+m+1;
                        j=j+m+1;
                        break;
                    }
                    if(flag==0)
                    {
                        a=temp;
                        m++;
                    }

                }
                if(flag==0)
                {
                    j++;
                }

            }

        }
        fout<<"Case #"<<k+1<<": "<<j<<endl;
    }
    fout.close();
    return 0;
}
