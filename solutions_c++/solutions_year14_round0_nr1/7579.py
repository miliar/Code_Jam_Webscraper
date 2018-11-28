#include<iostream>
#include<map>
#include<vector>
#include<cstdio>
using namespace std;
#define NUM 4

map<int,int> table;
vector<int> answer;

int main(){
    int t, count = 1, number;
    int i, j, choice1;
    scanf("%d", &t);
    while( t-- ){
        table.clear();
        answer.clear();
        scanf("%d", &choice1);
        for( i=1; i<=NUM; i++){
            for( j=1; j<=NUM; j++){
                scanf("%d", &number);
                if( i==choice1)
                    table[number] = 1;
            }
        }
        scanf("%d", &choice1);
        for( i=1; i<=NUM; i++){
            for( j=1; j<=NUM; j++){
                scanf("%d", &number);
                if( i==choice1 && table[number])
                    answer.push_back(number);
            }
        }
        printf("Case #%d: ", count++);
        if( answer.size() == 1){
            printf("%d\n", answer[0]);
        }else if( answer.size() > 1){
            printf("Bad magician!\n");
        }else
            printf("Volunteer cheated!\n");
    }
    return 0;
}

