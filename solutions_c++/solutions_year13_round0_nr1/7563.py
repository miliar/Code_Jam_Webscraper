#include <cstdio>
using namespace std;

void print_grid(char grid[][5]){
    for(int j=0; j<4; ++j){
        printf("%s\n",grid[j]);
    }
    printf("\n");
}

void process_grid_pos(char grid[][5], char * elem, char * draw, int i, int j){
    if(grid[i][j] == '.'){
        *draw = '.';
        *elem = 1;
    }
    else{
        if(grid[i][j] == 'T')
        ;
        else if(*elem == 0)
            *elem = grid[i][j];
        else if(*elem == grid[i][j])
            ;
        else{
            *elem = 1;
        }
    }

}

char process_grid(char grid[][5]){
    char elem;
    char draw = 'D';
    // see rows
    for(int i=0; i<4; ++i){
        elem = 0;
        for(int j=0; j<4; ++j){
            process_grid_pos(grid, &elem, &draw, i, j);
            if(elem == 1)
                break;
        }
        if(elem != 1){
            return elem;
        }
    }

    // see columns
    for(int j=0; j<4; ++j){
        elem = 0;
        for(int i=0; i<4; ++i){
            process_grid_pos(grid, &elem, &draw, i, j);
            if(elem == 1)
                break;
        }
        if(elem != 1){
            return elem;
        }
    }
    elem = 0;
    int j=0;
    for(int i=0; i<4; ++i, ++j){
        process_grid_pos(grid, &elem, &draw, i, j);
        if(elem == 1)
            break;
    }
    if(elem != 1){
        return elem;
    }

    elem = 0; j=3;
    for(int i=0; i<4; ++i, --j){
        process_grid_pos(grid, &elem, &draw, i, j);
        if(elem == 1)
            break;
    }
    if(elem != 1){
        return elem;
    }
    return draw;
}



int main(){
    char grid[4][5];
    int t;
    scanf("%d",&t);
    for(int i=0; i<t; ++i){
        for(int j=0; j<4; ++j){
            scanf("%s",grid[j]);
        }
        char out = process_grid(grid);
        if(out == 'X'){
            printf("Case #%d: X won\n",i+1);
        }
        else if(out == 'O'){
            printf("Case #%d: O won\n",i+1);
        }
        else if(out == 'D'){
            printf("Case #%d: Draw\n",i+1);
        }
        else if(out == '.'){
            printf("Case #%d: Game has not completed\n",i+1);
        }

        //print_grid(grid);
    }
    return 0;

}
