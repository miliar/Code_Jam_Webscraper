#include<iostream>
#include<fstream>
#include<cstdlib>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;
int arr1[4],arr2[4],ans[8];
int arr[4][4];
int main()
{
    ifstream f1;
    ofstream f2;
    f1.open("A-small-attempt0.in");
    f2.open("output.out");
    int c=1,t,ans1,ans2;
    f1>>t;
    while(c<=t)
    {
               memset(ans,0,sizeof(ans));
               f1>>ans1;
               for(int i=0;i<4;i++)
               for(int j=0;j<4;j++)
               f1>>arr[i][j];
               for(int i=0;i<4;i++)
               arr1[i] = arr[ans1-1][i];
               f1>>ans2;
               for(int i=0;i<4;i++)
               for(int j=0;j<4;j++)
               f1>>arr[i][j];
               for(int i=0;i<4;i++)
               arr2[i] = arr[ans2-1][i];
               int i=0,j=0,k=0;
               sort(arr1,arr1+4);
               sort(arr2,arr2+4);
               while(i<4 && j<4)
               {
                         if(arr1[i] < arr2[j])i++;
                         else if(arr2[j] < arr1[i])j++;
                         else /* if arr1[i] == arr2[j] */
                         {
                              ans[k++]=arr2[j++];
                              i++;
                              }
                         }
               f2<<"Case #"<<c++<<": ";
               if(k==0)f2<<"Volunteer cheated!\n";
               else if(k==1)f2<<ans[0]<<endl;
               else f2<<"Bad magician!\n";
               }
    f1.close();
    f2.close();
    //system("pause");
    return 0;
    }
