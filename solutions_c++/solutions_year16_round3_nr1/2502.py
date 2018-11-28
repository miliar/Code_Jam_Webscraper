#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<fstream>
#define F0(i,n) for(int i=0;i<n;i++)
using namespace std;
int break1=0,n=0;
int a[26][2];
bool check(int i,int j)
{
    int b[n][2],sum=0;
    F0(ii,n)
    {
        b[ii][0]=a[ii][0];
        b[ii][1]=a[ii][1];
    }
    b[i][1]--;
    if(j!=-1)
        b[j][1]--;
    F0(ii,n)
        sum+=b[ii][1];
    F0(ii,n)
    {
        if(b[ii][1]>sum/2)
            return false;
    }
    return true;
}
void update()
{
    /*F0(i,n)
        cout<<a[i][0]<<" "<<a[i][1]<<endl;*/
    F0(i,n)
    {
        if(a[i][1]<=0&&n>1)
        {
            for(int j=i;j<n;j++)
            {
                a[j][0]=a[j+1][0];
                a[j][1]=a[j+1][1];
            }
            n--;
        }
        else if(n==1&&a[i][1]<=0)
        {
            break1=1;
            n--;
        }

    }
}
int main()
{
    ifstream fin("A-large.in");
    ofstream fout("output.txt");
    int t;
    fin>>t;
    F0(co,t)
    {
        F0(i,26)
        {
            a[i][0]=0;
            a[i][1]=0;
        }
        fin>>n;
        F0(i,n)
        {
            a[i][0]=i;
            fin>>a[i][1];
        }
        fout<<"Case #"<<co+1<<": ";
        while(break1==0)
        {
            char A='A';
            F0(i,n)
            {
                F0(j,n)
                {
                    if(i==j)
                    {
                        if(a[i][1]>1)
                        {
                        if(check(i,i))
                        {
                            a[i][1]=a[i][1]-2;
                            fout<<(char)(A+a[i][0])<<(char)(A+a[i][0])<<" ";
                            goto stop;
                        }}
                        else if(a[i][1]>0)
                        {
                            if(check(i,-1))
                            {
                                a[i][1]--;
                                fout<<(char)(A+a[i][0])<<" ";
                                goto stop;
                            }
                        }
                    }
                    else
                    {
                        if(a[i][1]>0&&a[i][1]>0)
                        {
                            if(check(i,j))
                            {
                                a[i][1]--;
                                a[j][1]--;
                                fout<<(char)(A+a[i][0])<<(char)(A+a[j][0])<<" ";
                                goto stop;
                            }
                        }
                    }
                }
            }
            stop:
            update();
        }
        break1=0;
        fout<<endl;
    }

}
