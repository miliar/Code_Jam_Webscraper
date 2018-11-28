#include<iostream>
using namespace std;
int a[4][4], b[4][4], r1, r2;
void read()
{
     int i, j;
     cin>>r1;
     for(i = 0; i < 4; i++)
           for(j = 0; j < 4; j++)
                 cin>>a[i][j];
     cin>>r2;
     for(i = 0; i < 4; i++)
           for(j = 0; j < 4; j++)
                 cin>>b[i][j];
}
int addCards()
{
    int result, i, j, count;
    count = result = 0;
    read();
    for(i = 0; i < 4; i++)
    {
          for(j = 0; j < 4; j++)
          {
                if(a[r1-1][i] == b[r2-1][j])
                {
                      result = a[r1-1][i];
                      count++;
                }
          }
          if( count > 1)
              return -2;
    }
    if(count == 0)
             return -1; 
    return result;
}
int main()
{
    int result, t, T;
    cin>>T;
    for(t = 0; t < T; t++)
    {
          result = addCards();
          cout<<"Case #"<<t+1<<": ";
          if(result == -1)
          {
               cout<<"Volunteer cheated!";
          }
          else if(result == -2)
          {
               cout<<"Bad magician!";
          }  
          else
          {
              cout<<result;
          }        
          if(t < T-1)
          cout<<endl;
    }
    return 0;
}
