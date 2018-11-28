#include <iostream>
#include <string>

using namespace std;

char m[6][6];

int determinar(int c, int vacio){
 for(int i=1; i<5 ; i++){
       if((m[i][1]==m[i][2])&&(m[i][2]==m[i][3])&&(m[i][3]==m[i][4])&&(m[i][1]!='.')&&(m[i][1]!='T')){
           cout << "Case #" << c << ": " << m[i][1]<< " won" << endl;
            return 0;
        }
        
        if ((m[i][1]==m[i][2])&&(m[i][2]==m[i][3])&&(m[i][4]=='T')&&(m[i][1]!='.')&&(m[i][1]!='T')){
             cout << "Case #" << c << ": " << m[i][1]<< " won" << endl;
            return 0;
        }
        if ((m[i][1]==m[i][2])&&(m[i][2]==m[i][4])&&(m[i][3]=='T')&&(m[i][1]!='.')&&(m[i][1]!='T')){
         cout << "Case #" << c << ": " << m[i][1]<< " won" << endl;
            return 0;
        }
        if ((m[i][1]==m[i][3])&&(m[i][3]==m[i][4])&&(m[i][2]=='T')&&(m[i][1]!='.')&&(m[i][1]!='T')){
         cout << "Case #" << c << ": " << m[i][1]<< " won" << endl;
            return 0;
        }
        if ((m[i][2]==m[i][3])&&(m[i][3]==m[i][4])&&(m[i][1]=='T')&&(m[i][2]!='.')&&(m[i][2]!='T')){
         cout << "Case #" << c << ": " << m[i][2]<< " won" << endl;
            return 0;
        }
        
        
        
        
        
        
        
         if((m[1][i]==m[2][i])&&(m[2][i]==m[3][i])&&(m[3][i]==m[4][i])&&(m[1][i]!='.')&&(m[1][i]!='T')){
           cout << "Case #" << c << ": " << m[1][i]<< " won" << endl;
            return 0;
        }
        
        if ((m[1][i]==m[2][i])&&(m[2][i]==m[3][i])&&(m[4][i]=='T')&&(m[1][i]!='.')&&(m[1][i]!='T')){
             cout << "Case #" << c << ": " << m[1][i]<< " won" << endl;
            return 0;
        }
        if ((m[1][i]==m[2][i])&&(m[2][i]==m[4][i])&&(m[3][i]=='T')&&(m[1][i]!='.')&&(m[1][i]!='T')){
         cout << "Case #" << c << ": " << m[1][i]<< " won" << endl;
            return 0;
        }
        if ((m[1][i]==m[3][i])&&(m[3][i]==m[4][i])&&(m[2][i]=='T')&&(m[1][i]!='.')&&(m[1][i]!='T')){
         cout << "Case #" << c << ": " << m[1][i]<< " won" << endl;
            return 0;
        }
        if ((m[2][i]==m[3][i])&&(m[3][i]==m[4][i])&&(m[1][i]=='T')&&(m[2][i]!='.')&&(m[2][i]!='T')){
         cout << "Case #" << c << ": " << m[2][i]<< " won" << endl;
            return 0;
        }
            
  }
  
         if((m[1][1]==m[2][2])&&(m[2][2]==m[3][3])&&(m[3][3]==m[4][4])&&(m[1][1]!='.')&&(m[1][1]!='T')){
           cout << "Case #" << c << ": " << m[1][1]<< " won" << endl;
            return 0;
        }
        
        if ((m[1][1]==m[2][2])&&(m[2][2]==m[3][3])&&(m[4][4]=='T')&&(m[1][1]!='.')&&(m[1][1]!='T')){
             cout << "Case #" << c << ": " << m[1][1]<< " won" << endl;
            return 0;
        }
        if ((m[1][1]==m[2][2])&&(m[2][2]==m[4][4])&&(m[3][3]=='T')&&(m[1][1]!='.')&&(m[1][1]!='T')){
         cout << "Case #" << c << ": " << m[1][1]<< " won" << endl;
            return 0;
        }
        if ((m[1][1]==m[3][3])&&(m[3][3]==m[4][4])&&(m[2][2]=='T')&&(m[1][1]!='.')&&(m[1][1]!='T')){
         cout << "Case #" << c << ": " << m[1][1]<< " won" << endl;
            return 0;
        }
        if ((m[2][2]==m[3][3])&&(m[3][3]==m[4][4])&&(m[1][1]=='T')&&(m[2][2]!='.')&&(m[2][2]!='T')){
         cout << "Case #" << c << ": " << m[2][2]<< " won" << endl;
            return 0;
        }
        
        
        
        
         if((m[4][1]==m[3][2])&&(m[3][2]==m[2][3])&&(m[2][3]==m[1][4])&&(m[4][1]!='.')&&(m[4][1]!='T')){
           cout << "Case #" << c << ": " << m[4][1]<< " won" << endl;
            return 0;
        }
        
        if ((m[4][1]==m[3][2])&&(m[3][2]==m[2][3])&&(m[1][4]=='T')&&(m[4][1]!='.')&&(m[4][1]!='T')){
             cout << "Case #" << c << ": " << m[4][1]<< " won" << endl;
            return 0;
        }
        if ((m[4][1]==m[2][3])&&(m[2][3]==m[1][4])&&(m[3][2]=='T')&&(m[4][1]!='.')&&(m[4][1]!='T')){
         cout << "Case #" << c << ": " << m[4][1]<< " won" << endl;
            return 0;
        }
        if ((m[4][1]==m[1][4])&&(m[1][4]==m[3][2])&&(m[2][3]=='T')&&(m[4][1]!='.')&&(m[4][1]!='T')){
         cout << "Case #" << c << ": " << m[4][1]<< " won" << endl;
            return 0;
        }
        if ((m[3][2]==m[2][3])&&(m[2][3]==m[1][4])&&(m[4][1]=='T')&&(m[3][2]!='.')&&(m[3][2]!='T')){
         cout << "Case #" << c << ": " << m[3][2]<< " won" << endl;
            return 0;
        }
        
        if(vacio == 0){
             cout << "Case #"<<c<<": Draw" << endl;
             return 0;
        }
        
          cout << "Case #"<<c<<": Game has not completed" << endl;
  
  
  
 return 0; 
}

int main (){
int cases;
cin >> cases;
for(int i=1; i<= cases; i++){
    int blanc = 0;
    
    
  for(int j=1; j<5 ; j++){
        for(int k=1; k<5 ; k++){
            char car;
            cin >> car;
            m[j][k] = car;
            if(car == '.') blanc ++ ;
        }
    }   
    
  
  determinar(i,blanc);

  
}
    
 return 0;   
}
