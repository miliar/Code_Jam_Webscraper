#include <iostream>
#include <istream>
#include <fstream>

using namespace std;

int main() {
 
	ifstream reader("input.txt");
	ofstream writer("output.txt");
	   int no_of_test_case;
	   int first[4][4];
	   int second[4][4];
    reader>>no_of_test_case;
    for(int t=0;t<no_of_test_case;t++)
    {
     int row1,row2;
     reader>>row1;
     for(int i=0;i<4;i++)
     for(int j=0;j<4;j++)
     {
            
            reader>>first[i][j];

     }

          reader>>row2;
      for(int i=0;i<4;i++)
     for(int j=0;j<4;j++)
     {
            reader>>second[i][j];

     }
     
   //  sort(first[row1-1],first[row1-1]+3);
   //  sort(second[row2-1],second[row2-1]+3);
     
     int counter=0;
     int result=0;
     for(int i=0;i<4;i++)
     {
            for(int j=0;j<4;j++)
           {
               if(first[row1-1][i]==second[row2-1][j])
                     {
                            counter++;
                            result=first[row1-1][i];
                     }
     }
     }
if(counter==1)
writer << "Case #" << t + 1 << ": " << result << endl;
else if(counter==0)
writer << "Case #" << t + 1 << ": " << "Volunteer cheated!" << endl;
else
writer << "Case #" << t + 1 << ": " << "Bad magician!" << endl;
}
 return 0;
}
