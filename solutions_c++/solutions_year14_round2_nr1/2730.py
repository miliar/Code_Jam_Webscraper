#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    int t,n,arr[1000],var,vari,yes,i,ind,fina;
      long index;
    char a[1000][1000],temp[100];

    cin>>t;
    for(int k=1;k<=t;k++)
    {
     cin>>n;    
         fina=0;
     ind=0;   
          for(int i=0;i<n;i++)
          {
                  cin>>a[i];
                  a[i][999]='*';
                  
                  
          }  
          ind=0;
          do
          {
                  yes=0,var=0;
                  vari=0;
          for(i=0;i<n;i++)
          {
     
                        if(strlen(a[i])>vari && a[i][999]!='@')        
                          {
                              var=i;
                              vari=strlen(a[i]);  
                              yes=1;                               
                                                               
                          }
                     
                  
                        
                  
                  
          }
          
        
          arr[ind]=var;
          ind++;
                  a[var][999]='@';  
                  
                  
                  }
                  while(yes==1);
                  /* for(i=0;i<ind;i++)
          {cout<<arr[i]<<" ";
                           }
                  */
                  
                  long g,h;
            for(i=0;i<ind-2;i++)
            {
                    index=0;
                    int j=0;
                    while(j<strlen(a[arr[i+1]]))
                    {
                                      if(a[arr[i]][strlen(a[arr[i]])-1]!=a[arr[i+1]][strlen(a[arr[i+1]])-1])
          {
                                     goto u; 
                                      }          
                         //  cout<<a[arr[i]][index]<<" "<<a[arr[i+1]][j]<<endl;
                           
                          if(a[arr[i]][index]==a[arr[i+1]][j])
                          {
                              while(a[arr[i]][index]==a[arr[i+1]][j] && j<strlen(a[arr[i+1]]))
                                       {
                                       index++;   
                                       j++;                                   
                                       }                                 
                                                              
                                              j--;                
                                            index--;                  
                                            
                                            
                                            while(a[arr[i+1]][j]==a[arr[i+1]][j+1] && j<strlen(a[arr[i+1]]))
                                       {
                                       j++;  
                                       fina++;                                        
                                       }  
                                       j++;
                                       while(a[arr[i]][index]==a[arr[i]][index+1] && index<strlen(a[arr[i]]))
                                       {
                                       index++;   
                                       fina++;                                        
                                       }  
                                       
                                       
                                       
                                       //fina++;           
                                     index++; 
                                     g=i,h=j;              
                          }
                          else
                          {
                              u:
                          cout<<"Case #"<<k<<": Fegla Won";
                          goto y;    
                              
                          }
                            
                            
                    }
                  
            }
          if(a[arr[i]][strlen(a[arr[i]])-1]==a[arr[i+1]][strlen(a[arr[i+1]])-1])
          {
        
                          cout<<"Case #"<<k<<": "<<fina;
                          }
                          else
                          {
                              cout<<index<<endl;
                            cout<<"Case #"<<k<<": Fegla Won";   
                          }
            y:
                  cout<<endl;
    }

return 0;    
}
