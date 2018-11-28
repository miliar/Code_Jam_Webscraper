#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<string>
#include<sstream>
#include<cstring>

using namespace std;

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

int main()
{

	 freopen ("myfile.txt","w",stdout);

    int t;
    cin>>t;
    
    for(int i=0;i<t;i++)
    {
        int A,B;
        int tot=0;
        
        cin>>A>>B;
        
        
        
        for(int j=A;j<=B;j++)
        {
                
                double tst=sqrt(j);
                
                if(tst==floor(tst))
                {
                    
                string s=convertInt(j);
                int l=s.length(),flg=1;
                
                
                for(int k=0;k<l/2;k++)
                {
                    if(s[k]!=s[l-k-1])flg=0;
                }
                                
                if(flg)
                {
                    int sqr=sqrt(j);
                    string s1=convertInt(sqr);
                    int l1=s1.length(),flg1=1;
                    
                    for(int k=0;k<l1/2;k++)
                    {
                        if(s1[k]!=s1[l1-k-1])flg1=0;
                    }
                
                    if(flg1){tot++;}
                }
             }
        }
        cout<<"Case #"<<i+1<<": "<<tot<<endl;
    }
}