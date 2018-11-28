#include <set>
#include <vector>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{

    char t[10];
    ifstream f;
    f.open("c:\\input.txt");
    f.getline(t,10);

    ofstream o;
    o.open("c:\\output.txt");
    char out[100];
    int i = atoi(t);
    
    
    for(int k=1; k<=i;k++)
    {
        char str[3000]; 
        f.getline(str, 3000);
        int sz = strlen(str);
        int count=sz;  
        int arr[10] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        int alp[26] = {0};

        for(int i=0; i<sz; i++)
        {
            if(str[i] == 'A')
                alp[0]++;
            else if(str[i] == 'B')
                alp[1]++;
            else if(str[i] == 'C')
                alp[2]++;
            else if(str[i] == 'D')
                alp[3]++;
            else if(str[i] == 'E')
                alp[4]++;
            else if(str[i] == 'F')
                alp[5]++;
            else if(str[i] == 'G')
                alp[6]++;
            else if(str[i] == 'H')
                alp[7]++;
            else if(str[i] == 'I')
                alp[8]++;
            else if(str[i] == 'J')
                alp[9]++;
            else if(str[i] == 'K')
                alp[10]++;
            else if(str[i] == 'L')
                alp[11]++;
            else if(str[i] == 'M')
                alp[12]++;
            else if(str[i] == 'N')
                alp[13]++;
            else if(str[i] == 'O')
                alp[14]++;
            else if(str[i] == 'P')
                alp[15]++;
            else if(str[i] == 'Q')
                alp[16]++;
            else if(str[i] == 'R')
                alp[17]++;
            else if(str[i] == 'S')
                alp[18]++;
            else if(str[i] == 'T')
                alp[19]++;
            else if(str[i] == 'U')
                alp[20]++;
            else if(str[i] == 'V')
                alp[21]++;
            else if(str[i] == 'W')
                alp[22]++;
            else if(str[i] == 'X')
                alp[23]++;
            else if(str[i] == 'Y')
                alp[24]++;
            else if(str[i] == 'Z')
                alp[25]++;            
        }
        
        while( count >0){
           
               if(alp[25]){
                  arr[0]++;
                  alp[25]--;
                  alp[4]--;
                  alp[17]--;
                  alp[14]--;
                  count = count-4;
               }
              else if(alp[22])
              {
                 arr[2]++;
                 alp[19]--;
                 alp[22]--;
                 alp[14]--;
                 count = count -3;
              }
              else if(alp[6]){
                  arr[8]++;
                  alp[4]--;
                  alp[8]--;
                  alp[6]--;
                  alp[7]--;
                  alp[19]--;
                  count = count -5;
              }
              else if(alp[23]){
                  arr[6]++;
                  alp[18]--;
                  alp[8]--;
                  alp[23]--;
                  count = count - 3;
              }
              else if(alp[20]){
                 arr[4]++;
                 alp[5]--;
                 alp[14]--;
                 alp[20]--;
                 alp[17]--;
                 count = count - 4;
              }
              else if(alp[14]){
                  arr[1]++;
                  alp[14]--;
                  alp[13]--;
                  alp[4]--;
                  count = count - 3;
              }
              else if(alp[7]){
                  arr[3]++;
                  alp[19]--;
                  alp[7]--;
                  alp[17]--;
                  alp[4] = alp[4]-2;
                  count = count - 5;
              }
              else if(alp[5]){
                  arr[5]++;
                  alp[5]--;
                  alp[8]--;
                  alp[21]--;
                  alp[4]--;
                  count = count - 4;
              }
              else if(alp[18]){
                  arr[7]++;
                  alp[18]--;
                  alp[4] = alp[4]-2;
                  alp[21]--;
                  alp[13]--;
                  count = count - 5;
              }
              else if(alp[13]){
                  arr[9]++;
                  alp[13] = alp[13]-2;
                  alp[8]--;
                  alp[4]--;
                  count = count - 4;
              }              
           
        }
        
        string str1;
        for(int i=0; i<10; i++)
        {
            char buff[50];
            if(arr[i]){
            itoa(i, buff, 10);
            while(arr[i]){
               str1 += buff;
               arr[i]--;
            }
            }
        }
        sprintf(out, "Case #%d: %s\n", k, str1.c_str());
        o << out;
    }

    f.close();
    o.close();
    return 0;
}
