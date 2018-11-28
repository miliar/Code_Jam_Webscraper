#include<iostream>
#include<map>
#include<fstream>
using namespace std;
map<int,int> a;
void fun(long long y)
{
             
            while(y!=0)
             {
                       int m=y%10;
                      if(m==0)
                       a[0]=1;
                       if(m==1)
                       a[1]=1;
                       if(m==2)
                       a[2]=1;
                       if(m==3)
                       a[3]=1;
                       if(m==4)
                       a[4]=1;
                       if(m==5)
                       a[5]=1;
                       if(m==6)
                       a[6]=1;
                       if(m==7)
                       a[7]=1;
                       if(m==8)
                       a[8]=1;
                       if(m==9)
                       a[9]=1;
                       y/=10;
             }
                   
}
bool check()
{
     bool f=true;
     for(int i=0;i<=9;i++)
         if(a[i]==0)
         f=false;
         return f;
}
void print()
{
     for(int i=0;i<=10;i++)
       cout<<a[i]<<" ";
       cout<<endl;
}
int main()
{
    ifstream in("A-large.in");
    ofstream out("output.txt");
    int testcase;
    in>>testcase;
    for(int t=0;t<testcase;t++)
    {
            
            a.clear();
            long long x,y;
            in>>x;
            out<<"Case #"<<(t+1)<<": ";
            if(x==0)
            {
            out<<"INSOMNIA"<<endl;
            continue;
            }
            y=x;
            fun(x);
            
            int count=2;
             bool bb=false;
             while(bb!=true)
             {
                  x=y*count;
                  fun(x);
                  if(check()==true)
                  bb=true;
                count++;
                  
                          
             }
             out<<x<<endl;
    }
    
}
