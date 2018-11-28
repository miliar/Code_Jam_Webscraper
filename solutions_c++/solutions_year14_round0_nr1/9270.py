// reading a text file
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>     /* atoi */
#include <sstream>      /*  iss   */
using namespace std;


int main () {

    int MAX =100;
   // cout << "Hello world!" << endl;
  string line;
  int testNum;
  int lineNum=0;
  int ans1[MAX],ans2[MAX];
  int set1[4][4][MAX];
  int set2[4][4][MAX];
  int raw=0;


  ifstream myfile ("A-small-attempt1.in");
  if (myfile.is_open())
  {
      getline (myfile,line);
      testNum = atoi(line.c_str());
    // cout<<testNum<<'\n';

    for (int lineNum=0; getline (myfile,line) && lineNum<(10*testNum); lineNum++)
    {

         if((lineNum%10) == 0){
            ans1[(int)(lineNum/10)]=atoi(line.c_str());
            //  cout<<ans1<<'\n';
              raw=0;
         }
         if((lineNum%10) == 5){
            ans2[(int)(lineNum/10)]=atoi(line.c_str());
              //cout<<ans2<<'\n';
              raw=0;
         }
         if(0<(lineNum%10) && (lineNum%10)<5)
         {
            istringstream iss(line);
            int column=0;
             while (column<4)
            {
            string sub;
            iss >> sub;
            set1[raw][column][(int)(lineNum/10)] = atoi(sub.c_str());
            //cout << "Substring: " << set1[raw][column] << endl;
            column++;
            }
            raw++;
         }

         if((lineNum%10) > 5)
         {
            istringstream iss(line);
            int column=0;
             while (column<4)
            {
            string sub;
            iss >> sub;
            set2[raw][column][(int)(lineNum/10)] = atoi(sub.c_str());
            //cout << "Substring: " << set2[raw][column] << endl;
            column++;
            }
            raw++;



//         if((lineNum%10) == 9)
//         {
//             int match=0;
//             int matchWhat[4];
//            for(int inRaw1 =0; inRaw1<4;inRaw1++)
//            {
//                for(int inRaw2=0; inRaw2<4;inRaw2++)
//                {
//                    //cout <<set1[ans2-1][inRaw1]<< "and"<<set2[ans2-1][inRaw2] <<endl;
//                    if(set1[ans1-1][inRaw1]==set2[ans2-1][inRaw2])
//                    {
//                        match++;
//                        matchWhat[match]=set2[ans2-1][inRaw2];
//                       // cout <<set1[ans2-1][inRaw2]<<endl;
//                    }
//                }
//            }
//
//            if(match)
//            {
//                if(match==1){
//                cout << "Case #" << (int)(lineNum/10) <<": "<<matchWhat[1] <<endl;
//                }else cout << "Case #" << (int)(lineNum/10) <<": "<<"Bad magician!" <<endl;
//            }else cout << "Case #" << (int)(lineNum/10) <<": "<<"Volunteer cheated!" <<endl;
//         }
//
        }




      //cout << line << '\n';
    }
    myfile.close();
  }
  else cout << "Unable to open file";


ofstream myOut ("output.txt");
        if (myOut.is_open())
        {

  for(int i=0;i<testNum;++i)
  {
                   int match=0;
             int matchWhat[4];
            for(int inRaw1 =0; inRaw1<4;inRaw1++)
            {
                for(int inRaw2=0; inRaw2<4;inRaw2++)
                {
                    //cout <<set1[ans2-1][inRaw1]<< "and"<<set2[ans2-1][inRaw2] <<endl;
                    if(set1[ans1[i]-1][inRaw1][i]==set2[ans2[i]-1][inRaw2][i])
                    {
                        match++;
                        matchWhat[match]=set2[ans2[i]-1][inRaw2][i];
                       // cout <<set1[ans2-1][inRaw2]<<endl;
                    }
                }
            }


        //myfile << "This is a line.\n";
        //myfile << "This is another line.\n";

            if(match)
            {
                if(match==1){
                myOut << "Case #" << i+1 <<": "<<matchWhat[1] <<endl;
                }else myOut << "Case #" << i+1 <<": "<<"Bad magician!" <<endl;
            }else myOut << "Case #" << i+1 <<": "<<"Volunteer cheated!" <<endl;


  }

  myOut.close();
        }
        else cout << "Unable to open file";





  return 0;
}
