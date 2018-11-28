#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <bitset>
#include <list>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <functional>
#include <utility>
#include <ctime>
#include <numeric>
#include <iomanip>
#include <stdexcept>
#include <cmath>
#include <algorithm>



using namespace std;



class ABC
{
   struct pair
   {
      int r,c;
   };
   int **mat;
   int **done;
   int N,M;
   int *row, *col;
   queue<pair> myQ;
   int MAX;


public:
   
   ABC(int n, int m)
   {
     cout<<"const"<<endl;
     int i;
     N = n;
     M = m;

     mat = (int**)malloc(sizeof(int*)*N);
      for(i = 0; i<N; i++)
         mat[i] = (int *)malloc(sizeof(int)*M);

      done = (int**)malloc(sizeof(int*)*N);
      for(i = 0; i<N; i++)
      {
         done[i] = (int *)malloc(sizeof(int)*M);
         for(int j = 0; j<M; j++)         
           done[i][j] = 0;
      }


      row = (int *)malloc(sizeof(int)*N);
      for(i = 0; i<N; i++)
         row[i] = 0;

      col = (int *)malloc(sizeof(int)*M);
      for(i = 0; i<M; i++)
         col[i] = 0;

      MAX = 0;
   }

   ~ABC()
   {
      cout<<"deconst"<<endl;
      free(mat);
      free(done);
      free(row);
      free(col);
   }

   int add(int item, int i, int j)
   {
       mat[i][j] = item;     
       if(item > MAX)
       {
           if(myQ.empty())
           {
//               cout<<"added1"<<endl;
               pair p;
               p.r = i;
               p.c = j;
               myQ.push(p);
           } 
           else
           {
               while(!myQ.empty())
                  myQ.pop();

  //             cout<<"added2"<<endl;
               pair p;
               p.r = i;
               p.c = j;
               myQ.push(p);
                
           }
           MAX = item;
       } 
   }
  
   int display()
   {
//      FILE *fp = fopen("hello.txt","a");
      for(int i=0;i<N;i++)
      {   for(int j=0;j<M;j++)
          {cout<<mat[i][j]<<",";
  //         fprintf(fp,"%d,", mat[i][j]);
  }
    cout<<endl;
//         fprintf(fp,"\n");
      }
  //    fclose(fp);
   }


   int move()
   {
      jump:
      
      while(!myQ.empty())
      {
         jump2:
         pair p = myQ.front();
         cout<<"pop "<<p.r<<":"<<p.c<<"::"<<row[p.r]<<col[p.c]<<endl;
         myQ.pop();

           int l;
            for(l = 0; l<M; l++)
            {
                 if(mat[p.r][l] > mat[p.r][p.c] && done[p.r][l] == 0)
                 {   
                     done[p.r][p.c] = 0;
                     pair pp; pp.r = p.r; pp.c = l;
                     myQ.push(pp) ;
                     goto jump2;    
                 }
                 
             }

            for(l = 0; l<N; l++)
            {
                 if(mat[l][p.c] > mat[p.r][p.c] && done[l][p.c] == 0)
                 {   
                     done[p.r][p.c] = 0;
                     pair pp; pp.r = l; pp.c = p.c;
                     myQ.push(pp) ;
                     goto jump2;    
                 }
                 
             }

         done[p.r][p.c] = 1;


         
         int flag = 0;         
         if(row[p.r]==0)
         {
   
            flag =1;
            row[p.r] = mat[p.r][p.c];
            int max = 0;
            pair p2;
            for(int i =0; i<M; i++)
            {
               if(max < mat[p.r][i] && i != p.c && done[p.r][i] == 0 ) // && mat[p.r][i]!=mat[p.r][p.c])
               {
                 max = mat[p.r][i];
                 p2.r = p.r;
                 p2.c = i;

               }
            }
             if(max  > 0)
             {
               myQ.push(p2);
               cout<<"push1 "<<p2.r<<":"<<p2.c<<endl;
             }
         }
         
         if(col[p.c]==0)
         {
            flag = 1;
            col[p.c] = mat[p.r][p.c];
            int max = 0;
            pair p2;
            for(int i =0; i<N; i++)
            {
               if(max < mat[i][p.c] && i != p.r && done[i][p.c] == 0 ) // && mat[i][p.c]!=mat[p.r][p.c])
               {
                 max = mat[i][p.c];
                 p2.r = i;
                 p2.c = p.c;

               }
            }
             if(max  > 0)
             {
               myQ.push(p2);
               cout<<"push2 "<<p2.r<<":"<<p2.c<<endl;
             }

         }

         if((row[p.r] < mat[p.r][p.c] || col[p.c] < mat[p.r][p.c] ) && flag ==0  )
         {
             return 0;  //not possible
         }
         else if((row[p.r] > mat[p.r][p.c] && col[p.c] > mat[p.r][p.c] ) && flag ==0  )
             return 0;


      }

      if(check_row() == 1)
        goto jump;

      if( check_col() == 1)
        goto jump;

       if(verify() == 0)
         return 0;


      return 1;
   }  

    int verify()
    {
       for(int i =0; i<N; i++)
       {
          for(int j =0; j<M; j++)
         {
            if(mat[i][j] != row[i] && mat[i][j] != col[j]) 
                return 0;
          }
       }
       return 1;
    }

    int check_row()
    {
     
       for(int i = 0; i<N; i++)
       { // cout<<"row:"<<row[i]<<endl;
          if(row[i] == 0)
          {
              int max=0;
              for(int j = 0; j<M; j++)
              {
                  
                  if(max < mat[i][j] && done[i][j] == 0)
                  {
                     pair p;
                     p.r  = i;
                     p.c = j;
                     myQ.push(p);
            cout<<"push "<<p.r<<":"<<p.c<<endl;
                     return 1;
                  }   
              }
          }
       }
    }


    int check_col()
    {
     
       for(int i = 0; i<M; i++)
       {
//cout<<"col:"<<col[i]<<endl;
          if(col[i] == 0)
          {
              int max=0;
              for(int j = 0; j<N; j++)
              {
                  if(max < mat[j][i] && done[j][i] == 0)
                  {
                     pair p;
                     p.r = j;
                     p.c = i;
                     myQ.push(p);
            cout<<"push "<<p.r<<":"<<p.c<<endl;
                     return 1;
                  }   
              }
          }
       }
    }

};

#define SMALL

int main()
{
   FILE *fp = fopen("hello10.out", "a");

 freopen("a.txt", "rt", stdin);
#ifdef SMALL
	freopen("B-large.in","rt",stdin);
	freopen("s6.out","wt",stdout);
#endif
// FILE *fp = fopen("hello.txt", "a")

  int i, j;
  int T;
  
  cin>>T;
  
  for(int k =0; k<T; k++)
  {
     int N,M;
     cin>>N>>M;
//     cout<<N<<M;
     ABC OBJ(N,M);

     for(i =0; i<N; i++)
     {
         for(j =0; j<M; j++)
         {
             int item;
             cin>>item;
  //           cout<<item;

             OBJ.add(item, i , j);
         }
     }

     cout<<"hello"<<endl;
     OBJ.display();
     

     if(OBJ.move() == 0)
     {
      fprintf(fp, "Case #%d: NO\n", k+1);
        cout<<"Case #"<<k+1<<": NO"<<endl<<endl;
     }
     else
     {
        fprintf(fp, "Case #%d: YES\n", k+1);
      cout<<"Case #"<<k+1<<": YES"<<endl<<endl;
     }
    
   }

  fclose(fp);
  return 0;
	}

