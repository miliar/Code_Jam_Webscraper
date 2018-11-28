#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <math.h>
using namespace std;

int sign[5][5]={
0, 0, 0, 0, 0,
0, 1, 2, 3, 4,
0, 2,-1, 4,-3,
0, 3,-4,-1, 2,
0, 4, 3,-2,-1
};
int result[10010][10010];

bool Dijkstra(vector<int> &numbers, int m ){
    for( int i=0; i<m; i++ ){
        int sum = numbers[i];
        int state;
        for( int j=i; j<m; j++ ){
            if( j==i )
                result[i][j] = numbers[j];
            else{
                state = sum>0? 1: -1;
                sum = state*sign[abs(sum)][abs(numbers[j])];
                result[i][j] = sum;
            }
        }
    }
    for( int i=0; i<m; i++ ){
        if( result[0][i]==2 ){
            for( int j=i+1; j<m-1; j++){
                if( result[i+1][j]==3 && result[j+1][m-1]==4 )
                    return true;
            }
        }
    }
    return false;
}
int main()
{
    int n;
    FILE *fp;
	fp = fopen( "C-small-attempt2.in", "r");
	FILE *fp2;
	fp2 = fopen( "output.txt", "w");
	fscanf(fp, "%d", &n);
    for( int i=0; i<n; i++ ){
        int m, t;
        fscanf(fp, "%d", &m);
        fscanf(fp, "%d", &t);
        char *input = new char[10010];
        fscanf(fp, "%s", input);
        vector<int> numbers;
        for( int k=0; k<m*t; k++ )
            numbers.push_back((int)(input[k%m])-103);
        cout<<"Solution: "<<Dijkstra(numbers, m*t)<<endl;
        if( Dijkstra(numbers, m*t) )
            fprintf(fp2, "Case #%d: YES\n", i+1);
        else
            fprintf(fp2, "Case #%d: NO\n", i+1);
        delete [] input;
    }
    fclose(fp);
    fclose(fp2);

    return 0;
}
