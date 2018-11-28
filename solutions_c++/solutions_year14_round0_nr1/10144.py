#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    ifstream scan ("A-small-attempt0.in");
    ofstream myfile ("test.txt");
   // myfile<<4<<"\n"<<5<<endl;
    int t,a,b,num,i,j,req,k,count;
    vector<vector <int> > arr1(4),arr2(4);
    scan>>t;
    for(k=1;k<=t;k++)
    {
        count=0;
        scan>>a;
       for(i=0;i<4;i++)
       {
           for(j=0;j<4;j++)
           {
               scan>>num;
               arr1[i].push_back(num);
           }
       }

       scan>>b;
       for(i=0;i<4;i++)
       {
           for(j=0;j<4;j++)
           {
               scan>>num;
               arr2[i].push_back(num);
           }
       }

       for(i=0;i<4;i++)
       {
           for(j=0;j<4;j++)
           {
               if(arr1[a-1][i]== arr2[b-1][j]){
                    req = arr1[a-1].at(i);
                count++;
                if(count > 1)
                    break;
               }
           }
       }
       if(count == 1)
        myfile<<"Case #"<<k<<": "<<req<<endl;

        else if(count > 1){
            //cout<<"Case #"<<k<<": Bad magician!"<<endl;
            myfile<<"Case #"<<k<<": Bad magician!"<<endl;
        }

        else if(count == 0){
            //cout<<"Case #"<<k<<": Volunteer cheated!"<<endl;
            myfile<<"Case #"<<k<<": Volunteer cheated!"<<endl;
        }

            for(i=0;i<4;i++)
            {
                arr1[i].clear();
                arr2[i].clear();
            }

    }

    return 0;
}
