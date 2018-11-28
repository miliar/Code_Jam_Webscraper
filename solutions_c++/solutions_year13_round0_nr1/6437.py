//
//  main.cpp
//  TicTactoe
//
//  Created by Akanksha Verma on 4/13/13.
//  Copyright (c) 2013 Akanksha Verma. All rights reserved.
//

#include <iostream>
#include <string>
#include<fstream>

using namespace std;

int main()
{
    
    char arr[4][4];
    int count=0;
    ifstream file;
    file.open("test.txt");
    
    int number=0 ;
    
    while(true){
        if (file.eof()) {
            break;
        }
        
        int totalX=0;
        int totalO=0;
        int spacecounter =0;
        if(number == 0)
            file>>number;
        
        for(int r=0;r<4;r++){
            for(int c=0;c<4;c++){
                file>>arr[r][c];
                //cout<< arr[r][c];
                if(arr[r][c] == 'X'|| arr[r][c]=='T')
                    totalX++;
                else if(arr[r][c] == 'O')
                    totalO++;
                else if (arr[r][c] =='.')
                    spacecounter++;
                
            }
           //cout<<endl;
        }
        
        bool matches = true;
        int k=0;
        int s=0;
        
//For checking possible perfect combinations
        for(int i=0;i<4;i++){
            
            int O_row_counter=0;
            int O_col_counter =0;
            int X_row_counter =0;
            int X_col_counter =0;
            int X_1_Dia =0;
            int X_2_Dia =0;
            int O_1_Dia =0;
            int O_2_Dia =0;
            
 //******************************************************************************************************//
                int j=k; 
                while (j<4) {
                    if(arr[i][j]=='O' || arr[i][j] =='T')
                        O_row_counter++;
                    
                    j++;
                }
                j=k;
                while(j<4){
                    if(arr[j][i] == 'O' || arr[j][i] == 'T')
                        O_col_counter++;
                    
                    j++;
                }
                
                j=k;
                while(j<4){
                    if(arr[j][j] == 'O' || arr [j][j] == 'T')
                        O_1_Dia++;
                    
                    j++;
                }
                
            j=k;
            s=3;
            while(j<4){
                if(arr[j][s] == 'O' || arr[j][s] == 'T')
                    O_2_Dia++;
                
                j++;
                s--;
            }
        
/******************************************************************************************************/
            
            j=k;
            while (j<4) {
                if(arr[i][j]=='X' || arr[i][j] =='T')
                    X_row_counter++;
                
                j++;
            }
            j=k;
            while(j<4){
                if(arr[j][i] == 'X' || arr[j][i] == 'T')
                    X_col_counter++;
                
                j++;
            }
            
            j=k;
            while(j<4){
                if(arr[j][j] == 'X' || arr [j][j] == 'T')
                    X_1_Dia++;
                
                j++;
            }
            
            j=k;
            s=3;
            while(j<4){
                if(arr[j][s] == 'X' || arr[j][s] == 'T')
                    X_2_Dia++;
                
                j++;
                s--;
            }
            
            
/******************************************************************************************************/            
            
            if(count < number){
               if(X_row_counter == 4 || X_col_counter == 4 || X_1_Dia == 4 || X_2_Dia == 4){
                    cout<<"Case #"<<count+1<<": "<<"X won"<<endl;
                    count++;
                    break;
                }
                
            if(O_col_counter == 4 || O_row_counter == 4 || O_2_Dia == 4 || O_1_Dia == 4  )
                {
                    cout<<"Case #"<<count+1<<": "<<"O won"<<endl;
                    count++;
                    break;
                }
                
                
                
                else if(i== 3 && spacecounter !=0 ){
                    cout<<"Case #"<<count+1<<": "<<"Game has not completed"<<endl;
                    count++;
                    break;
                    
                }
                
                else if(i==3){
                    cout<<"Case #"<<count+1<<": "<<"Draw"<<endl;
                    count++;
                    break;
                }
            }

          
            
        }
        
    }
 
    return 0;
}
