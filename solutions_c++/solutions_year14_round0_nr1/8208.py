#include<iostream>
#include<fstream>
using namespace std;

int main()
{
    ifstream input;
    input.open("Sample.txt");
    ofstream output;
    output.open("Output.txt");
    int x,i,j,k, arr[4][4], temp[4], flag=0, n, T;
    
    input >> T;
for(k=1;k<=T;k++)
{   
    flag=0;
    input >> x;
    
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
             input >> arr[i][j];
        }
    }
    
    for(i=0;i<4;i++)
         temp[i]=arr[x-1][i];
    
    input >> x;
    
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
             input >> arr[i][j];
        }
    }
    
    for(i=0;i<4;i++)
    {
        for(j=0;j<4;j++)
        {
             if(temp[i]==arr[x-1][j])
             {
                  flag++;
                  if(flag>1)
                      break;
                  
                  n=arr[x-1][j];
             }
        }
    }
    
    if(flag==0){  output << "Case #" << k << ": Volunteer cheated!" << endl;  }
    else if(flag==1){  output << "Case #" << k << ": " << n << endl;    }
    else if(flag>1){   output << "Case #" << k << ": Bad magician!" << endl;  }
}
    
    input.close();
    output.close();
        
    system("pause");
    return 0;
}
