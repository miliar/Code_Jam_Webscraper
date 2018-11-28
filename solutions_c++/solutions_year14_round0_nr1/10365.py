#include<iostream>
#include<fstream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<conio.h>

using namespace std;

int main()
{
    int t=0,line=1,ans,ans_1,ans_2,i,j,k;
    int arr1[4][4],arr2[4][4],flag=0;
    char ch[10];
    ofstream out("C:\\Users\\Vivek\\Documents\\Codejam\\output\\magician.out");
    ifstream in("C:\\Users\\Vivek\\Downloads\\A-small-attempt3.in");
    in>>t;
    for(k=0;k<t;k++)
    {
     in>>ans_1;
     for(i=0;i<4;i++)
      {
       for(j=0;j<4;j++)
        in>>arr1[i][j];
      }
     in>>ans_2;
     for(i=0;i<4;i++)
      {
       for(j=0;j<4;j++)
        in>>arr2[i][j];
      }
     for(i=0;i<4;i++)
     {
      for(j=0;j<4;j++)
      {
       if(arr1[ans_1-1][i]==arr2[ans_2-1][j])
       {
        ans=arr1[ans_1-1][i];
        flag++;
       }
      }
     }
     if(flag>1)
      out<<"Case #"<<k+1<<": Bad magician!"<<endl;
     else if(flag!=0)
      out<<"Case #"<<k+1<<": "<<ans<<endl; 
     else
      out<<"Case #"<<k+1<<": Volunteer cheated!"<<endl;
     ans=0;
     flag=0;
    }
    in.close();
    out.close();
    system("pause");
    return 0;
}
