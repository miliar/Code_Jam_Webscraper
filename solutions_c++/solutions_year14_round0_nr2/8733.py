#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{
    ifstream input ("B-large.in");
    ofstream output ("output.txt");
    output.precision(7);
    output.setf(std::ios::fixed, std::ios::floatfield);

   int T; // number of test cases
   input>>T;
   string str;
   getline(input,str);
   double info,c,f,x,p,currentCost,nextCost,newFarmCost;


   for(int i=0;i<T;i++)
   {

    getline(input,str);
    stringstream ss(str);
    ss>>info;
    c=info;
    ss>>info;
    f=info;
    ss>>info;
    x=info;

     p=2.0;
     currentCost=x/p;
     newFarmCost=0;


    //buy a new farm
    newFarmCost= newFarmCost+ c/p;
    p=p+f;
    nextCost= newFarmCost+ x/p;


    if(nextCost>=currentCost)
        output<<"Case #"<<i+1<<": "<<currentCost<<endl;
    else
     {
       while(nextCost<currentCost)
        {
          currentCost=nextCost;
          //buy a new farm
          newFarmCost= newFarmCost+c/p;
          p=p+f;
          nextCost=newFarmCost+ x/p;

          if(nextCost>=currentCost)
            output<<"Case #"<<i+1<<": "<<currentCost<<endl;

        }//end while
      }//end else
   }//end for
        return 0;
}
