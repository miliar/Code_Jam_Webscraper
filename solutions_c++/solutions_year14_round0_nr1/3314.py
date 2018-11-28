#include <iostream>

#include <istream>
#include <fstream>

using namespace std;

int main() {
 
	ifstream reader("input.txt");
	ofstream writer("output.txt");
	   int no_of_test_case;
    //scanf("%d",&no_of_test_case);
    reader>>no_of_test_case;
    for(int t=0;t<no_of_test_case;t++)
    {int a[16]={0};
         int val;
     int row1,row2;
     //scanf("%d",&row1);
     reader>>row1;
     for(int i=0;i<16;i++)
     {
            //scanf("%d",&val);
            reader>>val;
             if(i>=4*(row1-1) &&i<=(4*(row1-1)+3))
                        { a[val-1]+=1;
                       // printf("xyz #%d : %d",i,val);
                        }
     }
     //int row2;
          //scanf("%d",&row2);
          reader>>row2;
     for(int i=0;i<16;i++)
    {
            reader>>val;
             if(i>=4*(row2-1) &&i<=(4*(row2-1)+3))
                         {a[val-1]+=1;
                          // printf("alpha #%d : %d",i,val);
                           }
     }
     int counter=0;
     int res=0;
     for(int i=0;i<16;i++)
     {// printf("abc #%d : %d",i,a[i]);
             if(a[i]==2)
     {counter++;
     res=i+1;
     
     }}
     if(counter==1)
    // printf("Case #%d : %d",t+1,res);
    writer << "Case #" << t + 1 << ": " << res << endl;
     else if(counter==0)
     //Case #3: Volunteer cheated!
     //printf("Case #%d: Volunteer cheated!",t+1);
       writer << "Case #" << t + 1 << ": " << "Volunteer cheated!" << endl;
     else
   writer << "Case #" << t + 1 << ": " << "Bad magician!" << endl;
     
   
     
}
 // scanf("%d",&no_of_test_case);
 return 0;
}
