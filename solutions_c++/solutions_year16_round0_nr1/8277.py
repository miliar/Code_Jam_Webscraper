#include <cstdlib>
#include <iostream>
#include <cmath>
#include <fstream>

using namespace std;

char numbers[10];
int test_count, test_data[100];
int flag;

ifstream fin ("0505rohit.in");
ofstream fout ("0505rohit.out");


int ReadData()
{
        
    fin >> test_count;  // read test cases count
    for (int a = 0; a < test_count; a++) 
    {
    fin >> test_data[a];
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

int power(int exponent)
{
    int value;
    if (exponent == 1)
    {
       value = 10; 
    } else if (exponent == 2)
      {
           value = 100;
      }else if (exponent == 3)
            {
                         value = 1000;
            } else if (exponent == 4)
              {
                   value =10000;
              }else if (exponent == 5)
                    {
                       value =100000;
                    }else if (exponent == 6)
                        {
                           value =1000000;
                        }
      
      
    
    return value;
    
}
          

int CountingSheep(int test_case, int test_no, int count)
{
       
    int i,j,first_no,temp_no,pow_no;
    first_no = test_no*count;
    
    if (first_no !=0)
    {
    pow_no = power(1);
    //cout<<"check2"<<pow_no<<'\n';
        for(i=1; first_no!=0; i++)
        {
                int a=i, b=10;

                //cout<<"check2"<<pow_no<<'\n';
                temp_no = first_no%pow_no;
                numbers[temp_no] = 'T';
                first_no = first_no/pow_no;
        }
        
        for(j=1; j<=10; j++)
        {
            if ( numbers[j-1] != 'T' )
            {
                 count++;
                 CountingSheep(test_case,test_no,count);
                 
            } 
            
            if (j==10&&flag!=1)
            {
               fout<<"Case #"<<test_case<<": "<<test_no*count<<'\n';
               flag=1;
               break;        
            }           
        }
        

                
                
    }
    else
    {
        fout<<"Case #"<<test_case<<": INSOMNIA"<<'\n';
    }    
    
    return 0;         

}

int main(int argc, char *argv[])
{
    
    ReadData();
    int x,test;
    for (x=1;x<=test_count;x++)
    {
        numbers[0]='F';
        numbers[1]='F';
        numbers[2]='F';
        numbers[3]='F';
        numbers[4]='F';
        numbers[5]='F';
        numbers[6]='F';
        numbers[7]='F';
        numbers[8]='F';
        numbers[9]='F';
        flag=0;
        test = test_data[x-1];
        //cout<<"check1"<<'\n';
        CountingSheep(x,test , 1);       
    }
        
    
    system("PAUSE");
    return EXIT_SUCCESS;
}
