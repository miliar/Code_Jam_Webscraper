#include <iostream>

using namespace std;
#define MAX 4

int arr1[MAX];
int arr2[MAX];

void checkTrick(int testCaseNo)
{
    
    int flag=0;
    int cardNum;
    int a,b;
    
    for(a=0;a<MAX;a++)
    {
        for(b=0;b<MAX;b++)
        {
                
            if(arr1[a]==arr2[b])
            {
                flag++;
                cardNum=arr1[a];
            }
        }
    }
    
    
    
    if(flag==0)
    cout<<"Case #"<<testCaseNo<<": Volunteer cheated!";
    else if(flag==1)
    cout<<"Case #"<<testCaseNo<<": "<<cardNum;
    else
    cout<<"Case #"<<testCaseNo<<": Bad magician!";
    
    for(a=0;a<4;a++)
    {
        arr1[a]=0;
        arr2[a]=0;
    }
}


int main()
{

   
   int row1,row2;
   int a,b;
   int temp;
   
   int testCases;
   int testCount=0;
   
   
   cin>>testCases;
   
   while(testCases>0)
   {
       testCount++;
       cin>>row1;
       
       for(a=0;a<4;a++)
       { 
            for(b=0;b<4;b++)
            {
               if(a==row1-1)
               {
                  cin>>arr1[b];
               }
               
               else
               {
                  cin>>temp;
               }
            }//end of inner for       
       }//end of outter for
       
       
      cin>>row2;
       
        for(a=0;a<4;a++)
       {
          
            for(b=0;b<4;b++)
            
            {
                if(a==row2-1)
                {
                    cin>>arr2[b];
                }
                
                else
                {
                    cin>>temp;
                }
            }//end of inner for       
       }//end of outter for
       
       checkTrick(testCount);
       cout<<"\n";
       testCases--;
   }

   return 0;
}