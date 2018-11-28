#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
        ios_base::sync_with_stdio(0);
        ifstream fin("A-large.in",ios::in);
        ofstream fout("1_large.txt",ios::out);
        long long t,count=0;
        fin>>t;
        while(t--)
        {
                long long n,temp,x;
                fin>>n;
                x=n;
                count++;
                if(n==0)
                fout<<"Case #"<<count<<": INSOMNIA\n";
                else
                {
         
                        long long digit[10],flag=0,c=2;
                        for(long long i=0;i<10;i++)
                        digit[i]=0;
                        while(!flag)
                        {
                                temp=n;
                                flag=1;
                                do
                                {
                                        digit[temp%10]++;
                                        temp/=10;
                                }while(temp>0);
                                for(long long i=0;i<10;i++)
                                {
                                        if(digit[i]==0)
                                        {
                                                flag=0;
                                                break;
                                       }        
                        
                               }
                               if(flag==1)
                               
                               fout<<"Case #"<<count<<": "<<n<<"\n";
                               n=c*x;
                                c++;
                        
                
                         }
                }
        }
  }      
