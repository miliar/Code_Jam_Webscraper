#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
        ios_base::sync_with_stdio(0);
        ifstream fin("B-large.in",ios::in);
        ofstream fout("2_large.txt",ios::out);
        int t,count=0;
        fin>>t;
        while(t--)
        {
                string s;
                int i=0,flag=0,flip=0,countplus=0,countminus=0;
                fin>>s;
                count++;
                for(int i=0;i<s.length();i++)
                {
                        if(s[i]=='+')
                        countplus++;
                        else if(s[i]=='-')
                        countminus++;
                 }
                 if(countplus==s.length())
                 fout<<"Case #"<<count<<": 0\n"; 
                 else if(countminus==s.length())
                 fout<<"Case #"<<count<<": 1\n"; 
                 else
                 {       
                        
                        while(!flag)
                        {
                                flag=1;
                                if(s[0]=='+')
                                {
                                        while(s[i]!='-')
                                                i++;
                                         for(int j=0;j<i;j++)
                                         {
                                              s[j]='-';
                                              
                                          }
                                          flip++;
                                         for(int k=1;k<s.length();k++)
                                         {
                                                if(s[k]!=s[k-1])
                                                {
                                                        flag=0;
                                                        break;
                                                }
                                         }
                                  }
                                else if(s[0]=='-')       
                                {
                                        while(s[i]!='+')
                                                i++;
                                         for(int j=0;j<i;j++)
                                         {
                                              s[j]='+';
                                      
                                          }
                                          flip++;
                                         for(int k=1;k<s.length();k++)
                                         {
                                                if(s[k]!=s[k-1])
                                                {
                                                        flag=0;
                                                        break;
                                                }
                                         }
                                 }  
                      } 
                        if(s[0]=='-')
                        fout<<"Case #"<<count<<": "<<flip+1<<"\n"; 
                        else if(s[0]=='+')
                        fout<<"Case #"<<count<<": "<<flip<<"\n";  
               }
      }
      }                       
                              
                                       
                        
