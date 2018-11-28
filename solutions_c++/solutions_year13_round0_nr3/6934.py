#include <cstdio>

#define YES "YES"
#define NO "NO"


int main (int argc, char* argv[]){

    int t;
    
    scanf("%d",&t);
    
    //T Test cases
    for(int z=0; z < t ; ++z){
    
        int resultado = 0; 
        
        int a,b;    
        
        //Read input
        scanf("%d",&a);
        scanf("%d",&b);      
        if(a > 484){
        
            resultado = 0;
        
        
        } 
        else if(a > 121){
        
           if(b >=484){
           
                       resultado = 1;
           

           
           }else{
           
                          resultado = 0;
           
            
           } 
        
        } 
        else if(a > 9 ){
        
           if(b >=484){
           
                       resultado = 2;
           

           
           }   
            
            else if(b >= 121){
            
                resultado = 1;
            }
            else{
                resultado = 0;
            
            }
            
        } else if (a > 4){
            
            if(b >=484){
                
                       resultado = 3;
           

           
           }
            
            else if(b >= 121){
            
               resultado = 2; 
            }
            else if (b >= 9){
                resultado = 1;
            
            }else{
            
                resultado = 0;
            
            }    
            
        }else if(a > 1){
            
            if(b >=484){
           
                       resultado = 4;
           }
             
            else if(b >= 121){
                resultado = 3;
            }
            else if (b >= 9){
                resultado = 2;
            
            }else if (b >= 4){
                resultado = 1;
                
            }else{
            
                resultado = 0;
            }
                    
        }else{
        
            if(b >=484){
           
                       resultado = 5;
           

           
           }
            else if(b >= 121){
                resultado = 4;
            }
            else if (b >= 9){
                resultado = 3;
            
            }else if( b >= 4){
                resultado = 2;
                
            }else {
            
                resultado = 1;
            }
        
        } 
        
        
        //Output
        printf("Case #%d: %d\n",z+1,resultado);
    
    
    }

    return 0;
    



}
