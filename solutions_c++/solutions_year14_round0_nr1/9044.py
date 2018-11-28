#include <iostream>
//#include <conio.h>

using namespace std;

int main()
{
    int T;
    int answer1, answer2;
    int array1[16], array2[16];
    int testCasesCount = 1;

    cin>>T;
    while (T-- > 0)
    {
          cin>>answer1;
          for(int i=1; i<=16; ++i)
          {
             cin>>array1[i];
          }

          cin>>answer2;
          for (int i=1; i<=16; ++i)
             cin>>array2[i];
             
         //apply the algorithm
         int count = 0;
         int position = 0;
         for (int i=0; i<4; ++i)
         {
             for(int j=0; j<4; ++j)
             {
                if(array1[answer1*4 - i] == array2[answer2*4 - j])
                {
                    ++count;
                    position = answer1*4 - i;                                     
                }
             }
         }   
         
         cout<<"Case #"<<testCasesCount++<<": ";
         if(count == 1)
         {
            cout<<array1[position];
         }

         if(count > 1)
         {
            cout<<"Bad magician!";
         }
         
         if(count == 0)
         {
            cout<<"Volunteer cheated!";
         }
		 
		 if(T != 0)
		 cout<<endl;
    }
    
  //  getch();
    return 0;
}
