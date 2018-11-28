#include <iostream>
#include <conio.h>

using namespace std;

void Solve(int k)
{
     int N;
     cin >> N;
     double Naomi[N], Ken[N];
     for (int i=0; i<N; i++)
         cin >> Naomi[i];
     for (int i=0; i<N; i++)
         cin >> Ken[i];
     sort(Naomi, Naomi+N);
     sort(Ken, Ken+N);
     
    //for (int i=0; i<N; i++)
   //      cout << "(" << i+1 << ")" <<  Naomi[i] << " ";
   // cout << endl;
   //  for (int i=0; i<N; i++)
   //      cout << "(" << i+1 << ")" <<  Ken[i] << " ";
   //  cout << endl;
     
     
     int x=0,y=0;
     int j=0;
     for (int i=0, j=0; i<N && j<N;)
         if (Naomi[i]>Ken[j])
         {
            x++; 
            i++;
            j++;
         }
         else
             i++;
             
             
     bool vis[N];
     for (int i=0; i<N; i++)
         vis[i]=false;
     int i=N-1;
     int j1=N-1,j2=N-1;
     bool change=false;
     
     //cout << "Here!" << endl;
     for (int z=0;z<N;z++)
     {
        //cout << "And here!" << endl;
        change=false;
        for (j1=N-1;j1>=0;j1--)
        {
            if (Naomi[i]>Ken[j1])
            {
               //cout << "Good, it's " << i+1 << " Naomi if bigger than " << j1+1 << " Ken" << endl;
               if (!change && vis[j1+1]!=true)
               {
               //     cout << "And it was for a biggest of Ken!" << endl;
                     break;
               }
               //cout << "O_o" << endl;
               for (j1++;j1<N && vis[j1]==true; j1++)
               if (j1==N)
                      change=false;
               break;
            }
            if (!vis[j1])
               change=true;
        }
        if (j1<0)
        {
           //cout << "Bad break" << endl;
           break;
        }
        if (!change)
        {
           //cout << "Ok,ok... where are we now?" << endl;
           for (j2=0; vis[j2]==true && j2<N;j2++);
           vis[j2]=true;
           i--;
           y++;
           //cout << "+1!" << endl;
        }
        else
        {
            //cout << "Now we chossed " << i+1 << " of Naomi and " << j1+1 << " of Ken" << endl;
            vis[j1]=true;
            i--;
           // cout << "Just not this time" << endl;
        }
     } 
                 
     cout << "Case #" << k+1 << ": " << x << " " << y << endl;       
}
int main()
{
    freopen("D-large.in", "r", stdin);
    //freopen("Input.txt", "r", stdin);
    freopen("OUTPUT.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i=0; i<T; i++)
        Solve(i);
    return 0;
}
