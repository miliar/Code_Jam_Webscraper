#include<iostream>
#include<math.h>
#include<vector.h>
using namespace std;


int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    
    int T;
    cin>>T;
    cin.ignore();
    
    int i,j;
    
    int myMole,noOfOtherMoles;
    int *otherMoles;
    
    int myNewMole,addToNoOfOperations;
    
    int noOfOperations=0;
    
    int t=1;
    while(T--)
    {
        cin>>myMole;
        cin>>noOfOtherMoles;
        
        otherMoles = (int *) malloc(sizeof(int) * noOfOtherMoles);
        
        for(i=0;i<noOfOtherMoles;i++)
            cin>>otherMoles[i];
        
        std::sort(otherMoles,otherMoles+noOfOtherMoles); 
        
        for(i=0;i<noOfOtherMoles;){
            if(myMole>otherMoles[i]){
                myMole += otherMoles[i];
                i++;
                continue;
            }else{
                //make any of the two choices whichever seems best.
                if( (myMole + myMole-1) > otherMoles[i] ){
                    myMole += myMole-1;
                    myMole += otherMoles[i];
                    noOfOperations++;
                    i++;
                } else{
                    j=i;
                    myNewMole = myMole;
                    addToNoOfOperations = 0;
                    if(myNewMole == 1){
                        noOfOperations++;
                        i++;
                        continue;
                    }
                    while(j<noOfOtherMoles){
                        if(myNewMole <= otherMoles[j]){
                            myNewMole += myNewMole -1;
                            addToNoOfOperations++;
                        }else{
                            myNewMole += otherMoles[j];
                            j++;
                        }
                        if(j-i > addToNoOfOperations){
                            i=j;
                            myMole = myNewMole;
                            noOfOperations += addToNoOfOperations;
                            break;
                        }
                    }
                    if (i!=j && j == noOfOtherMoles){  // No profit of adding numbers, just delete the number
                        noOfOperations++;
                        i++;
                    }
                }
            }   
        }
               
        cout<<"Case #"<<t++<<": "<<noOfOperations<<endl;
        cin.ignore();
        
        free(otherMoles);
        noOfOperations = 0;
    }
    
    return 0;
}