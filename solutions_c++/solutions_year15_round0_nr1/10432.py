# include <iostream>
using namespace std;
int main()
{
     int t, n, i, ans, t1;
     cin>>t;
     for (t1 = 1 ; t1 <= t ; ++t1)
     {
          cin>>n;
          char A[n+1];
          int B[n+1];
          ans = 0;
          cin>>A;
          /*for (i = 0 ; i < n+1 ; ++i)
          {
               //cin>>A[i];
               B[i] = int(A[i] - '0');
          }*/
          /*if (A[0] == '0')
          {
               B[0] = 1;
               ans++;
          }*/
          //else
          //     B[0] = int(A[0]);
          B[0] = 0;
          for (i = 1 ; i < n+2 ; ++i)
          {
               B[i] = B[i-1] + int(int(A[i-1]) - int('0'));
               if (B[i] < i)
               {
                    ans += (i - B[i]);
                    B[i] = i;
               }
          }
          //B[n+1] = B[n] + int(int(A[n]) - int('0'));
          //ans += (n+1 - B[n+1]);
          /*cout<<"A="<<A<<endl;
          for (i = 0 ; i < n+1 ; ++i)
          {
               cout<<"B["<<i<<"] = "<<B[i]<<"  ,   i = "<<i<<"  ,  A["<<i<<"] = "<<A[i]<<endl;
          }*/
          cout<<"Case #"<<t1<<": "<<ans<<endl;
          
          
     }
     return 0;
}
