#include<vector>
#include<string>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cctype>
 
using namespace std;
 
int main(){
    int T,caseno=0;
    scanf("%d",&T);
    while(T--){
        char parray[5][5];
        vector<string> difways;
        string str1;
        
        //initialising the square board
		for(int i=0;i<4;i++)
            scanf("%s",parray[i]);
        for(int i=0;i<4;i++)
            difways.push_back(parray[i]);
        for(int i=0;i<4;i++){
            str1="";
            for(int j=0;j<4;j++){
                str1 += parray[j][i];
            }
            difways.push_back(str1);
        }
        
        str1="";
        for(int i=0;i<4;i++){
            str1 += parray[i][i];
        }
        difways.push_back(str1);
        str1="";
        for(int i=3,j=0;i>=0;i--,j++){
            str1 += parray[j][i];
        }
        difways.push_back(str1);
        
        int vacant1=0,winX=0,winO=0;    
        for(int i=0;i<difways.size();i++){
            int cntX=0,cntO=0;
            for(int j=0;j<4;j++){
                if(difways[i][j]=='X'){
                    cntX++;
                    continue;
                }
                else if(difways[i][j]=='O'){
                    cntO++;
                    continue;
                
                }
                else if(difways[i][j]=='T'){
                    cntX++;
                    cntO++;
                    continue;
                }else{
                    vacant1++;
                }
            }
            if(cntX==4)
                winX++;
            else if(cntO==4)
                winO++;
            
        }
        
        if(winX > winO){
            printf("Case #%d: X won\n",++caseno);
            continue;
        }else if(winO > winX){
            printf("Case #%d: O won\n",++caseno);
            continue;
        }else if(winO == winX and !vacant1){
            printf("Case #%d: Draw\n",++caseno);
            continue;
        }else{
            printf("Case #%d: Game has not completed\n",++caseno);
            continue;
        }
        cin>>str1;
    }
}