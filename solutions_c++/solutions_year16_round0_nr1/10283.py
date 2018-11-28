#include<set>
#include<climits>
#include<iostream>
#include<fstream>

using namespace std;
   
int countSheep(int A) {
    set<int> mset;
    if (A==0) 
       return -1;
    else if (A==1)
        return 10;
    else if (A==2 || A==5 || A==6 || A ==9 || A==10)
         return 90;
    else if (A==3)
         return 30;
    else if (A==4)
         return 92;
    else if (A==7)
         return 70;
    else if (A==8)
         return 96;
    
    for (int i = 1; i < INT_MAX/A; ++i)
    {
        int temp = i * A;        
        int digit = 0;
        int bk_temp = temp;
        while(temp)
        {
            digit = temp % 10;
            mset.insert(digit);
            if(mset.size()==10)
            {
              return bk_temp;
            }
            temp /= 10;
        }
    }
    return -1;
}



int main()
{
  ifstream cinf; 
  cinf.open("in_small.in"); 
  ofstream coutf;
  coutf.open("out_small.out");

  int numCase;
  cinf >> numCase;
  int number;
  
  for (int j = 0; j < numCase; j++)
  {   
    cinf >> number;
    int result = countSheep(number);
    if(result < 0)
        coutf<<"Case #"<<j+1<<": "<< "INSOMNIA" <<endl;
    else
        coutf<<"Case #"<<j+1<<": "<< result <<endl;
  }
  cinf.close();
  coutf.close();
  return 0;
}

