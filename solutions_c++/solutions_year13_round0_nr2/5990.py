# include <iostream>
# include <conio.h>
# include <fstream>
#include <stdlib.h>
using namespace std;
ifstream fr("input.txt");
ofstream fw("output.txt");
int solve();
int main()
{   int t;
    fr>>t;
    for (int i=0;i<t;i++)
    {   if(solve()==0)
            fw<<"Case #"<<i+1<<": "<<"NO"<<endl;
        else
            fw<<"Case #"<<i+1<<": "<<"YES"<<endl;
    }
    //getch();
}
int solve()
{
    int depth,length;
    fr>>depth;                                              //depth->no of rows
    fr>>length;                                             //length->no of cols
    int arr[100][100];
    for (int j=0;j<depth;j++)
        for (int i=0;i<length;i++)
                fr>>arr[j][i];
    int largest=0;


    if (depth==1)
        return 1;
    if (length==1)
        return 1;
    for (int j=0;j<depth;j++)
        for (int i=0;i<length;i++)
            if(arr[j][i]>largest)
                largest=arr[j][i];
    int flag=1;
    for (int i=0;i<depth;i++)
    {   for (int j=0;j<length;j++)
        {   cout <<"\nfor"<<i<<" " <<j<<"::"<<arr[i][j]<<endl;
            int flag_l=1;
            int flag_d=1;
            if(arr[i][j]<largest)
            {   
                cout<<"\nflag_l:";
                for(int x=0;x<length;x++)
                {   if(arr[i][j]<arr[i][x])
                    {    flag_l=0;
                        cout <<"impossible";
                    }
                    cout <<arr[i][x];
                }
                
                cout <<"\nflag_b:";
                for(int x=0;x<depth;x++)
                {   if(arr[i][j]<arr[x][j])
                    {    flag_d=0;
                        cout <<"impossible";
                    }
                   cout <<arr[x][j];
                }
                flag=flag*(flag_l||flag_d);
            }
        }
    }
    return flag;
}


















