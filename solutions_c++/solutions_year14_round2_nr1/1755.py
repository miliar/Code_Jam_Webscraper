#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string>
#include<malloc.h>
#include<limits.h>
#include<algorithm>
using namespace std;
struct game
{
    char *c;
    int *f;
};
int encode(struct game &a,string str)
{
    //cout<<"Hello\n";
    int len=str.length();
    a.c=new char[len];
    a.f=new int[len];
    int j=0;
    int i=0;
    for(i=0;i<len;i++)
    {
        //cout<<"Yes\n";
        int ct=1;
        a.c[j]=str[i];
        while(i+1<len && str[i]==str[i+1])
        {
            ct++;
            i++;
        }

        a.f[j]=ct;
        j++;
    }
    return j;
}
int main()
{
    ifstream fil;
    ofstream file;
    file.open("out.txt");
    fil.open("A-large.in");
    int t;
    fil>>t;
    //cout<<t;
    //getchar();
    for(int z=1;z<=t;z++)
    {
        int n;
        fil>>n;
        struct game arr[n];
        string str;
        fil>>str;
        //cout<<str;
        //getchar();
        int len=encode(arr[0],str);
        //cout<<len;
        //getchar();
        int flag=0;
        for(int i=1;i<n;i++)
        {
            fil>>str;
            int init=encode(arr[i],str);
            if(init!=len)
            {
                flag=1;
            }
        }
        //cout<<"khchiucxh iu\nn v";
        //getchar();
        if(flag==1)
        {
            //cout<<"knkjn  \n";
            //getchar();
            file<<"Case #"<<z<<": Fegla Won\n";
            continue;
        }
        else
        {
            //cout<<"mckj c\n";
            //getchar();
            for(int i=0;i<len;i++)
            {
                //cout<<"bkdjbkdv\n";
                char temp=arr[0].c[i];
                //cout<<temp<<"\n";
                for(int j=1;j<n;j++)
                {
                    if(arr[j].c[i]!=temp)
                    {
                        flag=1;
                        break;
                    }
                }
                if(flag==1)
                {

                    break;
                }
            }
            if(flag==1)
            {
                file<<"Case #"<<z<<": Fegla Won\n";
                continue;
            }
            //cout<<"Yea\n";
            int final_ans=0;
            int temp;
            /*for(int i=0;i<n;i++)
            {
                temp=0;
               for(int j=0;j<n;j++)
               {
                    for(int k=0;k<len;k++)
                    {
                        temp+=abs(arr[j].f[k]-arr[i].f[k]);
                        if(temp>ans)
                        {
                            flag=1;
                            break;
                        }
                        if(flag==1)
                        break;
                    }
               }
               if(temp<ans)
               ans=temp;
            }*/
            for(int i=0;i<len;i++)
            {
                int ans=INT_MAX;

                for(int j=0;j<n;j++)
                {
                    temp=0;
                    int flag=0;
                    int num=arr[j].f[i];
                    for(int k=0;k<n;k++)
                    {
                        temp+=abs(arr[k].f[i]-arr[j].f[i]);
                        if(temp>ans)
                        {
                            flag=1;
                            break;
                        }
                    }
                    if(flag==0)
                    if(temp<ans)
                    ans=temp;
                }
                final_ans+=ans;
            }
            file<<"Case #"<<z<<": "<<final_ans<<"\n";
        }
    }
    return 0;
}
