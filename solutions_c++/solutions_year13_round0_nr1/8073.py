#include<iostream>
#include<fstream>

using namespace std;


int main()
{
    ifstream in;
    in.open("A-small-attempt0.in");
    ofstream out;
    out.open("output.txt");
    int test;
    in>>test;
   // 6<<test;
   // system("pause");
    char arr[4][4];
    bool X= false;
    bool Y=false;
    bool dot=false;
    int left=test;
    test=1;
    
    while(left!=0)
    {            
                 for(int i=0; i<4; i++)
                 {
                         for(int j=0; j<4; j++)
                         {
                              in>>arr[i][j];
                         }        
                 }
               int j=0;
               
                 for(int i=0; i<4 && X==false; i++)
                 {
                      //   for(int j=0; j<4; j++)
                      //   {
                           j=0;
                          if(Y==false &&X==false)
                              if(arr[i][j]=='X' || arr[i][j]=='T')
                              {
                                         j++;
                                               if(arr[i][j]=='X' || arr[i][j]=='T')
                                               {
                                               j++;
                                                    if(arr[i][j]=='X' || arr[i][j]=='T')
                                                    {
                                                       j++;
                                                       if(arr[i][j]=='X' || arr[i][j]=='T')
                                                       {
                                                                         
                                                        out<<"Case #"<<test<<": X won"<<endl;
                                                           X=true;      
                                                        }
                                                    }             
                                               }
                                                
                              }
                      //   }        
                 }
                 
                 
                 for(int i=0; i<4 && Y==false; i++)
                 {
                      //   for(int j=0; j<4; j++)
                      //   {
                           j=0;
                          if(Y==false &&X==false)
                              if(arr[i][j]=='O' || arr[i][j]=='T')
                              {
                                         j++;
                                               if(arr[i][j]=='O' || arr[i][j]=='T')
                                               {
                                               j++;
                                                    if(arr[i][j]=='O' || arr[i][j]=='T')
                                                    {
                                                       j++;
                                                       if(arr[i][j]=='O' || arr[i][j]=='T')
                                                       {
                                                                         
                                                        out<<"Case #"<<test<<": O won"<<endl;
                                                           Y=true;      
                                                        }
                                                    }             
                                               }
                                                
                              }
                      //   }        
                 }
                 
                 
                 
                 
                 for(int i=0; i<4 && X==false; i++)
                 {
                      //   for(int j=0; j<4; j++)
                      //   {
                           j=0;
                          if(Y==false &&X==false)
                              if(arr[j][i]=='X' || arr[i][j]=='T')
                              {
                                         j++;
                                               if(arr[j][i]=='X' || arr[i][j]=='T')
                                               {
                                               j++;
                                                    if(arr[j][i]=='X' || arr[i][j]=='T')
                                                    {
                                                       j++;
                                                       if(arr[j][i]=='X' || arr[i][j]=='T')
                                                       {
                                                                         
                                                        out<<"Case #"<<test<<": X won"<<endl;
                                                           X=true;      
                                                        }
                                                    }             
                                               }
                                                
                              }
                      //   }        
                 }
                 
                 
                 for(int i=0; i<4 && Y==false; i++)
                 {
                      //   for(int j=0; j<4; j++)
                      //   {
                           j=0;
                           if(Y==false &&X==false)
                              if(arr[j][i]=='O' || arr[j][i]=='T')
                              {
                                         j++;
                                               if(arr[j][i]=='O' || arr[j][i]=='T')
                                               {
                                               j++;
                                                    if(arr[j][i]=='O' || arr[j][i]=='T')
                                                    {
                                                       j++;
                                                       if(arr[j][i]=='O' || arr[j][i]=='T')
                                                       {
                                                                         
                                                        out<<"Case #"<<test<<": O won"<<endl;
                                                           Y=true;      
                                                        }
                                                    }             
                                               }
                                                
                              }
                      //   }        
                 }
                 
                      int i=0; 
                      j=0;
                       if(Y==false &&X==false)
                      if(arr[j][i]=='O' || arr[j][i]=='T' && Y==false)
                              {
                                         j++;i++;
                                               if(arr[j][i]=='O' || arr[j][i]=='T')
                                               {
                                         i++;     j++;
                                                    if(arr[j][i]=='O' || arr[j][i]=='T')
                                                    {
                                              i++;         j++;
                                                       if(arr[j][i]=='O' || arr[j][i]=='T')
                                                       {
                                                                        
                                                        out<<"Case #"<<test<<": O won"<<endl;
                                                           Y=true;      
                                                        }
                                                    }             
                                               }
                                                
                              }
                              
                      i=3; 
                      j=0;
                     if(Y==false &&X==false)
                      if(arr[j][i]=='O' || arr[j][i]=='T' && Y==false)
                              {
                                         j++;i--;
                                               if(arr[j][i]=='O' || arr[j][i]=='T')
                                               {
                                         i--;     j++;
                                                    if(arr[j][i]=='O' || arr[j][i]=='T')
                                                    {
                                              i--;         j++;
                                                       if(arr[j][i]=='O' || arr[j][i]=='T')
                                                       {
                                                                         
                                                        out<<"Case #"<<test<<": O won"<<endl;
                                                           Y=true;      
                                                        }
                                                    }             
                                               }
                                                
                              }   
                         
                 
                 i=0; 
                      j=0;
                      if(Y==false &&X==false)
                      if(arr[j][i]=='X' || arr[j][i]=='T' && X==false)
                              {         
                                         j++;i++;
                                               if(arr[j][i]=='X' || arr[j][i]=='T')
                                               {
                                         i++;     j++;
                                                    if(arr[j][i]=='X' || arr[j][i]=='T')
                                                    {
                                              i++;         j++;
                                                       if(arr[j][i]=='X' || arr[j][i]=='T')
                                                       {
                                                                         
                                                        out<<"Case #"<<test<<": X won"<<endl;
                                                           X=true;      
                                                        }
                                                    }             
                                               }
                                                
                              }
                              
                      i=3; 
                      j=0;
                      if(Y==false &&X==false)
                      if(arr[j][i]=='X' || arr[j][i]=='T' && X==false)
                              {
                                         j++;i--;
                                               if(arr[j][i]=='X' || arr[j][i]=='T')
                                               {
                                         i--;     j++;
                                                    if(arr[j][i]=='X' || arr[j][i]=='T')
                                                    {
                                              i--;         j++;
                                                       if(arr[j][i]=='X' || arr[j][i]=='T')
                                                       {
                                                                         
                                                        out<<"Case #"<<test<<": X won"<<endl;
                                                           X=true;      
                                                        }
                                                    }             
                                               }
                                                
                              }
                 
           
                  if(X==false && Y==false && dot==false)
                  {
                      for(int i=0; i<4 && dot==false; i++)
                      {
                              if(dot==false);
                         for(int j=0; j<4 && dot==false; j++)
                         {
                              if(arr[i][j]=='.')
                              dot=true;
                         }                  
                                        
                      }
                      if(dot==true)
                      {
                              out<<"Case #"<<test<<": Game has not completed"<<endl;      
                      }
                      else
                      {
                              out<<"Case #"<<test<<": Draw"<<endl;
                      }
                  }
                  
    left--;
     test++;
     X= false;
     dot=false;
     Y=false;              
    }
    in.close();
    out.close();
    system("pause");
return 0;    
    
}
