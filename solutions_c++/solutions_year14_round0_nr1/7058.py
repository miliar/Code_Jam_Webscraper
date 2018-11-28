#include<iostream>
#include<stdio.h>
#include<vector>
#include<iomanip>
#include<cstring>
#include<conio.h>

using namespace std;

int check(vector<int> v1, vector<int> v2)
{
    int flag = -1; int num;

    for(int i=0; i<4; i++)
     {       for(int j=0; j<4; j++)
     {	if(v1[i] == v2[j])
                            { flag++; num = v1[i];}
     }}
      if(flag==-1)
                return -1;
    else if(flag==0)
         return num;

    return 0;
}

int main()
{
    freopen("input.in", "r", stdin);
    freopen("p1Output.txt", "w", stdout);

    int t;
    cin>>t;

    for(int k=0; k<t; k++)//while(t--)
    {
              int r1;
              cin>>r1;

              int msquareI[4][4], msquaref[4][4];
              for(int i=0; i<4; i++)
                      for(int j=0; j<4; j++)
                              cin>>msquareI[i][j];

              int r2;
              cin>>r2;
              for(int i=0; i<4; i++)
                      for(int j=0; j<4; j++)
                              cin>>msquaref[i][j];

              vector<int> v1, v2;
              for(int i=0; i<4; i++)
                      {v1.push_back(msquareI[r1-1][i]); v2.push_back(msquaref[r2-1][i]);}

              int c = check(v1, v2);
              cout<<"Case #"<<k+1<<": ";
              if(c==0) //implies there are multiple numbers
                      cout<<"Bad magician!\n";
              else if(c==-1)
                    cout<<"Volunteer cheated!\n";
              else
                  cout<<c<<endl;


    }
  //getch();
  return 0;
}
