#include<iostream>
#include<cstring>
#include<fstream>
#include<cmath>

using namespace std;

bool str[100],str1[100];
unsigned long long convert(bool s[],int c,unsigned long long n)
{
//int x;
    unsigned long long p=0;
    unsigned long long g=1;
    //cout<<"called"<<g;
    for(long long i=n-1;i>=0;i--)
    {
        p=p+(s[i]*g);
        g=g*c;
    }
    return p;
}
void update(long long first,long long n)
{

    for(long long i=n-2;i>=1;i--)
    {
        str[i]=first%2;
        first=first/2;
    }


}
int main()
{
    ifstream fin;
    ofstream fout("out.txt");
    fin.open ("in.in");
    bool st[]={1,0,0,0,1,1};
    if(!fin.is_open())
    {
        cout<<"file error";
    }
    else
    {
        unsigned long long q,t,n,j,s,x,cou=0,arr[9],first,last,k,flag;
        fin>>t;
        s=t;
        while(t--)
        {
            fout<<"Case #"<<s-t<<": "<<endl;
            fin>>n>>q;

            for(long long i=0;i<n;i++)
            {
                if(i==0 ||i==n-1)
                {
                    str[i]=1;
                }
                else
                str[i]=0;
                str1[i]=1;
            }
            first=convert(str,2,n);
            last=convert(str1,2,n);
            //cout<<first<<" "<<last;
            for(int l=0;l<q;)
            {
                fill_n(arr,9,0);
                for(int i=2;i<=10;i++)
                {
                    k=0;
                    x=convert(str,i,n);
                    cout<<x<<" ";
                    for(int j=2;j<=sqrt(x);j++)
                    {
                        if(x%j==0)
                        {
                            k++;
                            break;
                        }
                    }
                    if(k==1)
                        arr[i-2]=x;

                }
                flag=0;
                for(int i=0;i<9;i++)
                    if(arr[i]==0)
                    flag++;
                if(flag==0)
                    {
                        for(long long i=0;i<n;i++)
                        fout<<str[i];
                        fout<<" ";
                        for(int i=0;i<9;i++)
                        {

                            for(int j=2;j<arr[i];j++)
                            {
                                if(arr[i]%j==0)
                                {
                                    fout<<arr[i]/j<<" ";
                                    break;
                                }
                            }
                        }
                        fout<<endl;
                        l++;
                    }

                update(first++,n);


            }
        }
        fin.close();
        fout.close();
    }
}
