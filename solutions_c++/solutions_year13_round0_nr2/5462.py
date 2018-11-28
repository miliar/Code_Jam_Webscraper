#include<stdio.h>
#include<fstream>
#include<sstream>
using namespace std;
int max(int a,int b)
{
    return(a>=b?a:b);
}

int main()
{
   /* ifstream test;
    ofstream ans;
    stringstream concat;
    test.open("test.txt");
    ans.open("ans.txt");*/
   int t=0,tc=0;
   //test>>tc;
   scanf("%d",&tc);
   for(t=1;t<=tc;t++)
   {
       int ar[120][120],arq[120][120],n=0,m=0,i=0,j=0;
       bool match=true;
       scanf("%d%d",&n,&m);
       //test>>n; test>>m;
       for(i=0;i<n;i++)
       {
           for(j=0;j<m;j++)
           {
               scanf("%d",&ar[i][j]);
               //test>>ar[i][j];
               arq[i][j]=10;
           }
       }

       for(i=0;i<n;i++)
       {
           int height=ar[i][0];
           for(j=0;j<m;j++)
            height=max(height,ar[i][j]);
           for(j=0;j<m;j++)
            if(arq[i][j]>=height)
            arq[i][j]=height;
       }
       for(j=0;j<m;j++)
       {
           int height=ar[0][j];
           for(i=0;i<n;i++)
            height=max(height,ar[i][j]);
           for(i=0;i<n;i++)
            if(arq[i][j]>=height)
            arq[i][j]=height;
       }

       for(i=0;i<n;i++)
       {
           for(j=0;j<m;j++)
           {
               if(ar[i][j]!=arq[i][j])
               match=false;
           }
       }
       if(match)
       {
            printf("Case #%d: YES\n",t);
            //concat<<"Case #"<<t<<": YES\n";
             //ans<<concat.str();
       }
       else {
            printf("Case #%d: NO\n",t);
           //concat<<"Case #"<<t<<": NO\n";
            //ans<<concat.str();
       }
     //concat.str("");
   }

//test.close();
//ans.close();



    return 0;
}
