#include<iostream>
#include<fstream>
using namespace std;
int main()
{
    int cases=0;

    char filename[100]="A-small-attempt3.in";
    ofstream fout("output.txt");
    //cout<<"\nEnter filename for input e.g.file.txt :";
    //cin>>filename;
    ifstream fin(filename);
    if(!fin)
    cout<<"File Not Found\n";
    fin>>cases;

if(cases<=100 && cases>=1)
    {


    int grid[4][4];
    int grid1[4][4];
    int caser=0;
    int answer[2];
    int arr[16];
    bool repeat=false;

while(caser<cases)
{
    for(int i=0;i<16;i++)
    arr[i]=0;
    fin>>answer[0];
    for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            fin>>grid[i][j];
            if(arr[grid[i][j]-1]==0)
            arr[grid[i][j]-1]++;
            else
            {
                 fout<<"Case #"<<caser+1<<": ";
                fout<<"Error!! "<<grid[i][j]<<" repeated. \n";
                repeat=true;
                break;
            }

        }

    }
     for(int i=0;i<16;i++)
     arr[i]=0;

     fin>>answer[1];
     if(answer[1]>=1 && answer[1]<=4 && answer[0]<=4 && answer[0]>=1)
     {
          for(int i=0;i<4;i++)
    {
        for(int j=0;j<4;j++)
        {
            fin>>grid1[i][j];
             if(arr[grid1[i][j]-1]==0)
             arr[grid1[i][j]-1]++;
            else
            {
                 fout<<"Case #"<<caser+1<<": ";
                fout<<"Error!! "<<grid[i][j]<<" repeated. \n";
                repeat=true;
                break;
            }

        }

    }
        int count=0;
    int value=0;
    if(repeat==false)
    {
          for(int i=0;i<4;i++)
  {
            for(int j=0;j<4;j++)
  {
       if(grid[answer[0]-1][i]==grid1[answer[1]-1][j])
       {
           count++;
           value=grid[answer[0]-1][i];
       }

  }
  }
  fout<<"Case #"<<caser+1<<": ";
  if(count==1)
  {
      fout<<value<<endl;
  }
  else if(count>1)
  {
      fout<<"Bad magician!"<<endl;
  }
  else if(count==0)
  {
      fout<<"Volunteer cheated!"<<endl;
  }

     }
     }

     else
     {
          fout<<"Case #"<<caser+1<<": ";
          fout<<"ROW No out of bound i.e 1 <= both answers <= 4.\n";

     }


caser++;
repeat=false;
}
    }
    else
    {
        fout<<"Test cases out of Limit: i.e 1 <= T <=100.\n";
    }


    return 0;
}
