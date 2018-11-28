#include <cstdio>

int main () {
	int tc;
    int ctr = 0;
    char map[4][4];
    char temp[4];
	scanf("%d\n",&tc);
	while(tc--){
        bool p1 = false, p2 = false;
        int n1, n2;
        ctr++;
        for(int i = 0; i < 4; i++){            
            gets(map[i]);
        }
        gets(temp);
        int ind = 0;
        while( (ind < 4) && (!p1) && (!p2) ) {
            n1 = 0; n2 = 0;
            char tmp;
            for(int j = 0; j < 4; j++){
                if (map[ind][j] == 'X' || map[ind][j] == 'T')
                    n1++;
                if (map[ind][j] == 'O' || map[ind][j] == 'T')
                    n2++;                                        
            }            
            if (n1 == 4)
                p1 = true;
            if (n2 == 4)
                p2 = true;
            ind++;    
        }
        ind = 0;
        while( (ind < 4) && (!p1) && (!p2) ) {
            n1 = 0; n2 = 0;
            char tmp;
            for(int j = 0; j < 4; j++){
                if (map[j][ind] == 'X' || map[j][ind] == 'T')
                    n1++;
                if (map[j][ind] == 'O' || map[j][ind] == 'T')
                    n2++;                                        
            }            
            if (n1 == 4)
                p1 = true;
            if (n2 == 4)
                p2 = true;
            ind++;    
        }
        
        if ( (!p1) && (!p2) ){
            n1 = 0; n2 = 0;
            for(int i = 0; i < 4; i++){           
                if (map[i][i] == 'X' || map[i][i] == 'T')
                        n1++;
                if (map[i][i] == 'O' || map[i][i] == 'T')
                        n2++; 
            }
            if (n1 == 4)
                    p1 = true;
            if (n2 == 4)
                    p2 = true;
        }
        if ( (!p1) && (!p2) ){
            n1 = 0; n2 = 0;
            for(int i = 0; i < 4; i++){           
                if (map[i][3-i] == 'X' || map[i][3-i] == 'T')
                        n1++;
                if (map[i][3-i] == 'O' || map[i][3-i] == 'T')
                        n2++; 
            }
            if (n1 == 4)
                    p1 = true;
            if (n2 == 4)
                    p2 = true;
        }
        
        if (p1)
           printf("Case #%d: X won\n", ctr);           
        else if (p2)
           printf("Case #%d: O won\n", ctr);
        else {
            bool notYet = false;
            for(int i = 0; i < 4; i++){
                for(int j = 0; j < 4; j++){
                    if (map[i][j] == '.'){
                        notYet = true;    
                        break;
                    }
                }    
            }
            if (notYet)
                printf("Case #%d: Game has not completed\n",ctr);
            else
                printf("Case #%d: Draw\n",ctr);            
        }                
    }
	return 0;
}
