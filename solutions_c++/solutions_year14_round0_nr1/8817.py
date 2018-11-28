#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>

using namespace std;

int main()
{
    int cnt;

    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &cnt);
    
    int iterate_time=1;
    while(iterate_time<=cnt){
        int first_choice, second_choice;
        int fm[4][4], sm[4][4];
        scanf("%d", &first_choice);
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                scanf("%d", &fm[i][j]);
            }
        }
        scanf("%d", &second_choice);
        for(int i=0; i<4; i++){
            for(int j=0; j<4; j++){
                scanf("%d", &sm[i][j]);
            }
        }
        first_choice--;
        second_choice--;
        
        map<int, bool> m;
        for(int i=0; i<4; ++i){
            m[fm[first_choice][i]]=true;
        }
        
        int cnt_match=0;
        int result;
        for(int i=0; i<4; i++){
            if(m.find(sm[second_choice][i])!=m.end()){
                result=sm[second_choice][i];
                cnt_match++;
            }
        }
        
        switch(cnt_match){
            case 0:
                cout << "Case #" << iterate_time << ": " << "Volunteer cheated!" << endl;
                break;
            case 1:
                cout << "Case #" << iterate_time << ": " << result << endl;
                break;
            default:
                cout << "Case #" << iterate_time << ": " << "Bad magician!" << endl;
                break;
        }
        iterate_time++;
    }
}

