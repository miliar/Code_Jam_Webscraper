#include<iostream>
#include<map>
#include<vector>
#include<string>
#include<fstream>
using namespace std;

int main()
{
     
     vector<vector<string>  > t;
     vector<string> e;
    e.push_back("1");
    e.push_back("i");
    e.push_back("j");
    e.push_back("k");
    t.push_back(e);
    e.clear();
    e.push_back("i");
   e.push_back("-1");
   e.push_back("k");
    e.push_back("-j");
    t.push_back(e);
    e.clear();
     e.push_back("j");
     e.push_back("-k");
    e.push_back("-1");
      e.push_back("i");
      t.push_back(e);
      e.clear();
     e.push_back("k");
      e.push_back("j");
       e.push_back("-i");
      e.push_back("-1");
      t.push_back(e);
       map<char,int> g;
       g['1']=0;
       g['i']=1;
       g['j']=2;
       g['k']=3;
      ifstream in("C-small-attempt1.in");
      ofstream out("output.txt");
    int testcase;
    in>>testcase;
    for(int tt=0;tt<testcase;tt++)
    {
            
            out<<"Case #"<<(tt+1)<<": ";
            int sign=1;
       int s=0,f=0;
       in>>s>>f;
           string x;
           in>>x;
           string w;
           for(int i=0;i<f;i++)
           w+=x;
           char a,b;
           int flag=0;
           bool ii,jj,kk;
           ii=false;
           jj=false;
           kk=false;
            string res="1";
            int pos=0;
           for(int i=0;i<w.size();i++)
           {
                  
                  
                   if(ii==false && w[i]=='i' && sign==1 && flag==0)
                   {
                          
                      ii=true;
                      continue;
                      
                   }
                   if(ii==true && jj==false && w[i]=='j' && sign==1 && flag==0)
                   {
                            
                      jj=true;
                      continue;
                      
                   }
                   
                   if(ii==true && jj==true && kk==false && w[i]=='k' && sign==1 && flag==0)
                   {
                                          
                     
                                
                      kk=true;
                     if(ii==true && jj==true && kk==true)
                      pos=i;
                      continue;
                     
                     
                       
                     
                   }
                   
        
                   
                   if(flag==0)
                   {
                   
                   a=w[i];
                   }
                   if(flag==1) 
                      b=w[i];
                   if(flag==1)
                   {
                            
                              int indn,indm;
                              indn=g[a];
                              indm=g[b];
                              
                             
                            res=t[indn][indm];
                         
                          
                            if(res[0]!='-')
                            {
                                     w.insert(i+1,res);  
                            }
                            else
                            {
                                string ttt;
                                ttt+=res[1];
                                w.insert(i+1,ttt);
                              sign*=-1;
                            }
                            
                           
                    }
                   
                     if(flag==0)
                     flag=1;
                     else
                     flag=0;
                   
           }
           
          

            if(ii==true &&  jj==true && kk==true)
                     {
                            
                                
                                   if(pos==w.size()-1)
                                   out<<"YES"<<endl;
                                    else
                                    {
                                        if(res=="1" || res=="-1")
                                        {
                                                  if(sign==1)
                                                   out<<"YES"<<endl;
                                                   else
                                                   out<<"NO"<<endl;
                                                  
                                        }
                                        else
                                        out<<"NO"<<endl;
                                    }
                     }
                     else
                     out<<"NO"<<endl; 
                     
    }
}
