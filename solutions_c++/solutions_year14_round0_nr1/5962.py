#include<bits/stdc++.h>

using namespace std;

#define sc scanf
#define pf printf


int main()
{

     long T, kase=1, counT, a[4][4], b[4][4], r1, r2;

     freopen("A_In.in", "r", stdin);
     //freopen("A_out.txt", "w", stdout);

     cin>>T;
     while(T--)
     {
          cin>>r1;
          for(long i=0; i<4; i++)
               for(long j=0; j<4; j++)
                    cin>>a[i][j];

          cin>>r2;
          for(long i=0; i<4; i++)
               for(long j=0; j<4; j++)
                    cin>>b[i][j];
          long result;
          counT=0;
          for(long i=0; i<4; i++)
               for(long j=0; j<4; j++)
               {
                    if(a[r1-1][i] == b[r2-1][j])
                    {
                         counT++;
                         result = a[r1-1][i];
                         //cout<<result<<" ";
                    }
               }

          printf("Case #%ld: ", kase++);

          if(counT == 1)
               printf("%ld\n", result);
          else if(counT > 1)
               printf("Bad magician!\n");
          else if(counT < 1)
               printf("Volunteer cheated!\n");

     }

     return 0;
}
