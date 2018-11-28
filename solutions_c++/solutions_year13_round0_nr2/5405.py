 
#include <iostream>
#include <cstdio>
#include <cstring>
#include <queue>
#include <cmath>
using namespace std;

int row , col;
char *yes = "YES";
char *no = "NO";
int map[150][150];


void Input(){
    cin >> row >> col;
    for(int i = 0 ; i < row ; i++)
        for (int j = 0 ; j < col ; j++)
            cin >> map[i][j];
}


bool OK(bool top,bool bottom,bool left,bool right ){
	if ((!top && bottom && !left && right) || (!top && bottom && left && !right)||
		(top && !bottom && !left && right) || (top && !bottom && left && !right)|| 
		(!top && bottom && left && right)|| 
		(top && !bottom && left && right)|| 
		(top && bottom && !left && right)|| 
		(top && bottom && left && !right)
		){
		return true;
	}
	return false;
}

char * Getans(){
	if(col==1 || row==1)return yes;
    for(int i = 0 ; i < row ; i++)
        for (int j = 0 ; j < col ; j++){
			bool top = (i==0 && (row-1)!=0)?(true):(false),bottom = (i==row-1)?(true):(false),left = (j==0 && (col-1)!=0)?(true):(false),right = (j==col-1)?(true):(false);
            for(int k = 0 ; k < i ; k++){
                if (map[i][j] < map[k][j]){
                    top = true;break;
                }
            }
            for(int k = i+1 ; k < row ; k++){
                if (map[i][j] < map[k][j]){
                    bottom = true;break;
                }
            }
            for(int k = 0 ; k < j ; k++){
                if (map[i][j] < map[i][k]){
                    left = true;break;
                }
            }
            for(int k = j+1 ; k < col ; k++){
                if (map[i][j] < map[i][k]){
                    right = true;break;
                }
            }

            if(top && bottom && left && right || ( (i>0&&i<row-1 && j>0&&j<col-1) && (OK(top,bottom,left,right))  ) ){
                return no;
            }
        }
    return yes;
}


int main()
{
    //freopen("B-small-attempt5.in","r",stdin);
    //freopen("out.txt","w",stdout);
    int Ncase;
    cin >> Ncase;
    int ans = 0;
    while(Ncase--){
        Input();
        cout <<"Case #" << ++ans << ": "<< Getans() << endl;
    }
    return 0;
}
