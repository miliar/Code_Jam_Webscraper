#include <cstdlib>
#include <iostream>
#include <fstream>

using namespace std;

ifstream fin ("0505rohit_2.in");
ofstream fout ("0505rohit_2.out");

int length, retry, test_case;
char test_array[100][100] = {0};
bool one_arr[100];

int notandswap(int swap)
{
    bool swap_el;
    int limit, r, s;
    int swaplen = swap;
    
    if ((swaplen+1)%2==0)
    {
       limit = (swaplen+1)/2;
    }else
    {
         limit = ((swaplen+1)/2)+1;
    }
    
    for (r=0;r<limit;r++,swaplen--)
    {
        swap_el=one_arr[r];
        one_arr[r]=one_arr[swaplen];
        one_arr[swaplen]=swap_el;
    }
    
    for (s=0;s<=swap;s++)
    {
        one_arr[s]=!(one_arr[s]);
    }
       
    return 0;
}

int ReadData()
{
        
    fin >> test_case;  // read test cases count
    //cout<<test_case<<endl;
    for (int b = 0; b < test_case; b++) 
    {
    fin >> test_array[b];
    //cout<<test_array[b]<<endl;
    
    }

    
    /*
    test_count = 5;
    test_data[0] = 0;
    test_data[1] = 1;
    test_data[2] = 2;
    test_data[3] = 11;
    test_data[4] = 1692;
    */
    
    return 0;
}

int reinitializebool()
{
    for (int a=0; a<100; a++)
    {
        one_arr[a]=0;   
    }
}

int loadtesttobool(int sequence)
{
    length=0;
    int exit;
    while ((length<100)&&(exit!=0))
    {
          if (test_array[sequence][length]=='+')
          {
             one_arr[length] = 1;
             //cout<<one_arr[length]<<'\t'; 
             length ++;          
                                       
          }else if (test_array[sequence][length]=='-')
                {
                   one_arr[length] = 0;
                   //cout<<one_arr[length]<<'\t'; 
                   length ++; 
                }else 
                      {
                           exit = 0;                    
                      }
    }
    //cout<<endl<<endl;  
    return 0;
}


int arrangement()
{
    int k, count=0;
    if (length>1)
    {
        for (k=0; k<length-1; k++)
        {
            if ((one_arr[k+1]-one_arr[k])!=0)
            {
               count++;
               notandswap(k);                                
            }                                 
        } 
    }
      
    if(one_arr[0]==0)
    {
                    count++;                
    }
    retry = count;
    //cout<<endl; 
    return 0;    
}


int main(int argc, char *argv[])
{
    // Read the data
    ReadData();
    
    // run the test cases
    
    for (int i =1; i<=test_case; i++)
    {
        retry =0;
        reinitializebool();
        
        //test = test_case[i]
        loadtesttobool(i-1);
        arrangement();
        fout<<"Case #"<<i<<": "<<retry<<'\n';
    } 
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
