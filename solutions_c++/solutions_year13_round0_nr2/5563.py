#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    std::ifstream infile("input1.txt");
    std::ofstream output("output1.txt");
    int T;
     infile>>T;
     int x;
 for(x=1;x<=T;++x)
 {
          int n,m,i,j;
          infile>>n>>m;
          int mat[n][m];
          int seen[n][m];
          int temp[n][m];


          for(i=0;i<n;++i)
          {
                          for(j=0;j<m;++j)
                          {
                           seen[i][j]=0;
                          }
          }

          for(i=0;i<n;++i)
          {
                          for(j=0;j<m;++j)
                          {
                                          infile>>mat[i][j];
                                          temp[i][j]= mat[i][j];
                          }
          }
         // for(i=0;i<n;++i)
//          {
//                          for(j=0;j<m;++j)
//                          {
//                           cout<<mat[i][j]<<" ";
//                           
//           
//                          }
//            cout<<endl;
//          }
//          
//          
//          
//                    for(i=0;i<n;++i)
//          {
//                          for(j=0;j<m;++j)
//                          {
//                           cout<<temp[i][j]<<" ";
//                           
//           
//                          }
//            cout<<endl;
//          }
//          
//          
//          
//          
         
          int alarm=0;
           int max;
          for(i=0;i<n;++i)
          {
                  max= -1; 
                     for(j=0;j<m;++j)
                          {
                                     if(temp[i][j]>max && seen[i][j] == 0)
                                                      max= temp[i][j];      
                //                                      cout<< i << " " << j << " " <<"max is " << max<<endl;           
                                     
                          }
                  //        cout<<i << " " << j <<" update " <<endl;
                          
                      for(j=0;j<m;++j)
                          {
                                      if(mat[i][j] == max )
                                                   seen[i][j]=1;
                                      if(mat[i][j]<max)
                                                       temp[i][j] = max;
                                       if(mat[i][j]>max)
                                       {     
                                       alarm = 1;
                    //                      cout<< i << " " << j << " " <<"ssssssssalarm " << alarm<<endl;           
                                        break;
                                        }
                                 
                                 
                                 
                          }
           
               
           
           }
           
           
            int y;
          for(i=0;i<n;++i)
          {
                     if(alarm==1)
                          break;
                  //   max = -1;
                     for(j=0;j<m;++j)
                          {
                                    
                                    if(mat[i][j]!=temp[i][j])
                                    {
                                         int p= mat[i][j];
                                          for(y=0;y<n;++y)
                                             {
                                               if(mat[y][j] !=p)
                                                  {
                                                            alarm=1;
                                                            break;
                                                  }
                                               }
                                               
                                                          
                                                          
                                         }  
                                                             
                                                             
                                                             
                          }
                                    
                                     
           
               
           
           }
           
           
           
           
           
           
           if(alarm ==1)
           output<<"Case #"<<x<<": NO"<<endl;
           else 
           output<<"Case #"<<x<<": YES"<<endl;
           
 }//while T--   
    
    
    
    
    system("pause");
    return 0;
}
