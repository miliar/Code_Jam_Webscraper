#include <iostream>
#include <fstream>
typedef long long lint;
using namespace std;

int  main()
{
    lint search[17];
    lint test,row1,temp1,temp2,temp3,temp4,count2=0,which,count=0;
    string line;
    ifstream myfile;
    ofstream ans;
    ans.open("ans.txt");
    myfile.open("A-small-attempt0.in");
    if (myfile.is_open())
      {
       myfile>>test;
       //cout<<"test"<<test<<endl;
       while(test--)
       {
           count++;
           count2=0;
           //initializer
           for(int i=1;i<=16;i++)
               search[i]=0;
           //
           myfile>>row1;
           //cout<<row1<<endl;
           for(int i=0; i<4;i++)
           {
            myfile>>temp1>>temp2>>temp3>>temp4;
            if((row1)==(i+1))
            {

               //cout<<temp1<<temp2<<temp3<<temp4<<endl;
               search[temp1]++;
               search[temp2]++;
               search[temp3]++;
               search[temp4]++;
            }


           }
           myfile>>row1;
           for(int i=0; i<4;i++)
           {
            myfile>>temp1>>temp2>>temp3>>temp4;
            if((row1)==(i+1))
            {


                //cout<<temp1<<temp2<<temp3<<temp4<<endl;
               search[temp1]++;
               search[temp2]++;
               search[temp3]++;
               search[temp4]++;
            }
            else{
                getline(myfile,line);
            }

           }
           for(int i =1;i<=16;i++)
           {
               if(search[i]>1)
               {
                   //cout<<"test "<<(test+1)<<"\t"<<endl;
                   count2++;
                   which=i;
               }
           }
           //cout<<"count "<<count2<<endl;
           if(count2==0)
           {
               ans<<"Case #"<<count<<": Volunteer cheated!\n";

           }
           else if(count2==1)
           {
               ans<<"Case #"<<count<<": "<<which<<"\n";
           }
           else
           {
               ans<<"Case #"<<count<<": Bad magician!\n";
           }

       }

      }

    myfile.close();
    ans.close();

    return 0;
}
