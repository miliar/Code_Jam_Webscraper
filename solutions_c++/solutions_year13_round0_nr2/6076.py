#include<iostream>
#include<fstream>
#include<ctime>
//#include<vector>
using namespace std;

//int hcheck()
//int vcheck()
int main()
{ 
    int T,t=0,n,m,t1;
    int yn=0,nn=0;
    //int count=0;
    ifstream fin;
    fin.open("input.txt");
    ofstream fout;
    fout.open("result.txt");
    fin>>T;
    while(t<T)
    {
              fin>>n>>m;
              //vector<int> v[n](m);
              int rows1 = n;
              int columns1 = m;
              int **v = (int**)malloc(rows1 * sizeof(*v));
	          for(int i = 0; i < rows1; i++)
	          {
		           v[i] = (int*)malloc(columns1 * sizeof(int));
              }
              //fout<<"rows :"<<rows1<<"\t"<<"columns :"<<columns1<<endl;
              int temp;
              for(int i=0;i<n;i++)
              {
                      for(int j=0;j<m;j++)
                      {
                              fin>>v[i][j];
                              //fout<<v[i][j];
                                            
                              
                      }
                      //fout<<"\n";
              }
              if(m != 1 && n != 1)
              {              
                /*for(int i=0;i<n;i++)
                {
                      for(int j=0;j<m;j++)
                      {
                              if(v[i][j]==2)
                              {
                                            ++count;
                                            v[i][j]=0;
                              }
                      }
                }
                fout<<" \n number of 2's"<<count<<endl;*/
                for(int i=0;i<m;i++)
                {
                      if(v[0][i]==1)
                      {             
                                    int temp=0;
                                    for(int j=1;j<n;j++)
                                    {
                                            if(v[j][i]==1)
                                            {
                                                          ++temp;
                                            }
                                    }
                                    //fout<<"\n verti "<<temp<<"\n";
                                    if(temp==(n-1))
                                    {
                                               for(int j=0;j<n;j++)
                                               {
                                                       v[j][i]=0;
                                               }
                                    }
                                    
                      }
                  }
                  for(int i=0;i<n;i++)
                  {
                      if(v[i][0]==1 || v[i][0]==0)
                      {
                                    int temp=0;
                                    for(int j=1;j<m;j++)
                                    {
                                            if(v[i][j]==1 || v[i][j]==0)
                                            {
                                                          ++temp;
                                            }
                                    }
                                    //fout<<"\n hori "<<temp<<"\n";
                                    if(temp==(m-1))
                                    {
                                               for(int j=0;j<m;j++)
                                               {
                                                       v[i][j]=0;
                                               }
                                    }
                                    
                      }
                  }
                  int temp4=0;
                  for(int i=0;i<n;i++)
                  {
                          for(int j=0;j<m;j++)
                          {
                                  if(v[i][j]==1)
                                  {
                                               ++temp4;
                                  }
                          }
                  }
                        
                                               
                  t1=t+1;
                  //fout<<"\n count :"<<count<<"\n";
                  if(temp4==0)
                  {
                       fout<<"Case #"<<t1<<": YES \n";
                       //fout<<"Case #"<<t1<<": YES \n";
                       ++yn;
                  }
                  else
                  {
                    fout<<"Case #"<<t1<<": NO \n";
                    //fout<<"Case #"<<t1<<": NO \n";
                    ++nn;
                  }
                  //count=0;
                  ++t;
             }
             else
             {
                 t1=t+1;
                 fout<<"Case #"<<t1<<": YES \n";
                 //cout<<"Case #"<<t1<<": YES \n";
                 ++yn;
                 //count=0;
                 ++t;
             }
    }
    
    cout<<"number of yes's "<<yn<<endl;
    cout<<"number of no's "<<nn<<endl;
    fin.close();
    fout.close();
    cin>>T;
    return(0);
}
                       
                                    
                                                          
                                    
                      
              
              
                                        
                                               
                                                          
                                                          
                                            
                              
                              
    
    

