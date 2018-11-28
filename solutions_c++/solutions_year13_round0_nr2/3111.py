#include<cstdlib>
#include <iostream>
using namespace std;
int N, M;

bool checkv(int* arr, int ht, int x, int y)
{
     bool fl=true;
     for(int i=0; i< N; i++)
     {
             if(arr[i*M+y]>ht)
              {
                  fl=false;
                  break;
              } 
     }
     if(fl)
        return fl;
     fl=true;   
     for(int i=0; i< M; i++)
     {
             if(arr[x*M+i]>ht)
              {
                  fl=false;
                  break;
              } 
     }
     return fl;
}
int main()
{
    int T;
    cin>>T;
    
    for(int k=0; k< T; k++)
    {
            bool imp=false;
            cin>>N;
            cin>>M;
            int arr[N][M];
            for(int i=0; i< N; i++)
               for(int j=0; j< M; j++)
                   cin>>arr[i][j];
            int max=1, min=100;      
            for(int i=0; i< N; i++)
               for(int j=0; j< M; j++)
               {
                   //cin>>arr[i][j]; 
                   if(arr[i][j]> max)
                      max=arr[i][j];
                   if(arr[i][j]< min)
                      min=arr[i][j];   
               }
               if(min!=max)
               {
            for(int i=0; i< N; i++)
               for(int j=0; j< M; j++)
               {
                       if(arr[i][j]!=max)
                       {
                                if(!checkv(&arr[0][0], arr[i][j], i, j))
                                {
                              
                                    imp=true;
                                    i=N;
                                    break;
                                }      
                       }    
               }
               }
               else 
                 imp=false;
           char sol[25];
           sprintf(sol,"Case #%d: ",k+1);
           if(imp)
              strcat(sol, "NO");
           else       
              strcat(sol, "YES");
          cout<<sol<<endl;     
    }
    return 0;
}
