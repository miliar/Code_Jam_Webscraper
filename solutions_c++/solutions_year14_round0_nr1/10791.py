#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;
int main()
{
    
    ifstream in("input.txt");
    if(!in)
    {
          cout<<"Sorry!";
          getch();
          return 0;
    }
          
    ofstream out("output.txt");
    if(!out)
    {
          cout<<"Sorry";
          getch();
          return 0 ;
    }
                  
    int x;
    in>>x;
                  
    int y=x;
                  
    while(x--)
    {
                  int k;
                  in>>k;
                  int input[4];
                  int exit;
                  int r=4-k;
                  while(k--)
                  
                {
                            for(int i=0; i<4;i++)
                            in>>input[i];
                }
                                      
                                     
                while(r--)
                {
                     for(int i=0;i<4; i++)
                     in>>exit;
                }
                                                
                
                int p;
                in>>p;
                int input2[4];
                r=4-p;
                                                
                while(p--)
                
                {
                    for(int i=0;i<4;i++)
                    in>>input2[i];
                }
                 
                while(r--)
                    {
                          for(int i=0;i<4;i++)
                          in>>exit;
                          
                    }       
                                                          
                int cnt=0, num;
                for(int i=0;i<4;i++)
                {
                    for(int j=0;j<4;j++)
                
                   {
                
                        if(input[i]==input2[j])
                      {
                                num=input[i];
                                cnt++;
                                                                                                         
                      }
                   }
                
                }
                                                                                                         
                if(cnt==0)
                out<<"Case #"<<y-x <<": Volunteer cheated!"<<endl;
                else if (cnt==1)
                out<<"Case #"<<y-x<<": "<<num<<endl;
                else
                out<<"Case #"<<y-x<<": Bad magician!"<<endl;    
                }
                getch();
                } 
