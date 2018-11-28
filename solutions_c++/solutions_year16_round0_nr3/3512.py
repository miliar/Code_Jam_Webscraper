#include<iostream>
#include<vector>
#include<math.h>
#include<fstream>
using namespace  std;
ofstream out("output.txt");
int nn;

bool valid(vector<int> a)
{
     for(int i=0;i<a.size();i++)
       if(a[i]==-1)
       return 0;
return 1;
}
string tobin(int number)
{
   
    string bin;
    char holder=' ';
    
    while(number!=0)
    {
        holder=number%2+'0';
        bin=holder+bin;
        number/=2;
    }
    return bin;
}
long long  pf(long long  n)
{
    // Print the number of 2s that divide n
   
    while (n%2 == 0)
    {
         
           return 2;
        n = n/2;
    }
      
    // n must be odd at this point.  So we can skip one element (Note i = i +2)
    for (long long i = 3; i <= sqrt(n); i = i+2)
    {
        // While i divides n, print i and divide n
        while (n%i == 0)
        {
              
            return  i;
            n = n/i;
        }
    }
 
    // This condition is to handle the case whien n is a prime number
    // greater than 2
    if (n > 2)
    {
          
              return -1;
    }
    return -1;
}

bool check(double x)
{
     long long y=int(x);
     for(int i=2;i<=sqrt(x);i++)
       if(y%i==0)
         return false;
         return true;
}
double bin(string x)
{
     int l=x.size()-1;
     int count=0;
     double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(2,count);
             count++;
     }
     return res;
}
double three(string x)
{
     int l=x.size()-1;
     int count=0;
    double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(3,count);
             count++;
     }
     return res;
}
double four(string x)
{
     int l=x.size()-1;
     int count=0;
     double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(4,count);
             count++;
     }
     return res;
}
double five(string x)
{
     int l=x.size()-1;
     int count=0;
     double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(5,count);
             count++;
     }
     return res;
}
double sex(string x)
{
     int l=x.size()-1;
     int count=0;
    double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(6,count);
             count++;
     }
     return res;
}
double sev(string x)
{
     int l=x.size()-1;
     int count=0;
    double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(7,count);
             count++;
     }
     return res;
}
double e(string x)
{
     int l=x.size()-1;
     int count=0;
     double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(8,count);
             count++;
     }
     return res;
}
double n(string x)
{
     int l=x.size()-1;
     int count=0;
     double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(9,count);
             count++;
     }
     return res;
}
double ten(string x)
{
     int l=x.size()-1;
     int count=0;
     double res=0;
     for(int i=l;i>=0;i--)
     {     
               if(x[i]=='1')
             res=res + pow(10,count);
             count++;
     }
     return res;
}

bool checkc(string x)
{
     double t=0;
      if(x[0]=='0' || x[x.size()-1]=='0')
      return false;
       t=bin(x);
      if(check(t)==true)
      return false;
       t=three(x);
      if(check(t)==true)
      return false; 
       t=four(x);
      if(check(t)==true)
      return false; 
       t=five(x);
      if(check(t)==true)
      return false; 
       t=sex(x);
      if(check(t)==true)
      return false; 
       t=sev(x);
      if(check(t)==true)
      return false; 
      t=e(x);
      if(check(t)==true)
      return false; 
       t=n(x);
      if(check(t)==true)
      return false;
       t=ten(x);
      if(check(t)==true)
      return false; 
      
     return true;  
}
vector<int> seq(string x)
{
            double y;
            long long num=0;
            vector<int> a;
             y=bin(x);
             num=pf((long long)y);
             
            a.push_back(num);
             y=three(x);
            num=pf((long long)y);
            
            a.push_back(num);
             y=four(x);
           num=pf((long long)y);
            a.push_back(num);
             y=five(x);
            num=pf((long long)y);
            a.push_back(num);
             y=sex(x);
            num=pf((long long)y);
            a.push_back(num);
             y=sev(x);
            num=pf((long long)y);
            a.push_back(num);
             y=e(x);
            num=pf((long long)y);
            a.push_back(num);
             y=n(x);
            num=pf((long long)y);
            a.push_back(num);
             y=ten(x);
           num=pf((long long)y);
            a.push_back(num);
            return a;
}


void f()
{
     int count=0;
     for(int i=0;i<=1000000;i++)
     {
             if(count==50)
             break;
          string x=tobin(i);
          if(x.size()==nn && x[0]!='0' && x[x.size()-1]!='0')
          {
              
              
                    vector<int> a=seq(x);
                    if(valid(a))
                    {
                               //ofstream out("output.txt");
                            out<<x<<" ";
                            for(int i=0;i<a.size();i++)
                            out<<a[i]<<" ";
                            out<<endl;
                            count++;
                   }       
              
          }
     }
     
}
int main()
{
    
    out<<"Case #1:"<<endl;
    
    string x;
     /*while(cin>>x)
     {
                   
                  bool r=checkc(x);
                   if(r==true)
                   {
                              cout<<endl;
                              vector<int> a;
                              a=seq(x);
                              for(int i=0;i<a.size();i++)
                              cout<<a[i]<<" ";
                              cout<<endl;
                   }
     }*/
      
      nn=16;
     f();
     cout<<"Done!"<<endl;
     int y;
     cin>>y;
}
