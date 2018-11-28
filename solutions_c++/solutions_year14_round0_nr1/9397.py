#include<iostream>
#include<stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

int main()
{
    int t=0;
    cin >> t;
    int ans1[t],ans2[t],row1[16],row2[16],pos1[4],pos2[4],counter[t],result[t];
  for(int i=1;i<=t;i++)
  {
    ans1[i-1]=0;
    ans2[i-1]=0;
    counter[i-1]=0;
    result[i-1]=0;
  }
  for(int i=1;i<=t;i++)
    {
       cin >> ans1[i-1];
         for(int k=1;k<=16;k++)
         {
       cin >> row1[k-1];
         }
         cin >>ans2[i-1];
         for(int k=1;k<=16;k++)
         {
       cin >> row2[k-1];
         }
  /*for(int i=1;i<=t;i++)
         {
       for(int k=1;k<=16;k++)
       {
              cout << row2[k-1]<<" ";
           }
           cout<< "change";
           
    }*/
    //for(int i=1;i<=t;i++)
      //{
        if(ans1[i-1]==1)
              { pos1[0]=row1[0];
                pos1[1]=row1[1];
                pos1[2]=row1[2];
                pos1[3]=row1[3];
              }

        else if(ans1[i-1]==2)
              { pos1[0]=row1[4];
                pos1[1]=row1[5];
                pos1[2]=row1[6];
                pos1[3]=row1[7];
              }
        else if(ans1[i-1]==3)
              { pos1[0]=row1[8];
                pos1[1]=row1[9];
                pos1[2]=row1[10];
                pos1[3]=row1[11];
              }
        else if(ans1[i-1]==4)
              { pos1[0]=row1[12];
                pos1[1]=row1[13];
                pos1[2]=row1[14];
                pos1[3]=row1[15];
              }
        if(ans2[i-1]==1)
              { pos2[0]=row2[0];
                pos2[1]=row2[1];
                pos2[2]=row2[2];
                pos2[3]=row2[3];
              }

        else if(ans2[i-1]==2)
              { pos2[0]=row2[4];
                pos2[1]=row2[5];
                pos2[2]=row2[6];
                pos2[3]=row2[7];
              }
        else if(ans2[i-1]==3)
              { pos2[0]=row2[8];
                pos2[1]=row2[9];
                pos2[2]=row2[10];
                pos2[3]=row2[11];
              }
        else if(ans2[i-1]==4)
              { pos2[0]=row2[12];
                pos2[1]=row2[13];
                pos2[2]=row2[14];
                pos2[3]=row2[15];
              }
        int common=0;
        for(int j=0;j<4;j++)
          { 
            for(int u=0;u<4;u++)
            {
              if(pos1[j]==pos2[u])
              {
              counter[i-1]++;
              common=pos2[u];
              }
            }

          }
         if(counter[i-1]==1)
          {
            result[i-1]=common;
          }                              
      } 

    for(int l=0;l<t;l++)
      {
        if(counter[l]==1)
          cout <<"Case #"<<l+1<<": "<<result[l]<<endl;
        else if(counter[l]>1)
          cout <<"Case #"<<l+1<<": Bad magician!"<<endl;
        else if(counter[l]==0)
          cout<<"Case #"<<l+1<<": Volunteer cheated!"<<endl;

      }

}
