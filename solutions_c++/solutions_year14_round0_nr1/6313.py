#include <iostream>
#include<algorithm>
#include<fstream>
using namespace std;
void intersection(int arr1[], int arr2[],int caseno);

int main()
{
   ifstream file("input.txt"); 
   int arr1[4][4], arr2[4][4];
   int a[4],b[4];
   int T, ans1, ans2;
   file>>T;
   for(int i=0; i<T;i++)
   {
       file>>ans1;
       for(int j=0;j<4;j++)
        for(int k=0;k<4;k++)
            file>>arr1[j][k];
    for(int m=0;m<4;m++)
        a[m]=arr1[ans1-1][m];
        file>>ans2;
        for(int j=0;j<4;j++)
            for(int k=0;k<4;k++)
                file>>arr2[j][k];
    for(int m=0;m<4;m++)
        b[m]=arr2[ans2-1][m];
    sort(a,a+4);
    sort(b,b+4);
    intersection( a, b,i+1);
   }
   file.close();
   return 0;
}
void intersection(int arr1[], int arr2[],int caseno)
{
    int common=0,count=0; 
int i = 0, j = 0;
  while(i < 4 && j < 4)
  {
    if(arr1[i] < arr2[j])
      i++;
    else if(arr2[j] < arr1[i])
      j++;
    else /* if arr1[i] == arr2[j] */
    {
      common=arr2[j++];
      count++;
      i++;
    }
  }
  if(count==1)
    {
        cout<<"Case #"<<caseno<<": "<<common<<endl;
    }
    else if(count == 0)
    {
        cout<<"Case #"<<caseno<<": Volunteer cheated!"<<endl;
    }
    else
    {
        cout<<"Case #"<<caseno<<": Bad magician!"<<endl;
    }
}