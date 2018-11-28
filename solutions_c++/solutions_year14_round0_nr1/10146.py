#include<iostream>
using namespace std;

int main()
{
  int T;
  int ans1;
  int ans2;
  int row1[4];
  int row2[4];
  int temp;

  cin>>T;
  int testcase = 1;
  while(T--)
  {
    cin>>ans1;
    for(int i=1;i<=4;i++)
    {
      for(int j=0;j<4;j++)
      {
        cin>>temp;
        if(i==ans1)
        {
          row1[j]=temp;
        }
      }
    }


    cin>>ans2;
    for(int i=1;i<=4;i++)
    {
      for(int j=0;j<4;j++)
      {
        cin>>temp;
        if(i==ans2)
        {
          row2[j]=temp;
        }
      }
    }

    int ans_count=0;
    int ans=0;
    for(int i=0;i<4;i++)
    {
      for(int j=0;j<4;j++)
      {
        if(row1[i] == row2[j] && ans_count==0)
        {
          ans = row1[i];
          ans_count++;
        }
        else if(row1[i] == row2[j])
        {
          ans = -1; //badjob
          i=4;
          j=4;
        }
      }
    }

    if(ans == -1)
    {
      cout<<"Case #"<<testcase<<": Bad magician!"<<endl;
    }
    else if(ans_count == 0)
    {
      cout<<"Case #"<<testcase<<": Volunteer cheated!"<<endl;
    }
    else
    {
      cout<<"Case #"<<testcase<<": "<<ans<<endl;
    }
    testcase++;
  }
  return 0;
}
