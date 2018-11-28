#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <fstream>
using namespace std;

#ifndef FALSE
#define FALSE (0)
#endif

#ifndef TRUE
#define TRUE (1)
#endif

#define _DEBUG_OFF

void insertion_sort (int arr[], char arr2[], int length){
	 	int j, temp;
		
	for (int i = 0; i < length; i++){
		j = i;
		
		while (j > 0 && (arr[j] > arr[j-1])){
			  temp = arr[j];
			  arr[j] = arr[j-1];
			  arr[j-1] = temp;
              
              temp = arr2[j];
			  arr2[j] = arr2[j-1];
			  arr2[j-1] = temp;
              
			  j--;
			  }
		}
}

main() {
    ifstream fin("A-small-attempt0.in");
	assert( !fin.fail() );
    ofstream fout("A-small1.out");
    assert( !fout.fail() );
    
    int T = 0, CaseNum = 0;
    
    fin >> T;
    
    CaseNum = 0;
    while(T--)
    {
       int N = 0, sc[26], i = 0, Total = 0;
       char ca[26];
       
       fin >> N;
       
       for(i=0 ; i < N ; ++i)
       {
           ca[i] = 'A' + i;
           fin >> sc[i];
           Total += sc[i];
       }
       
       ++CaseNum;
       fout << "Case #" << CaseNum << ":";
       
       while(Total)
       {
           insertion_sort(sc, ca, N);
           fout << " ";
           
           if(sc[1])
           {
               if(sc[1] <= ((Total - 2) / 2))
               {
                   fout << ca[0] << ca[0];
                   sc[0] -= 2;
                   Total -= 2;
               }
               else{
                   if(sc[1] <= ((Total - 1) / 2))
                   {
                       fout << ca[0];
                       sc[0] -= 1;
                       --Total;
                   }
                   else{
                       fout << ca[0] << ca[1];
                       sc[0] -= 1;
                       sc[1] -= 1;
                       Total -= 2;
                   }
               }
           }
       }
       
       fout << endl;
    }
    
    fin.close();
    fout.close();
    return 0;
}

bool findNum(char *str, int num)
{
    bool retVal = false;
    
    string numNames[] = {
                            "ZERO",
                            "ONE",
                            "TWO",
                            "THREE",
                            "FOUR",
                            "FIVE",
                            "SIX",
                            "SEVEN",
                            "EIGHT",
                            "NINE",
            };
    int numNamesLen[] = {
                            4,
                            3,
                            3,
                            5,
                            4,
                            4,
                            3,
                            5,
                            5,
                            4
        };
        
    char _str[30];
    int i=0, j=0;
    
    for(i=0 ; str[i] ; ++i)
    {
        _str[i] = str[i];
    }
    _str[i] = str[i];
    
    for(i=0, j=0 ; str[i] ; ++i)
    {
        for(int k=0 ; k < numNamesLen[num] ; ++k)
        {
            if(str[i] == numNames[num][k])
            {
                str[i] = '0';
                numNames[num][k] = '1';
                ++j;
                
                //cout << j << " " << numNamesLen[num] << endl;
                if(j >= numNamesLen[num])
                {
                    retVal = true;
                }
                
                break;
            }
        }
        
        
        if(retVal == true)
        {
            break;
        }
    }
    
    if(retVal == false)
    {
        for(i=0 ; _str[i] ; ++i)
        {
            str[i] = _str[i];
        }
        str[i] = _str[i];
    }
    
    return retVal;
}