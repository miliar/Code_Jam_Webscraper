
#include <iostream>
#include <set>

using namespace std;
int lawn[100][100];
int N, M, Case = 0;

set<int> Max;
set<int>::reverse_iterator rit;

int eval()
{
     int pat[100][100], i, j, m;
     bool valid, res=true;
     
     rit = Max.rbegin();
     m=*rit;
     ++rit;     
     for(i=0; i<N; ++i)
       for(j=0; j<M; ++j)
          pat[i][j]=m;
          
     for(; res && rit!=Max.rend(); ++rit)
     {
        m=*rit;
        res=false;
        for(i=0;i<N;++i)
        {
           valid=true;
           for(j=0;valid&&j<M;++j)
           {
             if(lawn[i][j]>m)
                valid=false;
           }
           if(valid)
             for(j=0,res=true;j<M;++j)
                pat[i][j]=m;                            
        }
        for(j=0;j<M;++j)
        {
           valid=true;
           for(i=0;valid&&i<N;++i)
           {
             if(lawn[i][j]>m)
                valid=false;
           }
           if(valid)
             for(i=0,res=true;i<N;++i)
                pat[i][j]=m;                            
        }        
        if(!res)
          return 0;
     } 
     
     for(i=0;i<N;++i)
        for(j=0;j<M;++j)
          if( lawn[i][j] != pat[i][j] )
             return 0;     
     return 1;
 }

int main(int argc, char *argv[])
{
    int T, i, j, a;
	//printf("Hellow\n");
    scanf("%d", &T);
    do
    {
       scanf("%d%d", &N, &M);
       for(i=0; i<N ; ++i)
       {
           for(j=0; j<M; ++j)
           {
              scanf("%d",&lawn[i][j]);
			  Max.insert(lawn[i][j]);
              //printf("%d",lawn[i][j]);
              }
           //scanf("%d\n", &a);
           //printf("\n");
       } 
       if(eval())
          printf("Case #%d: YES\n", ++Case);
       else
          printf("Case #%d: NO\n", ++Case);
                              
       Max.clear();
    }while(--T);
}
