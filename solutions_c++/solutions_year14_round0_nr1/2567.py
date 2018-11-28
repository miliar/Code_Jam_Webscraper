#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main()
{
    int t;
    ifstream ifile("A-small-attempt0.in");
    ifile>>t;
    ofstream ofile("out.txt");
    int tt=0;
    while(t--)
    {
              tt++;
              int a,b;
              int flag[17];
              for(int i=0;i<17;i++)
              flag[i]=0;
              ifile>>a;
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              int x;
                              ifile>>x;
                              if(i==a-1)
                              {
                                    flag[x]=1;    
                              }
                      }
              }
              ifile>>b;
              int found=0,no=-1;
              for(int i=0;i<4;i++)
              {
                      for(int j=0;j<4;j++)
                      {
                              int x;
                              ifile>>x;
                              if(i==b-1)
                              {
                                    if(flag[x]==1)
                                    {
                                             if(found==1 || found==2)
                                             found=2;
                                             else
                                             {
                                                
                                             no=x;
                                             found=1;
                                             }     
                                    }   
                              }
                      }
              }
             
              string s;
              char ch[256];
              char ch2[256];
              
              if(found==0)
              s=string("Case #") +itoa(tt,ch,10)+ (": Volunteer cheated!\n");
              else if(found==1)
              s=string("Case #")+itoa(tt,ch,10)+string(": ")+itoa(no,ch2,10)+string("\n");
              else
              s=string("Case #")+itoa(tt,ch,10)+string(": Bad magician!\n");
              ofile<<s;
    }
    
    //cin>>t;
}
