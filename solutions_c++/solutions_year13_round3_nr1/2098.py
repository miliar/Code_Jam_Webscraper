#include <string>
#include <algorithm>
#include <iostream>
#include <vector>
#include <fstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

main()
{
      int c, i, j, k;
      string str, sub;
      int n, count1=0, count2=0; //count2 gia to result
      ofstream save;
      save.open("output.out");
      
      ifstream load;
      load.open("input.in");
      if(load.is_open())
      {
               load >> c;
               for(i=0;i<c;i++)
               {
                    cout << "Case: " << i+1 <<endl;
                    load >> str;
                    load >> n;
                    
                       
                    for(int start=0; start<=str.length()-n; start++)
                    {
                            for(int end=start; end<str.length(); end++)
                            {
                                    count1=0;
                                    for(j=start; j<=end; j++)
                                    {
                                                 if(str[j]!= 'a' && str[j]!= 'e' && str[j]!= 'i' && str[j]!= 'o' && str[j]!= 'u')
                                                     count1++;
                                                 else
                                                     count1 = 0;
                                                 if(count1 == n)
                                                 {
                                                     count2++;
                                                     break;
                                                 }
                                    }
                            }
                    }
                                        
                    /*
                    for(j=0; j<=str.length()-n; j++)
                    {
                           count1 = 0;
                           for(k=j; k<str.length(); k++) 
                           {
                                    if(str[k]!= 'a' && str[k]!= 'e' && str[k]!= 'i' && str[k]!= 'o' && str[k]!= 'u')
                                       count1++;
                                    else
                                       count1 = 0;
                                    if(count1 == n)
                                    {
                                              count2++;
                                              
                                              break;
                                    }
                           }                                           
                    }*/
                    
                    
                    
                    
                    save << "Case #" << i+1 << ": " << count2 <<endl;
                    count2 = 0;                        
                               
               }
               
                        
      }
}
