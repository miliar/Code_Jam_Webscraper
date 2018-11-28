#include<iostream>
#include <sstream>
#include<math.h>
#include<string.h>
using namespace std;

int output(int r,int i)
    {
          cout<<"Case #"<<i+1<<": "<<r<<endl;
          return 0;
    }
    
int reverseint(int num_)
{
        int inv; inv = 0;

        while (num_>0)
        {
                inv = inv * 10 + (num_%10);
                num_ = num_ / 10;
        }

        return inv;
}

int pal(int k)
    {
        int l=0,a;
        string result;
        if((k%10)==0)
         return 1;
        a=reverseint(k);
        if(k==a)
        return 1;#include<iostream>
#include <sstream>
#include<math.h>
#include<string.h>
using namespace std;

int output(int r,int i)
    {
          cout<<"Case #"<<i+1<<": "<<r<<endl;
          return 0;
    }
    
int reverseint(int num_)
{
        int inv; inv = 0;

        while (num_>0)
        {
                inv = inv * 10 + (num_%10);
                num_ = num_ / 10;
        }
        return inv;
}

int pal(int k)
    {
        int l=0,a;
        string result;
        a=reverseint(k);
        if(k==a)
        return 1;
        else return 0;
        
    }
int check(int i,int a,int b)
    {
        int k,y=0;
        double s;
        for(k=a;k<=b;k++)
            {
                s=sqrt(k);                
                if(pal(k)==1 && int(s)==s &&  pal(s)==1)
                y++;
            }
        output(y,i);
        return 0;
    }   

int main()
    {
        int T,A,B;
        cin>>T;
        for(int i=0;i<T;i++)
            {
                cin>>A>>B;
                check(i,A,B);
            }
        return 0;
    }
        else return 0;
        
    }
int check(int i,int a,int b)
    {
        int k,y=0;
        double s;
        for(k=a;k<=b;k++)
            {
                cout<<sqrt(k);
                if(pal(k)==1 && pal(s)==1)
                y++;
            }
        output(y,i);
        return 0;
    }   

int main()
    {
        int T,A,B;
        cin>>T;
        for(int i=0;i<T;i++)
            {
                cin>>A>>B;
                check(i,A,B);
            }
        return 0;
    }