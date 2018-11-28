#include <iostream>
#include <vector>
#include <stdio.h>
#include <string.h>
#include <map>
using namespace std;

int validStanding(vector<int> s){
    int number = 0;
    int sum = 0;
    for( int i=0; i<s.size()-1; i++ ){
        if(sum==i&&s[i]==0 ){
            s[i]=1;
            number ++;
        }
        sum += s[i];
    }
    return number;
}

int main()
{
    int n;
    FILE *fp;
	fp = fopen( "A-small-attempt1.in", "r");
	FILE *fp2;
	fp2 = fopen( "output.txt", "w");
	fscanf(fp, "%d", &n);
    for( int i=0; i<n; i++ ){
        int m;
        fscanf(fp, "%d", &m);
        m++;
        char *input;
        fscanf(fp, "%s", input);
        vector<int> numbers;
        for( int j=0; j<m; j++ )
            numbers.push_back((int)(input[j])-48);
        fprintf(fp2, "Case #%d: %d\n", i+1, validStanding(numbers));
    }
    fclose(fp);
    fclose(fp2);
    return 0;
}
