#include <iostream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>

using namespace std;

int main(int argc,char *argv[])
{

  ifstream ifs(argv[1]);
  int cases;
  ifs>>cases;
  vector<int> sub;
  for(int i=0;i<cases;i++)
  {
    sub.clear();
    int curr;
    int row;
    ifs>>row;
  // cout<<"ROW 1 "<<row<<endl;
    int index;
    for(index=0;index<4*(row-1);index++)
     ifs>>curr;

    for(int j=0;j<4;j++)
     {
       ifs>>curr;
    //   cout<<"first "<<curr<<endl;
       sub.push_back(curr);
       index++;
     }
     for(;index<16;index++)
     ifs>>curr;



    ifs>>row;
    int res=0;
  // cout<<"ROW 2 "<<row<<endl;
    for(index=0;index<4*(row-1);index++)
     ifs>>curr;

    for(int j=0;j<4;j++)
     {
       ifs>>curr;
      for(int x=0;x<4;x++)
      {
       if(curr==sub[x])
        {
          if(res==0)
          {
          res=sub[x];

      }
          else
          res=-1;
        }

     }
     index++;
     }
     for(;index<16;index++)
     ifs>>curr;

    if(res==0)
    {
      printf("Case #%d: Volunteer cheated!\n",i+1);
    }
    else if(res>0)
    {
      printf("Case #%d: %d\n",i+1,res);
    }
    else
    {
      printf("Case #%d: Bad magician!\n",i+1);
    }


  }

ifs.close();
return 0;



}
