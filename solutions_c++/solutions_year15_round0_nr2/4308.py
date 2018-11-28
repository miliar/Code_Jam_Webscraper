#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <math.h>
using namespace std;

int panCakes(vector<int> t){
    vector<int> s = t;
    int minTime = 0;
    int sum = 0;
    for( int i=0; i<s.size(); i++ ){
        minTime = max(s[i], minTime);
        sum += s[i];
    }
    int time = 0;
    int T = sqrt(sum);
    while( 1 ){
        int value = 0;
        int index = 0;
        for( int i=0; i<s.size(); i++ ){
            if( value<s[i] ){
                value = s[i];
                index = i;
            }
        }
        minTime = min( minTime, value+time);
        if( value<=T )
            break;
        s[index] = T;
        s.push_back(value-T);
        time++;
    }
    time = 0;
    s = t;
    while( 1 ){
        int value = 0;
        int index = 0;
        for( int i=0; i<s.size(); i++ ){
            if( value<s[i] ){
                value = s[i];
                index = i;
            }
        }
        minTime = min( minTime, value+time);
        if( value==1 )
            break;
        s[index] = value/2;
        s.push_back(value-value/2);
        time++;
    }
    return minTime;
}

int main()
{
    int n;
    FILE *fp;
	fp = fopen( "B-small-attempt2.in", "r");
	FILE *fp2;
	fp2 = fopen( "output123.txt", "w");
	fscanf(fp, "%d", &n);
    for( int i=0; i<n; i++ ){
        int m;
        fscanf(fp, "%d", &m);
        vector<int> numbers;
        numbers.resize(m);
        for( int j=0; j<m; j++ )
            fscanf(fp, "%d", &numbers[j]);
        /*
        for( int j=0; j<m; j++ )
            cout<<numbers[j]<<" ";
        cout<<endl;
        cout<<"Solution: "<<panCakes(numbers)<<endl;

        for( int j=0; j<m; j++ )
            fprintf(fp2, "%d ", numbers[j]);
        fprintf(fp2, "\nSolution: %d\n", panCakes(numbers));
        */
        fprintf(fp2, "Case #%d: %d\n", i+1, panCakes(numbers));
    }
    fclose(fp);
    fclose(fp2);
    return 0;
}
