#include<cstdio>
#include<iostream>

using namespace std;





int main()
{
        int T;
        string a[4];
        cin >> T;
        int t = T;
        while(T--)
        {
                int ans = 3, i, j;
                for(i = 0 ; i < 4 ; i ++){
                        cin >> a[i];
                        //cout << i << a[i] << endl;                        
                        for(j = 0 ; j < 4 ; j ++)
                        {
                                if(a[i][j] == '.')
                                        ans = 4;
                                
                        }
                }
                
                for(i = 0 ; i < 4 ; i ++)
                {
                        int countx =0 ; int counto =0 ;
                        for( j = 0 ; j < 4 ; j ++)
                        {
                                if(a[i][j] == 'X' || a[i][j] == 'T')
                                        countx ++;
                                if(a[i][j] == 'O' || a[i][j] == 'T')
                                        counto ++ ;  
                        }
                        if(countx == 4){
                                ans = 1;break;
                        }
                        if(counto == 4){
                                ans = 2;break;
                        }
                        
                }
                       
                for(i = 0 ; i < 4 ; i ++)
                {
                        int countx =0 ; int counto =0 ;
                        for( j = 0 ; j < 4 ; j ++)
                        {
                                if(a[j][i] == 'X' || a[j][i] == 'T')
                                        countx ++;
                                if(a[j][i] == 'O' || a[j][i] == 'T')
                                        counto ++;   
                        }
                        if(countx == 4){
                                ans = 1;break;
                        }
                        if(counto == 4){
                                ans = 2;break;
                        }
                        
                }
                int countx= 0, counto = 0;
                for(i = 0; i < 4; i ++)
                {                        
                        if(a[i][i] == 'X' || a[i][i] == 'T')
                                countx ++;
                        if(a[i][i] == 'O' || a[i][i] == 'T')
                                counto ++;
                }               
                if(countx == 4)
                        ans = 1;
                if(counto == 4)
                        ans = 2;
                
                countx= 0; counto = 0;
                for(i = 0; i < 4; i ++)
                {                        
                        if(a[i][3-i] == 'X' || a[i][3-i] == 'T')
                                countx ++;
                        if(a[i][3-i] == 'O' || a[i][3-i] == 'T')
                                counto ++;
                }
                if(countx == 4)
                        ans = 1;
                if(counto == 4)
                        ans = 2;
                
                cout << "Case #" << t-T << ": ";
                if(ans == 1)
                        cout << "X won" << endl;
                if(ans == 2)
                        cout << "O won" << endl;
                if(ans == 3)
                        cout << "Draw" << endl;
                if(ans == 4)
                        cout << "Game has not completed" << endl;
                
        }
        
        
        
}