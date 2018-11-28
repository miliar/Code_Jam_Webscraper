#include <iostream>
#include <cstdio>
#include <vector>

using namespace std;

int N;
bool possible[17];
vector<int> cards;

int main()
{
    FILE *fin = fopen("a.in", "r");
    FILE *fout = fopen("a.out", "w+");
    fscanf(fin, "%d", &N);
    for(int i=0; i<N; i++){
        cards.clear();
        int a, b;
        fscanf(fin, "%d", &a);
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                int temp;
                fscanf(fin, "%d", &temp);
                if(j+1 == a){
                    possible[temp] = true;
                } else {
                    possible[temp] = false;
                }
            }
        }
        fscanf(fin, "%d", &b);
        for(int j=0; j<4; j++){
            for(int k=0; k<4; k++){
                int temp2;
                fscanf(fin, "%d", &temp2);
                if(j+1 == b && possible[temp2]){
                    cards.push_back(temp2);
                }
            }
        }
        if(cards.size() == 0){
            fprintf(fout, "Case #%d: Volunteer cheated!\n", i+1);
        } else if(cards.size() == 1){
            fprintf(fout, "Case #%d: %d\n", i+1, cards[0]);
        } else {
            fprintf(fout, "Case #%d: Bad magician!\n", i+1);
        }
    }
    return 0;
}
