#include <iostream>
#include<stdio.h>
#include<math.h>

using namespace std;
int alg(char gam[][4])
{  int xc,tc,oc,dc=0;
    for (int i=0;i<4;i++)
      {   xc=0;
          tc=0;
          oc=0;

          for(int j=0;j<4;j++)
       { if(gam[i][j]=='X')
         xc++;
         if(gam[i][j]=='T')
         tc++;
         if(gam[i][j]=='O')
         oc++;
         if(gam[i][j]=='.')
         dc++;
        }
        if(xc==4)
        return 1;
        else if(oc==4)
        return 2;
        else if(xc+tc==4)
        return 1;
        else if(tc+oc==4)
        return 2;
}

    for (int j=0;j<4;j++)
      {   xc=0;
          tc=0;
          oc=0;

          for(int i=0;i<4;i++)
       { if(gam[i][j]=='X')
         xc++;
         if(gam[i][j]=='T')
         tc++;
         if(gam[i][j]=='O')
         oc++;
         if(gam[i][j]=='.')
         dc++;
        }
        if(xc==4)
        return 1;
        else if(oc==4)
        return 2;
        else if(xc+tc==4)
        return 1;
        else if(tc+oc==4)
        return 2;
}

          xc=0;
          tc=0;
          oc=0;


    for (int i=0,j=3;j>=0;j--,i++)
      {
       {

       { if(gam[i][j]=='X')
         xc++;
         if(gam[i][j]=='T')
         tc++;
         if(gam[i][j]=='O')
         oc++;
         if(gam[i][j]=='.')
         dc++;
        }
       }
      }
        if(xc==4)
        return 1;
        else if(oc==4)
        return 2;
        else if(xc+tc==4)
        return 1;
        else if(tc+oc==4)
        return 2;

          xc=0;
          tc=0;
          oc=0;
   for (int i=0;i<4;i++)
      {

          for(int j=0;j<4;j++)
       if(i==j)
       {

       { if(gam[i][j]=='X')
         xc++;
         if(gam[i][j]=='T')
         tc++;
         if(gam[i][j]=='O')
         oc++;
         if(gam[i][j]=='.')
         dc++;
        }
       }
      }

        if(xc==4)
        return 1;
        else if(oc==4)
        return 2;
        else if(xc+tc==4)
        return 1;
        else if(tc+oc==4)
        return 2;




if(dc==0)
return 3;
else
return 4;
}
int main() {
    int n_cases;
    cin >> n_cases;
     char gam[4][4];
     int res[n_cases];
    for (int test_case = 0; test_case < n_cases; test_case++)
    {
        for (int i=0;i<4;i++)
       {

        cin>>gam[i][0]>>gam[i][1]>>  gam[i][2]>>  gam[i][3];
        res[test_case]=alg(gam);
    }
    }
    for(int i=0;i<n_cases;i++)
        {cout <<endl<< "Case #" << i +1<< ": ";
        if(res[i]==1)
        cout<<"X won";
        if(res[i]==2)
        cout<<"O won";
        if(res[i]==3)
        cout<<"Draw";
        if(res[i]==4)
        cout<<"Game has not completed";


    }
}

