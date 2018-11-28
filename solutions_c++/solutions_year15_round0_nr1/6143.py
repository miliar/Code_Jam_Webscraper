//
//  main.cpp
//  StandingOvation
//
//  Created by Arpit Quickgun Arora on 11/04/15.
//  Copyright (c) 2015 Arpit Quickgun Arora. All rights reserved.
//

#include <iostream>
#include <fstream>
using namespace std;

int main()
{
     ofstream myfile;
     myfile.open ("example.txt");
     int t = 0;
     char arr[1002];
     
     cin >> t;
     for (int i = 0; i < t; ++i)
     {
          int Smax = 0;
          cin >> Smax;
          cin >> arr;
          int j = 0, count = 0, friends = 0;
          
          while (arr[j])
          {
               arr[j] -= '0';
               if (arr[j])
               {
                    if(count < j)
                    {
                         friends += (j - count);
                         count += (j - count);
                    }
                    
                    count += arr[j];
                    
               }
               j++;
          }
          myfile << "Case #" << i+1 << ": " << friends << endl;
     }
       myfile.close();
    return 0;
}
