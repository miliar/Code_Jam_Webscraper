#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
    int cases;
    int pos1, pos2;
    int a[4][4], b[4][4];
    scanf("%d", &cases);
    for(int k=0; k<cases; k++){
        scanf("%d", &pos1);
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                scanf("%d", &a[i][j]);
            }
        }
        scanf("%d", &pos2);
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                scanf("%d", &b[i][j]);
            }
        }
        int l1[4] = { a[pos1-1][0], a[pos1-1][1], a[pos1-1][2], a[pos1-1][3] };
        int l2[4] = { b[pos2-1][0], b[pos2-1][1], b[pos2-1][2], b[pos2-1][3] };
        int intersection = 0;
        int intersection_count = 0;
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                if(l1[i] == l2[j]){
                    intersection_count++;
                    intersection = l2[j];
                }
            }
        }
        cout << "Case #" << k+1 << ": ";
        if(intersection_count == 1)
            cout <<  intersection << endl;
        else if (intersection_count == 0)
            cout << "Volunteer cheated!" << endl;
        else 
            cout << "Bad magician!" << endl;

    }
}

