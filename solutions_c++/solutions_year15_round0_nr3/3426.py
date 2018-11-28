#include<bits/stdc++.h>
using namespace std;
char a[10001];
int b[10001],c[10001][10001];
int main()
{
    int t,l,x,y,z,i,j,k,t1,flag;
    cin>>t;
    t1=t;
    while(t--)
    {
        cin>>l>>x>>a;

        for(j=0;j<x;j++)
        for(i=0;i<l;i++)
        {
            b[i+(j*l)]=int(a[i]);
        }
        for(i=0;i<l*x;i++)
        {
            for(j=i;j<l*x;j++)
            {
                if(i==j)
                {c[i][j]=b[i];}

                if(b[j]==105)   //i
                {
                    if(c[i][j-1]==106)  //j
                    {
                        c[i][j]=-107;
                    }
                    if(c[i][j-1]==-106)  //-j
                    {
                        c[i][j]=107;
                    }
                    if(c[i][j-1]==107)     //k
                    {
                        c[i][j]=106;
                    }
                    if(c[i][j-1]==-107)     //-k
                    {
                        c[i][j]=-106;
                    }
                    if(c[i][j-1]==105)      //i
                    {
                        c[i][j]=-1;
                    }
                    if(c[i][j-1]==-105)     //-i
                    {
                        c[i][j]=1;
                    }
                    if(c[i][j-1]==1)         //1
                    {
                        c[i][j]=b[j];
                    }
                    if(c[i][j-1]==-1)      //-1
                    {
                        c[i][j]=b[j]*(-1);
                    }

                }

                if(b[j]==106)   //j
                {
                    if(c[i][j-1]==106)  //j
                    {
                        c[i][j]=-1;
                    }
                    if(c[i][j-1]==-106)  //-j
                    {
                        c[i][j]=1;
                    }
                    if(c[i][j-1]==107)     //k
                    {
                        c[i][j]=-105;
                    }
                    if(c[i][j-1]==-107)     //-k
                    {
                        c[i][j]=105;
                    }
                    if(c[i][j-1]==105)      //i
                    {
                        c[i][j]=107;
                    }
                    if(c[i][j-1]==-105)     //-i
                    {
                        c[i][j]=-107;
                    }
                    if(c[i][j-1]==1)         //1
                    {
                        c[i][j]=b[j];
                    }
                    if(c[i][j-1]==-1)      //-1
                    {
                        c[i][j]=b[j]*(-1);
                    }

                }

                if(b[j]==107)   //k
                {
                    if(c[i][j-1]==106)  //j
                    {
                        c[i][j]=105;
                    }
                    if(c[i][j-1]==-106)  //-j
                    {
                        c[i][j]=-105;
                    }
                    if(c[i][j-1]==107)     //k
                    {
                        c[i][j]=-1;
                    }
                    if(c[i][j-1]==-107)     //-k
                    {
                        c[i][j]=1;
                    }
                    if(c[i][j-1]==105)      //i
                    {
                        c[i][j]=-106;
                    }
                    if(c[i][j-1]==-105)     //-i
                    {
                        c[i][j]=106;
                    }
                    if(c[i][j-1]==1)         //1
                    {
                        c[i][j]=b[j];
                    }
                    if(c[i][j-1]==-1)      //-1
                    {
                        c[i][j]=b[j]*(-1);
                    }

                }

                //cout<<c[i][j]<<" ";
            }//cout<<endl;
        }
        flag=0;
        for(j=0;j<(l*x-2);j++)       // 1st partition c[0][j] should be i==105
        {
            if(c[0][j]==105)
            {
                for(k=j+1;k<(l*x-1);k++)
                {
                    if(c[j+1][k]==106)
                    {
                        if(c[k+1][l*x-1]==107)
                        {
                            cout<<"Case #"<<t1-t<<": YES"<<endl;
                            flag=1;
                            break;
                        }
                    }
                }
                if(flag==1)
                {break;}
            }
        }
        if(flag==0)
        {
            cout<<"Case #"<<t1-t<<": NO"<<endl;
        }
    }
}
